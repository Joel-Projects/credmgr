Running Multiple Instances of credmgr
=====================================

Credmgr as of right now does not have a rate limit. But it will if it gets abused
or people write shitty code and spam the API.

Multiple Programs
-----------------

The recommended way to run multiple instances of credmgr is to simply write
separate independent Python programs. With this approach one program can
monitor a comment stream and reply as needed, and another program can monitor a
submission stream, for example.

If these programs need to share data consider using a third-party system such
as a database or queuing system.

Multiple Threads
----------------

.. warning:: credmgr is ***NOT*** thread safe.

Instances of :class:`.CredentialManager` are not thread-safe because each
instance depends on an instance of ``requests.Session``, which is not thread-safe [`ref
<https://github.com/kennethreitz/requests/issues/2766>`_]. Use multiple processes instead.