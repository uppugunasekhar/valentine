from django.conf.urls import patterns, include, url
from django.contrib import admin
from valentine import views
from django.http import HttpResponse
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',views.index, name ='index'),
	url(r'^middle/$',views.middle,name='middle'),	
	url(r'^register/$',views.register, name ='register'),
	url(r'^logout/$',views.logout, name ='logout'),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	#(r'^robots\.txt$',lambda r: HttpResponse("User-agent: *\nDisallow:", mimetype="text/plain")),
)

