from django.db import models


class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=122)
    