from django.contrib import admin
# from django.contrib.admin import site

from .models import MainMenu, Book, Order

# Register your models here.
admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Order)
