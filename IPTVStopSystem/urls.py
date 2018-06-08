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
from view import process_verify
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^$', views.redirect_to_index),
    url(r'^index$', views.index),

    # program
    url(r'^program/(?P<program_name>[\s\S]*)/(?P<program_type>[\s\S]*)/(?P<platform>[\s\S]*)/(?P<status>[\s\S]*)/(?P<program_ip_type>[\s\S]*)$',
        program.show_program),
    url(r'^program_logs/(?P<start_time>[\s\S]*)/(?P<end_time>[\s\S]*)$', program.show_log),
    url(r'^program_change$', program.program_change),
    url(r'^approximate$', program.approximate),

    # CDN
    url(r'^cdn_logs$', CDN.show_log),
    url(r'^cdn/(?P<platform>[\s\S]*)/(?P<city>[\s\S]*)/(?P<pop_node>[\s\S]*)$', CDN.show_cdn),
    url(r'^cdn_change$', CDN.cdn_change),

    # EPG
    url(r'^epg$', views.index),
    url(r'^epg_one_key$', EPG.epg_one_key),

    # process verify
    url(r'^process_verify$', process_verify.show_process_verify),
    url(r'^set_code$', process_verify.set_auth_code)

]
