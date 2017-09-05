"""app1 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from django_cas_ng import views as cas_views

@login_required
def index(request):
    return HttpResponse(str(request.session['attributes']))

urlpatterns = [
    url(r'^$', index),
    url(r'^accounts/login/$', cas_views.login, name='cas_ng_login'),
    url(r'^accounts/logout/$', cas_views.logout, name='cas_ng_logout'),
    url(r'^accounts/callback/$', cas_views.callback, name='cas_ng_proxy_callback'),
]
