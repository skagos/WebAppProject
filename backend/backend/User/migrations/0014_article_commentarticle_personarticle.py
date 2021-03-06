# Generated by Django 3.2.6 on 2021-09-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_connection_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Address', models.EmailField(max_length=240)),
                ('Comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Address', models.EmailField(max_length=240)),
                ('Interesting', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Address', models.EmailField(max_length=240)),
                ('TextArticle', models.TextField(null=True)),
                ('Image', models.FileField(blank=True, null=True, upload_to='article_images')),
                ('CommentUsers', models.ManyToManyField(blank=True, to='User.CommentArticle')),
                ('InterestingUsers', models.ManyToManyField(blank=True, to='User.PersonArticle')),
            ],
        ),
    ]
