from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default='', editable=True)  # added
    description = models.TextField(default='', editable=True)  # added

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

