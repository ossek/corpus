# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deathtally', '0004_auto_20141217_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='person',
        ),
        migrations.RemoveField(
            model_name='character',
            name='actor',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.RemoveField(
            model_name='character',
            name='inMedia',
        ),
        migrations.DeleteModel(
            name='DeathtallyInstance',
        ),
        migrations.RemoveField(
            model_name='event',
            name='inMedia',
        ),
        migrations.RemoveField(
            model_name='film',
            name='mediaMetaData',
        ),
        migrations.RemoveField(
            model_name='film',
            name='timeInfo',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ofGame',
        ),
        migrations.DeleteModel(
            name='GameInstance',
        ),
        migrations.RemoveField(
            model_name='player',
            name='person',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='on',
        ),
        migrations.DeleteModel(
            name='MediaMetaData',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='TimeInfo',
        ),
        migrations.RemoveField(
            model_name='death',
            name='who',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
        migrations.RemoveField(
            model_name='deathtallysolution',
            name='ofFilm',
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.AddField(
            model_name='death',
            name='actorname',
            field=models.TextField(default='wilbert eggbert'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathtallysolution',
            name='filmImageSrc',
            field=models.TextField(default='n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathtallysolution',
            name='filmTitle',
            field=models.TextField(default='polar justice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='death',
            name='when',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
