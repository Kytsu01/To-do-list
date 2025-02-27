from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.task_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    task_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=0)
    task_description = models.CharField(max_length=1000)
    end_date = models.DateField()
