# Generated by Django 3.2.6 on 2021-09-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_delete_personad'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Comments',
            field=models.TextField(null=True),
        ),
    ]
