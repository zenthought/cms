# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-23 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.ArticleDetail', verbose_name='文章详情'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default='', upload_to='img/article/', verbose_name='显示图片'),
        ),
    ]
