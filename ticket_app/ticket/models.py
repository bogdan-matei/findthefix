from django.db import models
# Create your models here.


class Model(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    unique_id = models.CharField(max_length=30, blank=False, unique=True)
    street_address = models.CharField(max_length=100, blank=True)
    email_address = models.CharField(max_length=40, blank=False, unique=True)
    credit_card = models.CharField(max_length=16, blank=False)
    purchase_date = models.DateTimeField(auto_now_add=True)

