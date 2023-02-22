from django.contrib import admin
from .models import Topping,Order,Pizza

# Register your models here.
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Pizza)
