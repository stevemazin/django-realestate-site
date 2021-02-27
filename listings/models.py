from django.db import models
from datetime import datetime
from realtors.models import Realtor
from PIL import Image

# ImageKit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Listing (models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    locality = models.CharField(max_length=150)
    estate = models.CharField(null=True, blank=True, max_length=150)
    description = models.TextField(blank=True)
    parking_space = models.IntegerField(default=0)
    bedrooms = models.IntegerField()

    buying_price = models.IntegerField(blank=True, null=True)
    rent_price = models.IntegerField(blank=True, null=True)
    
    rental = models.BooleanField(default=False, null=False, blank=False)
    for_sale = models.BooleanField(default=False, null=False, blank=False)

    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    photo_main = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/'
        , processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )
    
    photo_1 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )

    photo_2 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )

    photo_3 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )

    photo_4 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )

    photo_5 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )

    photo_6 = ProcessedImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        processors=[ResizeToFill(1280, 720)],
        format='JPEG',
        options={'quality': 100}
    )
    

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
