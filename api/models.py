from django.db import models


class CalendarEvent(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100)
    recurring = models.BooleanField()
    user = models.ForeignKey('auth.User')
