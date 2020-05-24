.. _credmgrInitialization:

Keyword Arguments to :class:`.CredentialManager`
================================================

Most of credmgr's documentation will show configuring credmgr through the use
of keyword arguments when initializing instances of :class:`.CredentialManager`. All of
the :ref:`configurationOptions` can be specified using a keyword argument of the same name.

For example, if we wanted to explicitly pass the information for ``bot3``
defined in :ref:`the .credmgr.ini custom config example <customConfigExample>`
without using the ``bot2`` site, we would initialize :class:`.CredentialManager` as:

.. code-block:: python

    from credmgr import CredentialManager

    credentialManager = CredentialManager(apiToken='2SV_6k8NpBLOH~YVJR8GjKih8rm1YBY-')
