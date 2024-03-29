"""raindrop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),
	url(r'^attachments/', include('attachments.urls')),
	url(r'^home/$', 'stories.views.home'),
	url(r'^login/$', RedirectView.as_view(url='/login/facebook')),
	url(r'^logout/$', RedirectView.as_view(url='/disconnect/facebook')),
    url(r'^admin/', include(admin.site.urls)),
)
