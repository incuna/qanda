# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_management.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('email', models.EmailField(max_length=511, unique=True, verbose_name='Email address')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('groups', models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(user_management.models.mixins.NameUserMethodsMixin, models.Model),
        ),
    ]
