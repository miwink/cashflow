"""cashflow URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from cashflow import settings
from .authviews import login, login_with_token, logout

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^login/(?P<token>.+)/$', login_with_token, name='login_with_token'),
    url(r'^logout/', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("expenses.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
