from django.db import models


class ContactMessage(models.Model):

    name = models.CharField(max_length=80)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} : {self.message}"
