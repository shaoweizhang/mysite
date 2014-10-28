from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView
from trybootstrap3 import views

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='bootstrap3_index.html'), name="bootstrap3_home"),
)
