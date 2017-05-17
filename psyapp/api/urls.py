from django.conf.urls import include, url

import users
from .views import subscriber_view, fetch_view, fetch_sid_view

urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^p/', include('processor.urls')),
    url(r'^signup/', subscriber_view),
    url(r'^fetch/$', fetch_view, name='fetch'),
    url(r'^fetch/(?P<key>[0-9a-zA-Z]+)$', fetch_view, name='fetch'),
    url(r'^sid/', fetch_sid_view, name='fetch')
]
