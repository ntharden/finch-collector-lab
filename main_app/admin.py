from django.contrib import admin
# import your models here
from .models import Friend, Order

# Register your models here
admin.site.register(Friend)
admin.site.register(Order)