from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^polls/', include('polls.urls',namespace="polls")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bootstrap/', include('demo_app.urls', namespace="demo_app")),
    url(r'^bootstrap3/', include('demo.urls', namespace="demo")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', "django.views.static.serve",  {"document_root": settings.MEDIA_ROOT,}),
    )