from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import datetime

# Create your models here.
class tank_master(models.Model):
    date=models.DateField(default=datetime.utcnow)
    petrolbefore=models.FloatField(null=True,blank=True)
    dieselbefore=models.FloatField(null=True,blank=True)
    petrolafter = models.FloatField(null=True,blank=True)
    dieselafter = models.FloatField(null=True,blank=True)
    lostpetrol = models.FloatField(null=True,blank=True)
    lostdiesel = models.FloatField(null=True,blank=True)
    lostpetrolprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    lostdieselprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    oilopeninlit = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    oilcloseinlit = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])

    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"

    def get_absolute_url(self):
        return reverse('Tank-view')