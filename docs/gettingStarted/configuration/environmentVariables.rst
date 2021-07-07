.. _environmentvariables:

Credmgr Environment Variables
=============================

The highest priority configuration options can be passed to a program via environment
variables prefixed with ``credmgr_``.

For example, you can invoke your script as follows:

.. code-block:: shell

    credmgr_apitoken=C6lkm3HsoKx8fM0Zt85B0JriX6.P9-8_ python bot.py

The ``apitoken`` provided via environment variables will override any such values passed
directly when initializing an instance of :class:`.CredentialManager`, as well as any
such values contained in a ``.credmgr.ini`` file.

All :ref:`configurationOptions` can be provided in this manner, except for custom
options.
