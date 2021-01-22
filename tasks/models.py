from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class TechExpert(models.Model):
    expert_id = models.AutoField(primary_key=True)
    expert_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.expert_name
    
class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.status_title

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50)
    job_tech_expert = models.ForeignKey(TechExpert, on_delete=models.CASCADE)
    job_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    job_date = models.TimeField(default=now())
    job_estimated_time = models.IntegerField()
    job_actual_time = models.IntegerField(default=0)
    job_desc = models.CharField(max_length=1000)
    job_notes = models.CharField(max_length=500)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_desc = models.CharField(max_length=1000)
    task_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    task_tech_expert = models.ForeignKey(TechExpert, on_delete=models.CASCADE)
    task_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    task_created_date = models.DateField(default=now())

    def __unicode__(self):
        return self.task_desc