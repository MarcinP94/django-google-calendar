from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("Title", max_length=500, null=True)
    start = models.DateTimeField("Start date", default=datetime.now, null=True)  # start event date
    end = models.DateTimeField("Start date", default=datetime.now, null=True)  # end event date
    event_id = models.CharField("Event id", max_length=1024, null=True, default='N/A')  # event id from google calendar

    def __str__(self):
        return self.title



