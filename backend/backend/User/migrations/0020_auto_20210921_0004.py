# Generated by Django 3.2.6 on 2021-09-21 00:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_friend_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_status',
            name='Friend_List',
        ),
        migrations.AddField(
            model_name='friend_status',
            name='Friend_List',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]