from django.db import models


#Model about the book and its content
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    review = models.CharField(max_length=250)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



