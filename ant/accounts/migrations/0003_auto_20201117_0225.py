# Generated by Django 3.1.2 on 2020-11-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201113_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.FloatField(default=0),
        ),
    ]
