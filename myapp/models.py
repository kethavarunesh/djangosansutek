from django.db import models

class Contactform(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField( max_length=50)
    message = models.TextField()

class ResumeSubmission(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)