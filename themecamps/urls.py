import themecampsapp
from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.contrib import admin
admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'themecamps.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^api/', include('themecampsapp.api_urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )
