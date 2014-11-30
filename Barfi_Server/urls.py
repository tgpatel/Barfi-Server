from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User

from api.models import CalendarEvent, ActionEvent

from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class CalendarEventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email')
 
    class Meta:
    	model = CalendarEvent
	fields = ('url', 'start_date', 'end_date', 'status', 'recurring', 'user')


class ActionEventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email')

    class Meta:
    	model = ActionEvent
	fields = ('url', 'action', 'action_datetime', 'day_of_week', 'latitude', 'longitude', 'user')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CalendarEventViewSet(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer


class ActionEventViewSet(viewsets.ModelViewSet):
    queryset = ActionEvent.objects.all()
    serializer_class = ActionEventSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'calendar/events', CalendarEventViewSet)
router.register(r'action/events', ActionEventViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Barfi_Server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
