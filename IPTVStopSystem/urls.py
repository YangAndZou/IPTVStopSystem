"""IPTVStopSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import views
from view import program
from view import CDN
from view import EPG
from django.conf.urls import url

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^$', views.redirect_to_index),
    url(r'^index$', views.index),
    url(r'^index/(?P<program_name>[\s\S]*)/(?P<program_ip>[\s\S]*)/(?P<status>[\s\S]*)$',
        views.index),

    # program
    url(r'^program_logs$', program.show_log),
    url(r'^program_change$', program.program_change),

    # CDN
    url(r'^cdn_logs$', CDN.show_log),
    url(r'^cdn/(?P<system_attr>[\s\S]*)/(?P<system_val>[\s\S]*)/(?P<router_group>[\s\S]*)$', CDN.cdn),
    # url(r'^cdn_change', CDN.cdn_change),

    # EPG
    url(r'^epg_logs$', EPG.show_log),
    url(r'^epg/(?P<system_attr>[\s\S]*)/(?P<system_val>[\s\S]*)/(?P<router_group>[\s\S]*)$', EPG.epg),
    # url(r'^epg_change', EPG.epg_change),
]
