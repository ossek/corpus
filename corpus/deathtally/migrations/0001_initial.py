# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeMedia',
            fields=[
                ('media_ptr', models.OneToOneField(to='deathtally.Media', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('minutesLength', models.IntegerField()),
            ],
            options={
            },
            bases=('deathtally.media',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('timemedia_ptr', models.OneToOneField(to='deathtally.TimeMedia', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
            ],
            options={
            },
            bases=('deathtally.timemedia',),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('timemedia_ptr', models.OneToOneField(to='deathtally.TimeMedia', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('wilhelmScreamCount', models.IntegerField()),
            ],
            options={
            },
            bases=('deathtally.timemedia',),
        ),
        migrations.AddField(
            model_name='tag',
            name='on',
            field=models.ForeignKey(to='deathtally.Media', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='inFilm',
            field=models.ForeignKey(to='deathtally.TimeMedia', default=None),
            preserve_default=True,
        ),
    ]
