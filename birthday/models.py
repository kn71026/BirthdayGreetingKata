from django.db import models


# Create your models here.
class Birthday(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=50, )
    created = models.DateTimeField(auto_now_add=True)
