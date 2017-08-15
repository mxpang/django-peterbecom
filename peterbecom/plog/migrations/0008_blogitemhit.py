# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plog', '0007_blogitem_screenshot_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogItemHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('blogitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plog.BlogItem')),
            ],
        ),
    ]