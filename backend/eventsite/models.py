from django.db import models

# Create your models here.


class Event(models.Model):
    _id = models.CharField(max_length=10)  # utilize id generator later
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    # implement true address validation
    location = models.CharField(max_length=100)
    _type = models.CharField(max_length=100)  # make enum later
    startDate = models.DateField()
    endDate = models.DateField()
    registerationReq = models.BooleanField(default=False)
    frequency = models.CharField(max_length=30)

    # what the admin will see

    def __str__(self):
        return self.title
