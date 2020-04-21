from django.db import models
from django.urls import reverse

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length=35, verbose_name='name')
    last_name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('resident-detail', args=[str(self.id)])

    class Meta:
        ordering = ['last_name']

class Intervention(models.Model):
    intervention = models.CharField(max_length=175)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.intervention}'

    def get_absolute_url(self):
        return reverse('intervention-detail', args=[str(self.id)])

    class Meta:
        ordering = ['intervention']
