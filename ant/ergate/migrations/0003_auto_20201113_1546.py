# Generated by Django 3.1.2 on 2020-11-13 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ergate', '0002_auto_20201027_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autoset',
            old_name='flag',
            new_name='count',
        ),
    ]
