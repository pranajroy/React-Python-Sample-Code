# -*- coding: utf-8 -*-
from __future__ import absolute_import

from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import DjangoFilterBackend

from apps.mobiles.models import Mobile
from utils import MobileFilterSet
from .serializers import MobileSerializer

__all__ = [
    'MobileViewSet'
]


class MobileViewSet(ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    filter_class = MobileFilterSet
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
