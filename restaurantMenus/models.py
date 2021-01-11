from django.db import models


class restaurantMenus(models.Model):
    brand = models.CharField(max_length=50, blank=False, default='')
    menuItem = models.CharField(max_length=100, blank=False, default='')
    ingredients = models.CharField(max_length=2000, blank=False, default='')
