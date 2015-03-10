from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myvalentine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('valentine.urls', namespace="valentine")),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls',namespace='social')),
    url('', include('django.contrib.auth.urls',namespace='auth')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    (r'^robots.txt$',lambda r: HttpResponse("User-agent: *\nDisallow:", mimetype="text/plain")),
     
)
