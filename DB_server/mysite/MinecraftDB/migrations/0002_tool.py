# Generated by Django 2.1.5 on 2019-12-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinecraftDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tool_name', models.CharField(max_length=20)),
                ('Durable', models.FloatField(default=0)),
            ],
        ),
    ]
