import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Terrain
from django.db import connection, transaction
from django.views import View

flag = 0


def index(request):
    return render(request, 'MinecraftDB/index.html')


def Search(request, search_name):
    cursor = connection.cursor()
    cursor.execute('select Introduction_text from MinecraftDB_Terrain')
    search_object = cursor.fetchone()[0]

    # search_object = Terrain.objects.get(Terrain, Terrain_name=search_name)
    return render(request, 'MinecraftDB/index.html', {'search_object': search_object})


def reply_login(request):
    if(request.method == "POST"):
        # 輸入帳號密碼
        if('account' in request.POST):
            # print(request.POST['account'])
            # 確認有沒有輸入正確
            if(request.POST['account'] == "" or request.POST['password'] == ""):
                return render(request, 'static/login/login.html', {'err_acc': "請輸入正確的 account 或 password"})
            # 確認有沒有此人
            cursor = connection.cursor()
            cursor.execute("select Member_name from MinecraftDB_member where Account_number LIKE '" +
                           request.POST['account']+"' and Password LIKE '"+request.POST['password']+"'")
            # cursor.execute("select Member_name from MinecraftDB_member where Account_number LIKE '%s' and Password LIKE '%s'",["ppaa","ppaa"])
            ans = cursor.fetchone()
            # print(ans)
            if ans is None:
                print("no ans")
                return render(request, 'static/login/login.html', {'err_acc': "請輸入正確的 account 或 password"})
            else:
                request.session['username'] = ans[0]
                request.session['flag'] =  '0'
                
                return redirect("/MinecraftDB/main/"+request.session['username']+"/")
        if('nickname' in request.POST):
            print(request.POST['nickname'])
            if(request.POST['nickname'] == ""):
                return render(request, 'static/login/login.html', {'no_nike': "請輸入nickname"})
            else:
                request.session['flag'] = '1'
                request.session['username'] = request.POST['nickname']
                return redirect("/MinecraftDB/main/"+"guest"+"/")
        # DB尋找


def reply_post(request):
    print("get")
    print(request.POST['content'])
    cursor = connection.cursor()
    title = request.POST['title']
    context = request.POST['content']
    print(title+" "+context)
    cursor.execute("INSERT INTO MinecraftDB_member_diary (Title, Diary,Member_Diary_name) values (%s, %s,%s)", [
                   title, "someone", context])
    # return render(request, 'MinecraftDB/login.html')
    return redirect("/MinecraftDB/main/"+"1"+"/")


def login(request):
    return render(request, 'static/login/login.html')


def main(request, username):
    cursor = connection.cursor()
    cursor.execute('select Introduction_text from MinecraftDB_Terrain')
    search_object = cursor.fetchone()[0]
    return render(request, 'static/main_page/main.html', {'Username': request.session['username']})


def producer(request):
    return render(request, 'static/Producer/producer.html')


def post(request, username):
    cursor = connection.cursor()
    cursor.execute("select Member_Diary_name,Diary,Title,id from MinecraftDB_member_diary WHERE Member_Diary_name LIKE '" +
                   request.session['username']+"'")
    search_Diary = cursor.fetchall()
    List = []
    for item in search_Diary:
        list_s = {'Poster': item[0], 'Title': item[2],
                  'content': item[1], 'id': item[3]}
        List.append(list_s)
    # print(List)
    # request.session["username"] = username
    if len(List) == 0:
        print("no")
        return render(request, 'static/post/post.html', {'List': List, 'Username': request.session['username'], 'ALTER': "目前沒有貼文，去發你的第一篇貼文吧!!"})
    else:
        print("yes")
        return render(request, 'static/post/post.html', {'List': List, 'Username': request.session['username']})


def ALLpost(request):
    cursor = connection.cursor()
    cursor.execute(
        'select Member_Diary_name,Diary,Title from MinecraftDB_member_diary')
    search_Diary = cursor.fetchall()
    # print(search_Diary)
    List = []
    for item in search_Diary:
        list_s = {'Poster': item[0], 'Title': item[2], 'content': item[1]}
        List.append(list_s)

    return render(request, 'static/Allpost/Allpost.html', {'List': List, 'Username': request.session['username']})


def getPost(request):
    print(request.POST)
    cursor = connection.cursor()
    title = request.POST['Title']
    context = request.POST['Contents']
    cursor.execute("INSERT INTO MinecraftDB_member_diary (Title, Diary,Member_Diary_name) values (%s, %s,%s)", [
                   title, context, request.session['username']])
    return redirect("/MinecraftDB/post/"+request.session['username']+"/")


def deletePost(request):
    print(request.POST)
    username = request.POST['Username'].replace("By ", "")
    title = request.POST['Title'].replace("Title：", "")
    postID = request.POST['ID']
    print(postID)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM MinecraftDB_member_diary WHERE id ="+postID)
    # print(request.session["username"])
    return render(request, 'static/login/login.html')


def profile(request):
    cursor = connection.cursor()
    cursor.execute("select Member_name,Account_number,Password,Profile from MinecraftDB_member where Member_name LIKE '" +
                   request.session['username']+"'")
    # cursor.execute("select Member_name from MinecraftDB_member where Account_number LIKE '%s' and Password LIKE '%s'",["ppaa","ppaa"])
    ans = cursor.fetchone()
    print(ans)
    return render(request, 'static/profile/profile.html', {'Password': ans[2], 'Account': ans[1], 'Info': ans[3], 'Username': request.session['username']})


def editPost(request):
    print(request.POST)
    ID = request.POST['postID']
    content = request.POST['Contents']
    print(ID, content)
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE MinecraftDB_member_diary SET Diary = '"+content+"' WHERE ID = "+ID)
    # print(request.session["username"])
    return render(request, 'static/login/login.html')


def signup(request):
    return render(request, 'static/sign_up/signup.html')


def aggressive_mobs(request):
    return render(request, 'static/main_page/aggressive_mobs.html', {'Username': request.session['username']})


def neutral_mobs(request):
    return render(request, 'static/main_page/neutral_mobs.html')


def Overworld(request):
    return render(request, 'static/main_page/Overworld.html')


def Nether(request):
    return render(request, 'static/main_page/Nether.html')


def End(request):
    return render(request, 'static/main_page/End.html')


def tools(request):
    return render(request, 'static/main_page/tools.html')


def foods(request):
    return render(request, 'static/main_page/foods.html')


def building_materials(request):
    return render(request, 'static/main_page/building_materials.html')


def ores(request):
    return render(request, 'static/main_page/ores.html')


def biome(request):
    return render(request, 'static/main_page/biome.html')


def structures(request):
    return render(request, 'static/main_page/structures.html')

def Steve(request):
    return render(request, 'static/main_page/Steve.html')


def backtomain(request):
    
    if(request.session['flag'] == '0'):
        return redirect("/MinecraftDB/main/"+request.session['username']+"/")
    else:
        return redirect("/MinecraftDB/main/"+"guest"+"/")
