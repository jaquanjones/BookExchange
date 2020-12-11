from django.contrib import admin

from .models import MainMenu, Book, Order, OrderItem, Review

# from django.contrib.admin import site

# Register your models here.
admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
