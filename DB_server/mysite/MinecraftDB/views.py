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


def Search(request):
    if request.method == "POST":
        print("get")
    search_key=request.POST["search"]
    cursor = connection.cursor()
    #攻擊生物
    cursor.execute("select MinecraftDB_attack_creature.id,Attack_Creature_name,Search_range,HealthPoints,Attack from MinecraftDB_attack_creature,MinecraftDB_creature where Attack_Creature_name=Creature_name AND Attack_Creature_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"攻擊性生物",'Search_range':search_object[2],'HP':search_object[3],'attack':search_object[4]})
    #中立生物
    cursor.execute("select MinecraftDB_neutral_creature.id,Neutral_Creature_name,HealthPoints,Attack,Can_grow,Can_Trap from MinecraftDB_neutral_creature,MinecraftDB_creature where Neutral_Creature_name=Creature_name AND Neutral_Creature_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"中立性生物",'can_trap':search_object[5],'can_grow':search_object[4],'HP':search_object[2],'attack':search_object[3]})
    
    #工具
    cursor.execute("select MinecraftDB_tool.id,Tool_name,Durable,Rarity,Max_Quantity from MinecraftDB_tool,MinecraftDB_item where tool_name=Item_name AND Tool_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:       
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"工具",'Durable':search_object[2],'Rarity':search_object[3],'Max_Quanity':search_object[4]})
    #食物
    cursor.execute("select MinecraftDB_food.id,Food_name,Satiety,Rarity,Max_Quantity from MinecraftDB_food,MinecraftDB_item where Food_name=Item_name AND Food_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:       
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"食物",'Satiety':search_object[2],'Rarity':search_object[3],'Max_Quanity':search_object[4]})
   
    #建材
    cursor.execute("select MinecraftDB_building_materials.id,Building_Materials_name,Texture,Anti_Riot,Rarity,Max_Quantity from MinecraftDB_building_materials, MinecraftDB_item where Building_Materials_name=Item_name AND Building_Materials_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:       
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"建材",'Texture':search_object[2],'Anti_Riot':search_object[3],'Rarity':search_object[4],'Max_Quanity':search_object[5]})
    #礦物
    cursor.execute("select MinecraftDB_mineral.id,Mineral_name,Generate_Range,Rarity,Max_Quantity from MinecraftDB_mineral,MinecraftDB_item where Mineral_name=Item_name AND Mineral_name='"+search_key+"'")
    search_object = cursor.fetchone()
    if search_object is not None:       
        return render(request, 'static/main_page/Search.html',{'Search':search_key,'type':"礦物",'Generate_Range':search_object[2],'Rarity':search_object[3],'Max_Quanity':search_object[4]})
    #世界
    
    # search_object = Terrain.objects.get(Terrain, Terrain_name=search_name)

    return render(request, 'static/main_page/Search.html',{'Search':search_key,"a":'A',"no_answer":"1"})


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
            #print(ans[0])
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
    cursor = connection.cursor()
    cursor.execute(
        'select MinecraftDB_attack_creature.id,Attack_Creature_name,Search_range,HealthPoints,Attack from MinecraftDB_attack_creature,MinecraftDB_creature where Attack_Creature_name=Creature_name')
    search_attack_creature = cursor.fetchall()
    print(search_attack_creature)
    List = []
    for item in search_attack_creature:
        list_s = {'mob_id': item[0], 'mob_name': item[1], 'mob_search_range': item[2],'HP':item[3],'attack':item[4]}
        List.append(list_s)
    return render(request, 'static/main_page/aggressive_mobs.html', {'Username': request.session['username'],'List':List})


def neutral_mobs(request):
    cursor = connection.cursor()
    cursor.execute(
        'select MinecraftDB_neutral_creature.id,Neutral_Creature_name,HealthPoints,Attack,Can_grow,Can_Trap from MinecraftDB_neutral_creature,MinecraftDB_creature where Neutral_Creature_name=Creature_name')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'mob_id': item[0], 'mob_name': item[1], 'HP': item[2],'Attack':item[3],'can_grow':item[4],'can_trap':item[5]}
        List.append(list_s)
    return render(request, 'static/main_page/neutral_mobs.html',{'Username': request.session['username'],'List':List})


def Overworld(request):
    return render(request, 'static/main_page/Overworld.html', {'Username': request.session['username']})


def Nether(request):
    return render(request, 'static/main_page/Nether.html', {'Username': request.session['username']})


def End(request):
    return render(request, 'static/main_page/End.html', {'Username': request.session['username']})


def tools(request):
    cursor = connection.cursor()
    cursor.execute('select MinecraftDB_tool.id,Tool_name,Durable,Rarity,Max_Quantity from MinecraftDB_tool,MinecraftDB_item where tool_name=Item_name')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1], 'Durable': item[2],'Rarity':item[3],'Max_Quanity':item[4]}
        List.append(list_s)
    return render(request, 'static/main_page/tools.html',{'Username': request.session['username'],'List':List})


def foods(request):
    cursor = connection.cursor()
    cursor.execute(
        'select MinecraftDB_food.id,Food_name,Satiety,Rarity,Max_Quantity from MinecraftDB_food,MinecraftDB_item where Food_name=Item_name')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1], 'Satiety': item[2],'Rarity':item[3],'Max_Quanity':item[4]}
        List.append(list_s)
    return render(request, 'static/main_page/foods.html',{'Username': request.session['username'],'List':List})


def building_materials(request):
    cursor = connection.cursor()
    cursor.execute(
        'select MinecraftDB_building_materials.id,Building_Materials_name,Texture,Anti_Riot,Rarity,Max_Quantity from MinecraftDB_building_materials LEFT OUTER JOIN MinecraftDB_item on Building_Materials_name=Item_name')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1], 'Texture': item[2],'Anti_Riot': item[3],'Rarity':item[4],'Max_Quanity':item[5]}
        List.append(list_s)
    return render(request, 'static/main_page/building_materials.html',{'Username': request.session['username'],'List':List})



def ores(request):
    cursor = connection.cursor()
    cursor.execute(
        'select MinecraftDB_mineral.id,Mineral_name,Generate_Range,Rarity,Max_Quantity from MinecraftDB_mineral LEFT OUTER JOIN MinecraftDB_item on Mineral_name=Item_name')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1], 'range': item[2],'Rarity':item[3],'Max_Quanity':item[4]}
        List.append(list_s)
    return render(request, 'static/main_page/ores.html',{'Username': request.session['username'],'List':List})


def biomes(request):
    cursor = connection.cursor()
    cursor.execute('select id,Terrain_name from MinecraftDB_terrain')
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1]}
        List.append(list_s)
    return render(request, 'static/main_page/biome.html',{'Username': request.session['username'],'List':List})

def biome(request):
    cursor = connection.cursor()
    cursor.execute("select id,Terrain_name from MinecraftDB_terrain")
    search = cursor.fetchall()
    print(search)
    List = []
    for item in search:
        list_s = {'id': item[0], 'name': item[1]}
        List.append(list_s)
    return render(request, 'static/main_page/biome.html',{'Username': request.session['username'],'List':List})

def structures(request):
    cursor = connection.cursor()
    cursor.execute('select Structure_name,Structure_Explain,Terrain_Call from MinecraftDB_structure')
    search = cursor.fetchall()
    List = []
    for item in search:
        list_s = {'name': item[0],'where': item[2], 'Introduction': item[1]}
        List.append(list_s)
    return render(request, 'static/main_page/structures.html',{'Username': request.session['username'],'List':List})



def Steve(request):
    return render(request, 'static/main_page/Steve.html', {'Username': request.session['username']})


def backtomain(request):
    
    if(request.session['flag'] == '0'):
        return redirect("/MinecraftDB/main/"+request.session['username']+"/")
    else:
        return redirect("/MinecraftDB/main/"+"guest"+"/")
