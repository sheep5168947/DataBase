# Generated by Django 2.1.5 on 2019-12-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinecraftDB', '0004_mineral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Structure_name', models.CharField(max_length=20)),
                ('Structure_Explain', models.CharField(max_length=20)),
                ('Terrain_Call', models.CharField(max_length=20)),
            ],
        ),
    ]
