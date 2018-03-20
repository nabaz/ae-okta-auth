=====
Usage
=====

To use A+E Django OKTA Auth in a project, add it to your `INSTALLED_APPS`:

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
