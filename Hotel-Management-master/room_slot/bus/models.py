# Create your models here.
from django.db import models


# Create your models here.

class Buses(models.Model):
    bus_name1 = models.CharField(blank=True, null=True, max_length=30)
    source1 = models.CharField(max_length=30)
    dest1 = models.CharField(blank=True, null=True, max_length=30)
    nos1 = models.DecimalField(decimal_places=0, max_digits=2)
    rem1 = models.DecimalField(decimal_places=0, max_digits=2)
    price1 = models.DecimalField(decimal_places=2, max_digits=6)
    date1 = models.DateField(blank=True, null=True)
    time1 = models.TimeField()
    def __str__(self):
        return self.bus_name1



class people(models.Model):
    user_id = models.CharField(null=True, max_length=40)
    email = models.EmailField(null=True, blank=True, max_length=40)
    name = models.CharField(null=True, blank=True, max_length=30)
    password = models.CharField(null=True, blank=True, max_length=30)
    def __str__(self):
        return self.name



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField(null=True, blank=True, max_length=40)
    name = models.CharField(null=True, blank=True, max_length=30)
    userid =models.IntegerField()
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(blank=True,null=True, max_length=30)
    source = models.CharField(null=True, blank=True, max_length=30)
    dest = models.CharField(max_length=30,null=True)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    def __str__(self):
        return self.name

