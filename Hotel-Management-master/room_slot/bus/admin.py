from django.contrib import admin
from .models import Buses, Book,people

# Register your models here.

admin.site.register(Buses)
admin.site.register(people)
admin.site.register(Book)


