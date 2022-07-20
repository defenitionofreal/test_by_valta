from django.db import models


class Filial(models.Model):
    name = models.CharField(max_length=255)
    region = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} | {self.region}"
