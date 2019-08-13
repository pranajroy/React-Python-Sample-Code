# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


__all__ = [
    'Mobile'
]


class Mobile(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    ram = models.CharField(max_length=4)
    battery = models.CharField(max_length=10)
    screen_size = models.FloatField()
    description = models.TextField()
    cover = models.URLField()

    def __str__(self):
        return self.id
