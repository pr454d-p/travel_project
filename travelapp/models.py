from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Team_members(models.Model):
    full_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='images')
    job_description = models.TextField()

    def __str__(self):
        return self.full_name
