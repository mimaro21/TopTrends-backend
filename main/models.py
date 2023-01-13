from django.db import models

# Create your models here.

class Country(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    acronym = models.CharField(max_length=2)
    woeid = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']