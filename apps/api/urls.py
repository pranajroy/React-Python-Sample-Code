# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import *

router = routers.DefaultRouter()
router.register('mobiles', MobileViewSet)

# Custom API URLs
urlpatterns = [
    url(r'', include(router.urls)),
]
