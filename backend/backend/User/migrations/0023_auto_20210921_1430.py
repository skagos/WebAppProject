# Generated by Django 3.2.6 on 2021-09-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_alter_friend_status_friend_list'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend_List',
        ),
        migrations.RemoveField(
            model_name='article',
            name='CommentUsers',
        ),
        migrations.AddField(
            model_name='article',
            name='CommentUsers',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='article',
            name='InterestingUsers',
        ),
        migrations.AddField(
            model_name='article',
            name='InterestingUsers',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='friend_status',
            name='Email_Address',
            field=models.EmailField(max_length=240, null=True),
        ),
        migrations.DeleteModel(
            name='CommentArticle',
        ),
        migrations.DeleteModel(
            name='PersonArticle',
        ),
    ]
