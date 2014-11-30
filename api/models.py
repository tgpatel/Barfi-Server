from django.db import models

from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


class CalendarEvent(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100)
    recurring = models.BooleanField()
    user = models.ForeignKey('auth.User')


class ActionEvent(models.Model):
    ACTION_CHOICES = Choices(
    	    	(0, _('Silent')),
	    	(1, _('Vibrate')),
	    	(2, _('Normal')),
	    )
    WEEK_DAY_CHOICES = Choices(
    	   	(1, _('Sunday')),
		(2, _('Monday')),
		(3, _('Tuesday')),
		(4, _('Wednesday')),
		(5, _('Thursday')),
		(6, _('Friday')),
		(7, _('Saturday')),
	   )
    action = models.IntegerField(default=0, choices=ACTION_CHOICES)
    action_datetime = models.DateTimeField()
    day_of_week = models.IntegerField(choices=WEEK_DAY_CHOICES)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('auth.User')
