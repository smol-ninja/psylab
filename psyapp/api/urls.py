from django.conf.urls import include, url

import users
from .views import subscriber_view

urlpatterns = [
    url(r'^users/', include('users.urls')),
    url(r'^p/', include('processor.urls')),
    url(r'^signup/', subscriber_view)
]
