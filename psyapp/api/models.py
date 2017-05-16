from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
    subscriber = models.EmailField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.subscriber
