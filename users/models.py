from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class Inquiry (models.Model):
    listing = models.CharField(max_length=100)
    listing_id = models.IntegerField()

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str(self):
        return self.name
    
