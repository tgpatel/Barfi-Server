from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CalendarEvent
from datetime import datetime, timedelta

import pytz

@api_view(['GET'])
def take_action(request):
    if request.method == 'GET':
    	username = request.GET.get('username')
	time = datetime.strptime(request.GET.get('time'), '%Y-%m-%dT%H:%M:%SZ')
	time = pytz.utc.localize(time)

	calendar_event = CalendarEvent.objects.filter(user__username=username, start_date__gte=time+timedelta(days=0, hours=6, minutes=59), start_date__lte=time+timedelta(days=0, hours=7, minutes=1))

	if calendar_event:
	    response_data = { 'takeAction': True, 'action': 0 }
	else:
	    calendar_event = CalendarEvent.objects.filter(user__username=username, end_date__gte=time+timedelta(days=0, hours=6, minutes=59), end_date__lte=time+timedelta(days=0, hours=7, minutes=1))

	    if calendar_event:
	        response_data = { 'takeAction': True, 'action': 2 }
	    else:
	        response_data = { 'takeAction': False, 'action': -1 }

	return Response(response_data)

