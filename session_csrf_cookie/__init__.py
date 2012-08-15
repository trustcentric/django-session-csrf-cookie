# -*- mode: django; coding: utf-8 -*-
#
# Copyright © 2012, TrustCentric
# All rights reserved.
# Redistribution is subject to terms contained in the LICENSE file.

from django.conf import settings
from django.utils.cache import patch_vary_headers


class CsrfCookieMiddleware(object):
    """
    Sets a CSRF cookie when the CSRF token has been used.  This is useful for
    AJAX requests and web service APIs that don't want to parse the HTML to
    extract the token.

    Add this to settings.MIDDLEWARE_CLASSES *after*
    session_csrf.CsrfMiddleware.
    """
    def process_response(self, request, response):
        if (getattr(request, 'csrf_token', False)):
            response.set_cookie(
                settings.CSRF_COOKIE_NAME,
                request.csrf_token,
                max_age=60 * 60 * 24 * 366,
                domain=settings.CSRF_COOKIE_DOMAIN,
                secure=getattr(settings, 'CSRF_COOKIE_SECURE', None),
                httponly=getattr(settings, 'CSRF_COOKIE_HTTPONLY', None),
            )
            patch_vary_headers(response, ['Cookie'])
        return response
