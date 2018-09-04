=============================
A+E Django OKTA Auth
=============================

.. image:: https://badge.fury.io/py/ae_okta_auth.svg
    :target: https://badge.fury.io/py/ae_okta_auth

.. image:: https://travis-ci.org/nabaz/ae_okta_auth.svg?branch=master
    :target: https://travis-ci.org/nabaz/ae_okta_auth

.. image:: https://codecov.io/gh/nabaz/ae_okta_auth/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/nabaz/ae_okta_auth

Django Package to integrate OKTA SAML2 with Django

Documentation
-------------

The full documentation is at https://ae_okta_auth.readthedocs.io.

Quickstart
----------

Install A+E Django OKTA Auth::

    pip install -e git+git://github.com/nabaz/ae-okta-auth.git#egg=django-ae-okta-aCollecting django-ae-okta-auth from git+git://github.com/nabaz/ae-okta-auth.git#egg=django-ae-okta-auth

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ae_okta_auth.apps.AeOktaAuthConfig',
        ...
    )

Add A+E Django OKTA Auth's URL patterns:

.. code-block:: python

    from ae_okta_auth import urls as ae_okta_auth_urls


    urlpatterns = [
        ...
        url(r'^', include(ae_okta_auth_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
