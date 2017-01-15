from django.db import models

class Guests(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date registered')
    email = models.CharField(max_length=200)

    def __str__(self):
            return self.name

