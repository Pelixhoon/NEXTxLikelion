from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Subject(models.Model):
    major = models.ForeignKey(
        "Major", on_delete=models.CASCADE, related_name='subject')
    subject_name = models.CharField(max_length=255)
    prof_name = models.CharField(max_length=255)
    memo = models.CharField(max_length=255)

    def __str__(self):
        return str(self.subject_name)