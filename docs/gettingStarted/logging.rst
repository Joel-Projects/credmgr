Logging in credmgr
==================

It is occasionally useful to observe the HTTP requests that credmgr is issuing. To
do so you have to configure and enable logging.

Add the following to your code to log everything available:

.. code-block:: python

    import logging

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger('credmgr')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

When properly configured, HTTP requests that are issued should produce output
similar to the following:

.. code-block:: text

    Data: None
    Request: GET https://credmgr.jesassn.org/api/v1/bots/1
    Query Parameters: None
    Response: 200 (691 bytes)

For more information on logging, see :py:class:`logging.Logger`.
