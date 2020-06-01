from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    short_description = models.CharField(max_length=175)
    long_description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.short_description}'

    def get_absolute_url(self):
        return reverse('intervention-detail', args=[str(self.id)])

    class Meta:
        ordering = ['short_description']

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, null=True)
    intervention = models.ForeignKey('Intervention', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.resident}: {self.intervention} - {self.date} {self.time}'
