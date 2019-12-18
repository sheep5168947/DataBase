from django.db import models
# Create your models here.
class Terrain(models.Model):
    #名稱
    Terrain_name=models.CharField(max_length=20)
    #簡介說明
    Introduction_text = models.TextField()
    #值被材質
    Texture = models.TextField()

    def __str__(self):
        return self.Terrain_name

class Creature(models.Model):
    #名稱
    Creature_name=models.CharField(max_length=20)
    #血量
    HealthPoints = models.IntegerField(default=0)
    #攻擊力
    Attack = models.IntegerField(default=0)
    #移動速度
    #掉落物
    def __str__(self):
        return self.Creature_name

class Attack_Creature(models.Model):
    #名稱
    Attack_Creature_name=models.CharField(max_length=20)
    #搜索範圍
    Search_range=models.FloatField(default=0)
    def __str__(self):
        return self.Attack_Creature_name
class Neutral_Creature(models.Model):
    #名稱
    Neutral_Creature_name=models.CharField(max_length=20)
    #可成長
    Can_grow=models.BooleanField()
    # 可誘捕
    Can_Trap=models.BooleanField()
    def __str__(self):
        return self.Neutral_Creature_name

class Tool(models.Model):
    #名稱
    Tool_name=models.CharField(max_length=20)
    #耐久
    Durable=models.FloatField(default=0)
    def __str__(self):
        return self.Tool_name

class Item(models.Model):
    #名稱
    Item_name=models.CharField(max_length=20)
    #稀有度
    Rarity=models.IntegerField(default=0)
    # 最大堆疊數量
    Max_Quantity=models.BooleanField()
    def __str__(self):
        return self.Item_name
class Food(models.Model):
    #名稱
    Food_name=models.CharField(max_length=20)
    #飽食度
    Satiety=models.FloatField(default=0)
    def __str__(self):
        return self.Food_name
class Building_Materials(models.Model):
    #名稱
    Building_Materials_name=models.CharField(max_length=20)
    #材質
    Texture=models.CharField(max_length=20)
    #抗暴程度
    Anti_Riot=models.FloatField(default=0)
    def __str__(self):
        return self.Building_Materials_name

class Mineral(models.Model):
    #名稱
    Mineral_name=models.CharField(max_length=20)
    #生成範圍
    Generate_Range=models.FloatField(default=0)
    def __str__(self):
        return self.Mineral_name

class World(models.Model):
    #名稱
    World_name=models.CharField(max_length=20)
    #到達方式
    Arrival_Way=models.CharField(max_length=20)
    #說明
    World_Explain=models.CharField(max_length=20)
    #可產生地形
    Terrain_Generate=models.CharField(max_length=20)
    #形成天氣
    Weather_Generate=models.CharField(max_length=20)
    def __str__(self):
        return self.World_name

class Weather(models.Model):
    #名稱
    Weather_name=models.CharField(max_length=20)
    #說明
    Weather_Explain=models.CharField(max_length=20)
    def __str__(self):
        return self.Weather_name

class Structure(models.Model):
    #名稱
    Structure_name=models.CharField(max_length=20)
    #說明
    Structure_Explain=models.CharField(max_length=20)
    #地形名稱
    Terrain_Call=models.CharField(max_length=20)
    def __str__(self):
        return self.Structure_name

class Member(models.Model):
    #會員名字
    Member_name=models.CharField(max_length=20)
    #帳號
    Account_number=models.CharField(max_length=20)
    #密碼
    Password=models.CharField(max_length=20)
    #個人簡介
    Profile=models.TextField()
    def __str__(self):
        return self.Member_name
class Member_Diary(models.Model):
    #會員名字
    Member_Diary_name=models.CharField(max_length=20)
    #文章
    Diary=models.TextField()
    #標題
    Title=models.CharField(max_length=20,default='myDiary')
    #圖片
    picture = models.ImageField(upload_to='pictures', default='',null=True)
    def __str__(self):
        return self.Member_Diary_name