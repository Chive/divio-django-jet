# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
]

if settings['DIVIO_DJANGO_JET_ENABLE_DASHBOARD']:
    urlpatterns.append(
        url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    )
