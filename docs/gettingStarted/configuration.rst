.. _configuration:

Configuring Credential Manager Client (credmgr)
===============================================

.. toctree::
   :maxdepth: 2

   configuration/options


Configuration options can be provided to credmgr in one of three ways:

.. toctree::
   :maxdepth: 1

   configuration/credmgrini
   configuration/clientInitialization
   configuration/environmentVariables

Environment variables have the highest priority, followed by keyword arguments
to :class:`.CredentialManager`, and finally settings in ``.credmgr.ini`` files.