from django.db import models
from accounts.models import User
# Create your models here.

class Stockitem(models.Model):
    stock_num = models.CharField(primary_key=True,max_length=15)
    name = models.CharField(max_length=45, blank=True, null=True)
    representative = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    numofstock = models.FloatField(blank=True, null=True)
    probabilitytowin = models.FloatField(blank=True, null=True)
    probabilitytolose = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Autoset(models.Model):
    auto_num = models.AutoField(primary_key=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname', blank=True, null=True)
    s_num = models.ForeignKey(Stockitem, models.DO_NOTHING, db_column='s_num', blank=True, null=True)
    sname = models.CharField(max_length=45, blank=True, null=True)
    set_money = models.FloatField(blank=True, null=True)
    today = models.FloatField(blank=True, null=True)
    input = models.FloatField(blank=True, null=True)
    output = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.sname

class Predictrate(models.Model):
    stock_num = models.OneToOneField(Stockitem, models.DO_NOTHING, db_column='stock_num', primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    numofstock = models.FloatField(blank=True, null=True)
    persent = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Simulation(models.Model):
    simul_num = models.AutoField(primary_key=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname', blank=True, null=True)
    st_num = models.ForeignKey(Stockitem, models.DO_NOTHING, db_column='st_num', blank=True, null=True)
    sname = models.CharField(max_length=45, blank=True, null=True)
    set_money = models.FloatField(blank=True, null=True)
    today = models.FloatField(blank=True, null=True)
    input = models.FloatField(blank=True, null=True)
    output = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.sname
