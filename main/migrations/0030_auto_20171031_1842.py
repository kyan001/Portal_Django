# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20171031_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='status',
            field=models.CharField(choices=[('active', (('inprogress', '进行中'), ('follow', '追剧中'), ('todo', '待阅读'), ('error', '出错'))), ('archive', (('done', '已完成'), ('giveup', '冻结中')))], max_length=50),
        ),
    ]
