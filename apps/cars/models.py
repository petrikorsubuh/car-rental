from django.db import models

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()
    cargo_volume = models.IntegerField()
    car_pict = models.ImageField(upload_to='image/cars/')
    price = models.CharField(max_length=12,blank=True,null=True,default='0.0')

    def __str__(self):
        return self.car_name

    class Meta:
        db_table = 'cars'