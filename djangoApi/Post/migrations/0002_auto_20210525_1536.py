# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-25 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='dislike_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reactions', to='Post.DislikePost'),
        ),
        migrations.AddField(
            model_name='reactions',
            name='like_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reactions', to='Post.LikePost'),
        ),
    ]
