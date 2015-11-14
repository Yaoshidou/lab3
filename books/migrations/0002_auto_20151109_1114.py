# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['ISBN']},
        ),
        migrations.AlterField(
            model_name='author',
            name='Name',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.RemoveField(
            model_name='book',
            name='AuthorID',
        ),
        migrations.AddField(
            model_name='book',
            name='AuthorID',
            field=models.ManyToManyField(related_name='books', to='books.Author'),
        ),
    ]
