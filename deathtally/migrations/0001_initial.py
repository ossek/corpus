# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('characterName', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('atTimeMillis', models.IntegerField(default=0)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('wilhelmScreamCount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaMetaData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('realName', models.TextField()),
                ('inMedia', models.ForeignKey(to='deathtally.MediaMetaData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('on', models.ForeignKey(default=None, to='deathtally.MediaMetaData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('millisLength', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='film',
            name='mediaMetaData',
            field=models.ForeignKey(to='deathtally.MediaMetaData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='timeInfo',
            field=models.ForeignKey(to='deathtally.TimeInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='inMedia',
            field=models.ForeignKey(default=None, to='deathtally.MediaMetaData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='person',
            field=models.ForeignKey(to='deathtally.Person'),
            preserve_default=True,
        ),
    ]
