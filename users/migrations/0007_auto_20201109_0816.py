# Generated by Django 3.1.2 on 2020-11-09 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201108_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 11, 9), help_text='ex: 2020-01-20', null=True),
        ),
    ]
