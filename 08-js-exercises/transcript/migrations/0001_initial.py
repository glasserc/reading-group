# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('graduation', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='transcript.Student')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='transcript',
            field=models.ForeignKey(to='transcript.Transcript'),
        ),
        migrations.AddField(
            model_name='course',
            name='period',
            field=models.ForeignKey(to='transcript.Period'),
        ),
    ]
