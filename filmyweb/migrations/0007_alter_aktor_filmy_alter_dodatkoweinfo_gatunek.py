# Generated by Django 4.0.6 on 2022-10-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0006_auto_20200327_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='filmy',
            field=models.ManyToManyField(related_name='aktorzy', to='filmyweb.film'),
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Horror'), (4, 'Drama'), (3, 'Sci-fi'), (2, 'Komedia')], default=0),
        ),
    ]
