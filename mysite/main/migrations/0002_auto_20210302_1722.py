# Generated by Django 3.1.5 on 2021-03-02 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 17, 22, 48, 350738), verbose_name='Date Published'),
        ),
    ]