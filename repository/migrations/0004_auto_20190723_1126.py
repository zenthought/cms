# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-23 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20190723_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, default='img/article/123.jpg', upload_to='img/article/', verbose_name='显示图片'),
        ),
    ]
