from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    created_by = models.ForeignKey(User, related_name='created_by')
    modified_by = models.ForeignKey(User, related_name='modified_by')
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
