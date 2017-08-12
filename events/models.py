from django.db import models

# Create your models here.
class Event(models.Model):
    year = models.IntegerField()
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return str(self.year)

