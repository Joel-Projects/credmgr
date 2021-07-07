.. _.credmgr.ini:

.credmgr.ini Files
==================

Credential Manager comes with a ``.credmgr.ini`` file in the package directory, and
looks for user defined ``.credmgr.ini`` files in a few other locations:

1. In the current working directory at the time :class:`.CredentialManager` is
   initialized.
2. In the launching user's home directory.

Format of .credmgr.ini
----------------------

``.credmgr.ini`` uses the `INI file format <https://en.wikipedia.org/wiki/INI_file>`_,
which can contain multiple groups of settings separated into sections. Credmgr refers to
each section as a ``section``. The default section, ``DEFAULT``, is provided in the
package's ``.credmgr.ini`` file. This section defines the default settings for
interaction with CredentialManager. The contents of the package's ``.credmgr.ini`` file
are:

.. literalinclude:: ../../../credmgr/.credmgr.ini
    :linenos:
    :language: ini

.. warning::

    Avoid modifying the package's ``.credmgr.ini`` file. Instead, you can override its
    values in your own ``.credmgr.ini`` file. You can even override settings of the
    ``DEFAULT`` section in user defined ``.credmgr.ini`` files.

Defining Additional Sections
----------------------------

In addition to the ``DEFAULT`` section, additional sections can be configured in user
defined ``.credmgr.ini`` files. All sections inherit settings from the ``DEFAULT``
section and can override whichever settings desired.

Defining additional sections is a convenient way to store :ref:`auth credentials <auth>`
for various bots. For example if you have three separate bots, you might create a
section for each:

.. _customconfigexample:

.. code-block:: ini

    [DEFAULT]
    dateformat = %%m/%%d/%%Y %%I:%%M %%p

    [bot1]
    username = spaz
    password = p@s$w0rd

    [bot2]
    apitoken = C6lkm3HsoKx8fM0Zt85B0JriX6.P9-8_

    [bot3]
    apitoken = kyEnW4h6ia2uA8jbIaRIV68-O-oVE4Yf

Choosing a Custom Config Section
--------------------------------

Section selection is done via the ``configName`` parameter to
:class:`.CredentialManager`. For example, to use the settings defined for ``bot2`` as
shown above, initialize :class:`.CredentialManager` like so:

.. code-block:: python

    from credmgr import CredentialManager

    credentialManager = CredentialManager("bot2")

A section can also be selected via a ``credmgr_configName`` environment variable. This
approach has precedence over the ``configName`` parameter shown above.
