# Generated by Django 3.2.6 on 2021-09-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_friend_list_friend_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Address_Sender', models.EmailField(max_length=240)),
                ('Email_Address_Receiver', models.EmailField(max_length=240)),
            ],
        ),
    ]
