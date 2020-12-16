from django.db import models

# Create your models here.
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