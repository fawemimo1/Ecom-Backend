from django.db import models

# Create your models here.

class Newsletter(models.Model):
    first_name =  models.CharField(max_length=100, null = True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email