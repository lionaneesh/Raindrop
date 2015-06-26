# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_type', models.CharField(default=b'Text', max_length=8, choices=[(b'Video', b'Video'), (b'Picture', b'Picture'), (b'Text', b'Text')])),
                ('attachment', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='snippets',
            name='story',
            field=models.ForeignKey(to='stories.Story'),
        ),
    ]
