# -*- coding: utf-8 -*-
from __future__ import absolute_import

from rest_framework import serializers

from apps.mobiles.models import Mobile

__all__ = [
    'MobileSerializer'
]


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
