# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
   openapi.Info(
      title="Mobile API",
      default_version='v1',
      description="APIs for sample mobile application",
      terms_of_service="",
      contact=openapi.Contact(email="contact@mobile.api"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(AllowAny,),
)


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/', include('apps.api.urls', namespace='api')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

admin.site.site_title = 'mobileapi Administration'
admin.site.index_title = 'mobileapi Administration'
admin.site.site_header = 'mobileapi Administration'
