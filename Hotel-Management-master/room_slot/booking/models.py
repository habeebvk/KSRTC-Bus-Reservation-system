from django.db import models
from login.models import Customer,RoomManager
from datetime import date
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    def __str__(self):
        return self.name
class Rooms(models.Model):
    manager=models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)
    no_of_days_advance=models.IntegerField()
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    def __str__(self):
        return "Room No: "+str(self.id)
'''
class RoomImage(models.Model):
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
'''
class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return "Booking ID: "+str(self.id)
    @property
    def is_past_due(self):
        return date.today()>self.end_day


from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import random

def random_price():
    return random.randint(800,2000)

# CATEGORY_CHOICES=(
#     ('MN','Munnar'),
#     ('NL','Nelliyampathy'),
#     ('OT','Ooty'),
#     ('CG','Coorg'),
#     ('MS','Mysore'),
#     ('WY','Wayanad'),
#     ('KD','Kodaikanal'),
#     ('FK','Fort Kochi'),
# )

class PersonalDetail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    Address = models.CharField(max_length=700)
    
class GuestDetail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    Address = models.CharField(max_length=700)


class Destination(models.Model):
    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    desc = models.TextField()
    price = models.IntegerField() 
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True, blank=True)   


class Dest(models.Model):
    name =  models.CharField(max_length=100) 
    desc_big = models.TextField() 
    image = models.ImageField(upload_to='media')
    city = models.CharField(null=True,max_length=100)
    price = models.IntegerField(blank=True, default=1)
    
def _str_(self):
    return self.name

# class Bus(models.Model):
    
#     bus_no = models.CharField(max_length=30)
#     source = models.CharField(max_length=30)
#     desti = models.CharField(max_length=30)
#     image = models.ImageField(null=True, upload_to='media')
#     price = models.DecimalField(decimal_places=2, max_digits=6)
#     date = models.DateField()
#     time = models.TimeField()
#     ticket_no = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class casamontana(models.Model):

#     ckeck_in = models.DateField(max_length=)     
# 
# class hotel(models.Model):
#     city = models.CharField(default=None, max_length=64)
#     name = models.CharField(max_length=100)
#     number_of_rooms = models.DecimalField(decimal_places=0, max_digits=2)
#     type = models.CharField(max_length=30)
#     imgurls = models.CharField(default=None, max_length=64)
#     rating = models.CharField(default=0, max_length=64)   
#     price = models.FloatField(default=random_price)
#     def __str__(self):
#         return self.city

# class Room(models.Model):
#     ROOM_CATEGORIES = (
#         ('YAC', 'AC'),
#         ('NAC', 'NON-AC'),
#         ('DEL', 'DELURE'),
#         ('KIN', 'KING'),
#         ('QUE', 'QUEEN'),

#     )
#     number=models.IntegerField()
#     category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
#     beds = models.IntegerField()
#     capacity = models.IntegerField()   

#     def __str__(self):
#         return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'   

# class Booking(models.Model):
#     hotel = models.ForeignKey(hotel, related_name="booking", on_delete=models.CASCADE)
#     tracking_id = models.CharField(default='000', max_length=64)

#     first_name = models.CharField(default=None, max_length=64)
#     last_name = models.CharField(default=None, max_length=64)
#     email = models.CharField(default=None, max_length=64)
#     phone = models.CharField(default=None, max_length=64)

#     room = models.IntegerField(default=1)
#     adult = models.IntegerField(default=1)
#     child = models.IntegerField(default=0)

#     checkin_date = models.CharField(default=None , max_length=64)
#     checkout_date = models.CharField(default=None, max_length=64)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     price = models.CharField(max_length=64, default=None, null=False)

#     user = models.ForeignKey(User, related_name="booking", on_delete=models.SET_NULL, default=None, null=True, blank=True)


#     def __str__(self):
#         return self.tracking_id    

# class Transaction(models.Model):
#     made_by = models.ForeignKey(User, related_name='transactions',
#                                 on_delete=models.CASCADE)
#     made_on = models.DateTimeField(auto_now_add=True)
#     amount = models.IntegerField()
#     order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
#     checksum = models.CharField(max_length=100, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.made_on and self.id:
#             self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
#         return super().save(*args, **kwargs)        


class Hotels(models.Model):
    ROOM_CATEGORIES = (
         ('YAC', 'AC'),
         ('NAC', 'NON-AC'),
         ('DEL', 'DELURE'),
         ('KIN', 'KING'),
         ('QUE', 'QUEEN'),

     )
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    room_no = models.IntegerField()
    type = models.CharField(max_length=3, choices=ROOM_CATEGORIES)


class Feedback(models.Model):
    name=models.CharField(max_length=40, null=True)
    feedback = models.CharField(max_length=400)  


class Notifi(models.Model):
    notification = models.CharField(max_length=500)   

class certificate(models.Model):
    ROOM_CATEGORIES = (
         ('YAC', 'AC'),
         ('NAC', 'NON-AC'),
         ('DEL', 'DELURE'),
         ('KIN', 'KING'),
         ('QUE', 'QUEEN'),

     )
    name = models.CharField(max_length=60)
    desc=models.CharField(max_length=300)
    price=models.IntegerField()
    type = models.CharField(max_length=3, choices=ROOM_CATEGORIES)