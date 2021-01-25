from django.db import models

# Create your models here.
class Config(models.Model):
    contractAddress = models.CharField(max_length=255)
    eventSpecification = models.CharField(max_length=255)
    abi = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    interval = models.IntegerField()

    def __str__(self):
        return self.contractAddress
