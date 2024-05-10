from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=100)
    host_id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name
