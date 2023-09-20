from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    country = models.CharField(max_length=255)
    information = models.TextField()

    def __str__(self):
        return self.name
