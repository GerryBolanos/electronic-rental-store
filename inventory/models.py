# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    custid = models.IntegerField(db_column='custId', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class Electronics(models.Model):
    elecid = models.IntegerField(db_column='elecId', primary_key=True)  # Field name made lowercase.
    electype = models.CharField(db_column='elecType', max_length=11)  # Field name made lowercase.
    model = models.CharField(max_length=128, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    os = models.CharField(max_length=128, blank=True, null=True)
    screen_size = models.IntegerField(blank=True, null=True)
    storage = models.IntegerField(blank=True, null=True)
    gpu = models.CharField(max_length=128, blank=True, null=True)
    refresh_rate = models.IntegerField(blank=True, null=True)
    carrier = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ELECTRONICS'


class Phone(models.Model):
    custid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='custId', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'PHONE'
        unique_together = (('custid', 'phone'),)


class Rents(models.Model):
    custid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='custId', primary_key=True)  # Field name made lowercase.
    elecid = models.ForeignKey(Electronics, models.DO_NOTHING, db_column='elecId')  # Field name made lowercase.
    rental_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RENTS'
        unique_together = (('custid', 'elecid'),)

