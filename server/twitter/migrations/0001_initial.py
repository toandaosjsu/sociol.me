# Generated by Django 3.1.2 on 2020-11-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterModel',
            fields=[
                ('email', models.CharField(default='', max_length=70)),
                ('name', models.CharField(default='', max_length=70)),
                ('user_id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('screen_name', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=1000)),
                ('followers_count', models.IntegerField(default=0)),
                ('friends_count', models.IntegerField(default=0)),
                ('auth_token', models.CharField(default='', max_length=2000)),
                ('auth_token_secret', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
