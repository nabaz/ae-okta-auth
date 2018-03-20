# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from ae_okta_auth.urls import urlpatterns as ae_okta_auth_urls

urlpatterns = [
    url(r'^', include(ae_okta_auth_urls, namespace='ae_okta_auth')),
]
