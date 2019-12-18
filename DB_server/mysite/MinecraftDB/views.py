from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Terrain
from django.db import connection,transaction

def index(request):
    return render(request,'MinecraftDB/index.html')

def Search(request, search_name):
    cursor=connection.cursor()
    cursor.execute('select Introduction_text from MinecraftDB_Terrain')
    search_object=cursor.fetchone()[0]

    # search_object = Terrain.objects.get(Terrain, Terrain_name=search_name)
    return render(request, 'MinecraftDB/index.html', {'search_object': search_object})

def reply_login(request):
    if(request.method=="POST"):
        # 輸入帳號密碼
        if('account' in request.POST):
            #print(request.POST['account'])
            # 確認有沒有輸入正確
            if(request.POST['account']=="" or request.POST['password']==""):
                return render(request, 'static/login/login.html',{'err_acc':"請輸入正確的 account 或 password"})
            #確認有沒有此人
            cursor=connection.cursor()
            cursor.execute("select Member_name from MinecraftDB_member where Account_number LIKE '"+request.POST['account']+"' and Password LIKE '"+request.POST['password']+"'")
            # cursor.execute("select Member_name from MinecraftDB_member where Account_number LIKE '%s' and Password LIKE '%s'",["ppaa","ppaa"])
            ans=cursor.fetchone()
            #print(ans)
            if ans is None:
                print("no ans")
                return render(request, 'static/login/login.html',{'err_acc':"請輸入正確的 account 或 password"})
            else :
                return redirect("/MinecraftDB/main/"+ans[0]+"/")         
        if('nickname' in request.POST):
            print(request.POST['nickname'])
            if(request.POST['nickname']==""):
                return render(request, 'static/login/login.html',{'no_nike':"請輸入nickname"})
            else:
                return redirect("/MinecraftDB/main/"+"guest"+"/")
        # DB尋找


def reply_post(request):
    print("get")
    print(request.POST['Contents'])
    cursor=connection.cursor()
    title=request.POST['title']
    context=request.POST['Contents']
    print(title+" "+context)
    cursor.execute("INSERT INTO MinecraftDB_member_diary (Title, Diary,Member_Diary_name) values (%s, %s,%s)", [title,"someone", context])
    #return render(request, 'MinecraftDB/login.html')
    return redirect("/MinecraftDB/main/"+"1"+"/")

def login(request):
    return render(request, 'static/login/login.html')

def main(request,username):
    cursor=connection.cursor()
    cursor.execute('select Introduction_text from MinecraftDB_Terrain')
    search_object=cursor.fetchone()[0]
    return render(request, 'static/main_page/main.html',{'Username':username})

def producer(request):
    return render(request, 'static/Producer/producer.html')

def post(request):
    return render(request, 'static/post/post.html')

def ALLpost(request):
    List=[{'Poster':"willy",'Title':"loooooool",'content':"nooo"}]
    return render(request, 'static/Allpost/Allpost.html',{'List':List,'Username':'lulalabana'})