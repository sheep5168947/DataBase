# Generated by Django 2.1.5 on 2019-12-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinecraftDB', '0006_weather_world'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building_Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Building_Materials_name', models.CharField(max_length=20)),
                ('Texture', models.CharField(max_length=20)),
                ('Anti_Riot', models.FloatField(default=0)),
            ],
        ),
    ]
