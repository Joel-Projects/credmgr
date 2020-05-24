.. _configurationOptions:

Configuration Options
=====================

Credmgr's configuration options are broken down into the following categories:

* :ref:`basicSettings`
* :ref:`authSettings`
* :ref:`serverOptions`

All of these options can be provided in any of the ways mentioned in
:ref:`configuration`.

.. _basicSettings:

Basic Configuration Options
---------------------------

:dateformat: This is used to specify the date format that is printed for
    creation and modification date/time for objects. (default: ``%%m/%%d/%%Y %%I:%%M:%%S %%p %%Z``).

.. note:: You must escape ``%`` symbols in the format string. For example:

    .. code::

        dateformat = %%m/%%d/%%Y %%I:%%M:%%S


.. _authSettings:

Authentication Configuration Options
------------------------------------

:apitoken: (Strongly recommended) The API Token that will be used for interacting with CredentialManager

.. _serverOptions:

CredentialManager Server Configuration Options
----------------------------------------------

Credmgr can be configured to work with instances of CredentialManager which are not at
`credmgr.jesassn.org <https://credmgr.jesassn.org>`_. The following options may need to be
updated in order to interact a local dev server for instance.

:server: The server credmgr will use when interacting with CredentialManager (default `https://credmgr.jesassn.org`)

:endpoint: The endpoint credmgr will use when interacting with CredentialManager (default `/api/v1`)

.. _customOptions:

Custom Configuration Options
----------------------------

Your application can utilize credmgr's configuration system in order to provide
its own custom settings.

For example, you might want to set a global ``botName: botName`` option to your
application's ``.credmgr.ini`` file. To access the value of this custom option
from an instance of :py:class:`.CredentialManager` you can execute:

.. code-block:: python

    credmgr.config.custom['botName']

.. note:: Custom CredentialManager configuration environment variables are not
          supported. You can directly access environment variables via
          ``os.getenv``.
