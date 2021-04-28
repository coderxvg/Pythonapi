from django.db import models

# Create your models here.
class CcrFormnew(models.Model):
    id = models.AutoField(primary_key=True)
    Requestor = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)