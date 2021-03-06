# Generated by Django 2.1.5 on 2019-12-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack_Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attack_Creature_name', models.CharField(max_length=20)),
                ('Search_range', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creature_name', models.CharField(max_length=20)),
                ('HealthPoints', models.IntegerField(default=0)),
                ('Attack', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Neutral_Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Neutral_Creature_name', models.CharField(max_length=20)),
                ('Can_grow', models.BooleanField()),
                ('Can_Trap', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Terrain_name', models.CharField(max_length=20)),
                ('Introduction_text', models.TextField()),
                ('Texture', models.TextField()),
            ],
        ),
    ]
