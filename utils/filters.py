# -*- coding: utf-8 -*-
from __future__ import absolute_import

import rest_framework_filters as drf_filters

from apps.mobiles.models import *

__all__ = [
    'MobileFilterSet'
]


class MobileFilterSet(drf_filters.FilterSet):
    id = drf_filters.AllLookupsFilter()

    class Meta:
        model = Mobile
        fields = '__all__'
