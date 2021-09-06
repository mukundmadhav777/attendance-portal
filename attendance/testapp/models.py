from django.db import models

class Portal(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('verified','Verified'))
    desigination_choices=(('student','Student'),('teacher','Teacher'))
    name=models.CharField(max_length=264)
    desigination=models.CharField(max_length=264,choices=desigination_choices,default='teacher')
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
