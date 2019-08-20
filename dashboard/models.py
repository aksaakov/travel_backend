from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe


# Create your models here.
class Tour(models.Model):
    location_title = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    tour_date_and_time = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/', default='images/placeholderImage.png')

    def __str__(self):
        return self.location_title

    class Meta:
        verbose_name_plural = "Tours"


class TourPackage(models.Model):
    package_title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.package_title

    class Meta:
        verbose_name_plural = "TourPackages"
