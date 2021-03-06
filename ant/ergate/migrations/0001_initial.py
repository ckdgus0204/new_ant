# Generated by Django 3.1.2 on 2020-10-11 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stockitem',
            fields=[
                ('stock_num', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('representative', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('numofstock', models.FloatField(blank=True, null=True)),
                ('probabilitytowin', models.FloatField(blank=True, null=True)),
                ('probabilitytolose', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Predictrate',
            fields=[
                ('stock_num', models.OneToOneField(db_column='stock_num', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ergate.stockitem')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('numofstock', models.FloatField(blank=True, null=True)),
                ('persent', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('simul_num', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, max_length=45, null=True)),
                ('set_money', models.FloatField(blank=True, null=True)),
                ('today', models.FloatField(blank=True, null=True)),
                ('input', models.FloatField(blank=True, null=True)),
                ('output', models.FloatField(blank=True, null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('start_date', models.CharField(blank=True, max_length=45, null=True)),
                ('end_date', models.CharField(blank=True, max_length=45, null=True)),
                ('st_num', models.ForeignKey(blank=True, db_column='st_num', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ergate.stockitem')),
                ('uname', models.ForeignKey(blank=True, db_column='uname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Autoset',
            fields=[
                ('auto_num', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, max_length=45, null=True)),
                ('set_money', models.FloatField(blank=True, null=True)),
                ('today', models.FloatField(blank=True, null=True)),
                ('input', models.FloatField(blank=True, null=True)),
                ('output', models.FloatField(blank=True, null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('start_date', models.CharField(blank=True, max_length=45, null=True)),
                ('end_date', models.CharField(blank=True, max_length=45, null=True)),
                ('s_num', models.ForeignKey(blank=True, db_column='s_num', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ergate.stockitem')),
                ('uname', models.ForeignKey(blank=True, db_column='uname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
