# Generated by Django 3.0.8 on 2021-12-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
