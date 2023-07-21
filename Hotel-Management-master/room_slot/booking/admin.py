from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PersonalDetail
from .models import GuestDetail
from . models import Destination, Dest,Hotels, Feedback, Notifi,certificate
admin.site.register(PersonalDetail)
admin.site.register(GuestDetail)
admin.site.register(Destination)
admin.site.register(Dest)
admin.site.register(Hotels)
# admin.site.register(Feedback)

@admin.register(Feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display=['feedback']
    readonly_fields = ['feedback']
    def has_add_permission(self, request):
      return False

    def has_delete_permission(self, request, obj=None):
      return False  

admin.site.register(Notifi)
admin.site.register(certificate)        