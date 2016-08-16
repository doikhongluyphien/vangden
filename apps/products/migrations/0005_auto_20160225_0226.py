# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160219_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attachment',
            field=models.FileField(blank=True, max_length=500, upload_to='attachments'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'Hết Hàng'), (1, 'Còn Hàng')], default=1),
        ),
    ]
