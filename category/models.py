from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date_created']

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date_created']  

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-date_created']

class Brand(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-date_created']