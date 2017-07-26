# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=140, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='storyboard.Post')),
            ],
        ),
    ]