from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()


class Technology(models.Model):
    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)


class User(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    profession = models.CharField(max_length=40)


class Order(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

