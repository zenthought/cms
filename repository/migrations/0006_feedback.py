# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20190723_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/feedback/')),
                ('back_type', models.IntegerField(choices=[(0, '未分类'), (1, '学习笔记'), (2, '学员评价'), (3, '入职邀约')], default=0)),
            ],
        ),
    ]
