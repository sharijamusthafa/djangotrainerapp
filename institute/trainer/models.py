from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TrainerProfile(models.Model):
    qualification=models.CharField(max_length=120)
    phonenumber=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    user=models.CharField(max_length=120)
    photo=models.ImageField(upload_to="images",default="hii")


    def __str__(self):
        return self.user

class SkillModel(models.Model):
    skill = models.CharField(max_length=120)

    def __str__(self):
         return self.skill


class InstituteDetails(models.Model):
    job = models.CharField(max_length=120)
    skills = models.ForeignKey(SkillModel,on_delete=models.CASCADE)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.job

class filterskill(models.Model):
    filter=models.ForeignKey(SkillModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.filter