What is this?
-------------

``django-session-csrf-cookie`` is Django middleware that provides a
CSRF token cookie when using `django-session-csrf
<https://github.com/mozilla/django-session-csrf/>`_.  By design,
django-session-csrf does not require a CSRF token cookie, but such a
cookie is useful for AJAX requests and other web APIs, since it allows
the client to get the CSRF token without parsing HTML.  (Note that the
cookie is not used by the server for any purpose, so the security hole
django-session-csrf was designed to fix is still fixed.)  



Installation
------------

From PyPI::

    pip install django-session-csrf-cookie

From github::

    git clone git://github.com/trustcentric/django-session-csrf-cookie.git

Add ``session_csrf_cookie.CsrfCookieMiddleware`` to your ``MIDDLEWARE_CLASSES``
below ``session_csrf.CsrfMiddleware``::

    MIDDLEWARE_CLASSES = (
        ...
        'session_csrf.CsrfMiddleware',
        'session_csrf_cookie.CsrfCookieMiddleware',
        ...
    )

Add ``session_csrf_cookie`` to ``INSTALLED_APPS``.


Settings
--------

``session-csrf-cookie-middleware`` can be controlled using the
following settings:

    ``CSRF_COOKIE_NAME``
        The name used for the CSRF token cookie.

        Default: ``csrftoken``

    ``CSRF_COOKIE_DOMAIN``
        The domain to be used when setting the CSRF cookie.

        Default: None

    ``CSRF_COOKIE_SECURE``
        Whether to use a secure cookie for the CSRF cookie.

        Default: False

    ``CSRF_COOKIE_HTTPONLY``
        Whether to set the HTTPOnly flag on the CSRF cookie.

        Default: False
