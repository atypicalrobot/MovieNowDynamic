# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_recommendation_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='recommends', to=settings.AUTH_USER_MODEL),
        ),
    ]