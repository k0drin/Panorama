from django.db import models
from django.urls import reverse


class Panorama(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='panoramas/')

    def get_absolute_url(self):
        return reverse('panorama_detail', args=[self.pk])
    
    def __str__(self):
        return self.title


class Marker(models.Model):
    panorama = models.ForeignKey(Panorama, related_name='markers', on_delete=models.CASCADE)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    tooltip_text = models.CharField(max_length=200)
    linked_panorama = models.ForeignKey(Panorama, related_name='linked_markers', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Marker at ({self.x_coordinate}, {self.y_coordinate})"


class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.name} ({self.email})"