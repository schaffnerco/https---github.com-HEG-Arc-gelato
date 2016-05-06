# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0010_remove_glace_bac'),
    ]

    operations = [
        migrations.AddField(
            model_name='glace',
            name='bac',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='congelateur.Bac', verbose_name='Bac ou trouver la glace'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glace',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='congelateur.Categorie', verbose_name='Catégorie de la glace'),
            preserve_default=False,
        ),
    ]
