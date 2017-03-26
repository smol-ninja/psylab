"""psyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings

from . import psyadmin
from users import views

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
]

if settings.DEBUG:
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

urlpatterns = [
    url(r'^admin/', psyadmin.urls),
    url(r'^o/', include(oauth2_endpoint_views, namespace='oauth2_provider')),
    url(r'login/$', views.TokenView.as_view(), name="login"),
    url(r'logout/$', views.RevokeTokenView.as_view(), name="logout"),
    url(r'register/$', views.register, name='register'),
    url(r'^api/', include('api.urls')),
]
