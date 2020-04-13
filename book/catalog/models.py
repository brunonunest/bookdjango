from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    review = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']