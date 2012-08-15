# -*- mode: django; coding: utf-8 -*-
#
# Copyright © 2012, TrustCentric
# All rights reserved.
# Redistribution is subject to terms contained in the LICENSE file.

from django import http
from django.conf import settings
from django.conf.urls.defaults import patterns
from django.contrib.auth.models import User
from django.test import TestCase


urlpatterns = patterns(
    '',
    ('^$', lambda r: http.HttpResponse()),
)


class CsrfCookieTests(TestCase):
    def test_csrf_cookie(self):
        # Test that a csrftoken cookie is set on normal requests.
        User.objects.create_user(username='tony', password='grrreat',
                                 email='tony@example.com')
        self.client.login(username='tony', password='grrreat')

        self.client.get('/')
        self.assertTrue(self.client.cookies.get('csrftoken', None))
