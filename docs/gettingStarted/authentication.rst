.. _auth:

Authenticating with CredentialManager
=====================================

CredentialManager supports two types of authentication:

- :ref:`API Token <api_token>`
- :ref:`Username/Password Combo <username_password>`

.. _api_token:

API Token
---------

To create an API Token, you must first `create one here
<https://credmgr.jesassn.org/api_tokens/>`_

.. code-block:: python

    from credmgr import CredentialManager

    credentialManager = CredentialManager(username="spaz", password="p@s$w0rd")

.. note::

    See here for more ways to pass an API Token to ``credmgr``

.. _username_password:

Username/Password
-----------------

This should be obvious, but this method is utilized by passing username and password to
``credmgr``'s initialization call:

.. code-block:: python

    from credmgr import CredentialManager

    credentialManager = CredentialManager(username="spaz", password="p@s$w0rd")

.. warning::

    This method is not recommended and should not be used in prod environments!

To verify that you are authenticated as the correct user run:

.. code-block:: python

    print(credentialManager.currentUser().username)

The output should be your..well uh..username

.. note::

    If the following exception is raised, double-check your credentials, and ensure that
    that the API Token or username/password you are using are correct and your account
    is not disabled

    .. code-block::

        credmgr.exceptions.Unauthorized:
        401: https://credmgr.jesassn.org/api/v1/users/me
        Unauthorized
