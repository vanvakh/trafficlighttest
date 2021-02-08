from django.db import models


class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    website = models.URLField(blank=True)
    address_street = models.CharField(max_length=60, blank=True)
    address_suite = models.CharField(max_length=60, blank=True)
    address_city = models.CharField(max_length=60, blank=True)
    address_zipcode = models.CharField(max_length=20, blank=True)
    address_geo_lat = models.FloatField(blank=True)
    address_geo_lng = models.FloatField(blank=True)
    company_name = models.CharField(max_length=60, blank=True)
    company_catchphrase = models.CharField(max_length=60, blank=True)
    company_bs = models.CharField(max_length=60, blank=True)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True)
    body = models.TextField(blank=True)
