# Generated by Django 3.2.6 on 2021-09-21 00:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_auto_20210921_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_status',
            name='Friend_List',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]
