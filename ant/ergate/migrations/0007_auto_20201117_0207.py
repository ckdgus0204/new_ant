# Generated by Django 3.1.2 on 2020-11-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ergate', '0006_auto_20201117_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='stock_num',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
