from django.db import models


class Book(models.Model):
    # full_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # pdf = models.FileField(upload_to='books/pdfs/')
    # cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    full_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    chicago_collision_data = models.FileField(upload_to='json/chicago_collision_data/', null=True, blank=True)
    flight_call = models.FileField(upload_to='json/flight_call/', null=True, blank=True)
    light_levels = models.FileField(upload_to='json/light_levels/', null=True, blank=True)

    def __str__(self):
        return self.full_name