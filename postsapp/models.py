from django.db import models


class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60,)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    address_street = models.CharField(max_length=60)
    address_suite = models.CharField(max_length=60)
    address_city = models.CharField(max_length=60)
    address_zipcode = models.CharField(max_length=20)
    address_geo_lat = models.FloatField()
    address_geo_lng = models.FloatField()
    phone = models.CharField(max_length=30)
    website = models.URLField()
    company_name = models.CharField(max_length=60)
    company_catchphrase = models.CharField(max_length=60)
    company_bs = models.CharField(max_length=60)


class Post(models.Model):
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    body = models.TextField(blank=True)