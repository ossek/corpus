# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deathtally', '0003_auto_20141217_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='person',
        ),
        migrations.AddField(
            model_name='character',
            name='actor',
            field=models.ForeignKey(to='deathtally.Actor', default=0),
            preserve_default=False,
        ),
    ]
