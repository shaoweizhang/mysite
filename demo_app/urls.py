from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView
from demo_app import views

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="demo_contact"),
    url(r'^form$', views.demo_form, name="demo_form"),
    url(r'^form_template$', views.demo_form_with_template, name="demo_form_with_template"),
    url(r'^form_inline$', views.demo_form_inline, name="demo_form_inline"),
    url(r'^formset$', views.demo_formset, {}, name="demo_formset"),
    url(r'^tabs$', views.demo_tabs, {}, name="demo_tabs"),
    url(r'^pagination$', views.demo_pagination, {}, name="demo_pagination"),
    url(r'^widgets$', views.demo_widgets, {}, name="demo_widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="demo_buttons"),
    url(r'^example$', TemplateView.as_view(template_name='base.html.example'), name="demo_example"),
    #url(r'^example$', views.example, name="example"),
)

