from django.conf.urls import include, url

import users
from .views import subscriber_view, fetch_view

urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^p/', include('processor.urls')),
    url(r'^signup/', subscriber_view),
    url(r'^fetch/$', fetch_view, name='fetch'),
    url(r'^fetch/(?P<key>[0-9a-zA-Z]+)$', fetch_view, name='fetch')
]
