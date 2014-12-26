# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deathtally', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeathtallyInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeathtallySolution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ofFilm', models.ForeignKey(to='deathtally.Film')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('mediaMetaData', models.ForeignKey(to='deathtally.MediaMetaData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ofGame', models.ForeignKey(to='deathtally.GameInstance')),
                ('person', models.ForeignKey(to='deathtally.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='death',
            name='inDeathtally',
            field=models.ForeignKey(to='deathtally.DeathtallySolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='death',
            name='when',
            field=models.ForeignKey(to='deathtally.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='death',
            name='who',
            field=models.ForeignKey(to='deathtally.Character'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='person',
            name='inMedia',
        ),
        migrations.AddField(
            model_name='character',
            name='inMedia',
            field=models.ForeignKey(to='deathtally.MediaMetaData', default=0),
            preserve_default=False,
        ),
    ]
