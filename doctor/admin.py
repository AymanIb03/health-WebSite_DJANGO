from django.contrib import admin
from .models import Appointment,Service,Hospital
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(Hospital)


