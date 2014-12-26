# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deathtally', '0002_auto_20141213_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('tmdbPersonId', models.IntegerField()),
                ('person', models.ForeignKey(to='deathtally.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='gamesolution',
            name='mediaMetaData',
        ),
        migrations.DeleteModel(
            name='GameSolution',
        ),
        migrations.AddField(
            model_name='character',
            name='tmdbCreditId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='tmdbFilmId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
