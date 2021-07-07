Quick Start
===========

In this section, you'll see some examples on how to use credmgr, (CredentialManager
Client).

Prerequisites
-------------

:CredentialManager Account: You need an account on `CredentialManager
    <https://credmgr.jesassn.org>`_. If you don't have one, contact JES.
:API Token: To authenticate with and access CredentialManager you need to create an API
    token.

.. seealso::

    :ref:`auth`

Common Tasks
------------

Create a :class:`.CredentialManager` Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    This should be obvious...but, the following examples pass the API Token via
    arguments to :py:func:`credmgr.CredentialManager`. If you do this, you need to be
    careful not to reveal this information to the outside world if you share your code.
    It is recommended to use a :ref:`.credmgr.ini file <.credmgr.ini>` in order to keep
    your API Token and in turn, your..ya know..credentials in CredentialManager safe and
    separate from your code.

You need an instance of the :class:`.CredentialManager` class to do *anything* with
CredentialManager.

In order to initialize a :class:`.CredentialManager` instance, you need to authenticate
with one of the following:

1. An API Token or,
2. Your CredentialManager username/password pair

.. seealso::

    :ref:`auth`

If you prefer, you can provide these by passing in keyword arguments ``apiToken`` or
``username`` and ``password`` when you call the :class:`.CredentialManager` initializer,
like the following:

.. code-block:: python

    from credmgr import CredentialManager

    credentialManager = CredentialManager(apiToken="an api token")

    print(credentialManager.currentUser().username)  # Output: your username

.. note::

    See :ref:`configuration` for better ways to pass credentials to credmgr.

Obtain a :class:`.Bot` Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To obtain a :class:`.Bot` instance, pass the Bot's name when calling :properyt: on your
:class:`.CredentialManager` instance. For instance:

.. code-block:: python

    bot = credentialManager.bot("botName")
    print(bot.name)  # Output: botName

Now that you have a :class:`.Bot` instance, you can get the bot's configured apps
(:class:`.RedditApp`, :class:`.SentryToken`, and/or :class:`.DatabaseCredential`) and
get each app's credentials. The following examples will use the above code to initialize
a :class:`.Bot` instance as..ya know.. ``bot``.

.. _gettingredditinstance:

Obtain :class:`.RedditApp` Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way of obtaining a :py:class:`.RedditApp` is by accessing it from a
:class:`.Bot` instance. The intended use for :py:class:`.RedditApp` is to initialize a
``praw.Reddit``. The :py:class:`.RedditApp` has a special property that will initialize
the ``praw.Reddit`` instance for you.

To initialize a read-only ``praw.Reddit`` instance do:

.. code-block:: python

    redditApp = bot.redditApp
    print(redditApp.name)  # Output: myRedditApp
    reddit = redditApp.reddit()  # This will return an read-only instance
    print(reddit.read_only)  # Output: True

To initialize an authenticated ``praw.Reddit`` instance for u/``redditor`` do:

.. code-block:: python

    redditApp = bot.redditApp
    print(redditApp.name)  # Output: myRedditApp
    reddit = redditApp.reddit("redditor")
    print(reddit.read_only)  # Output: False
    print(reddit.user.me())  # Output: redditor

.. note::

    This will only work if all of the follow conditions are met * Used CredentialManager
    create a `refresh token auth url <https://credmgr.jesassn.org/refresh_tokens>`_ with
    a permanent duration, the needed scopes, and used
    ``https://credmgr.jesassn.org/oauth2/reddit_callback`` as the ``redirectUri`` *
    Provided the auth url to ``redditor`` * ``redditor`` navigated to url to allow
    ``myRedditApp`` access to their account

.. _gettingsentrytokeninstance:

Obtain :class:`.SentryToken` Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    sentryToken = bot.sentryToken
    print(sentryToken.name)  # Output: mySentryToken
    print(sentryToken.dsn)  # Output: DSN of the sentryToken (this is the important part)

.. _gettingdatabasecredentialsinstance:

Obtain :class:`.DatabaseCredential` Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    databaseCredential = bot.databaseCredential
    print(databaseCredential.name)  # Output: name of the databaseCredential
    print(
        databaseCredential.databaseHost
    )  # Output: Address used to connect to the database
    print(
        databaseCredential.databaseUsername
    )  # Output: Username used to establish connection with database
    print(
        databaseCredential.databasePassword
    )  # Output: Password used to establish connection with database
    print(databaseCredential.databasePort)  # Output: Port number to create connection over

.. _determine-available-attributes-of-an-object:

Determine Available Attributes of an Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a credmgr object, e.g., :class:`.RedditApp`, :class:`.SentryToken`, or
:class:`.DatabaseCredential`, and you want to see what attributes are available along
with their values, use the built-in :py:func:`vars` function of python. For example:

.. code-block:: python

    from pprint import pprint

    bot = credentialManager.bot("botName")
    databaseCredential = bot.databaseCredential
    pprint(vars(databaseCredential))

Credmgr object initialization only creates attributes that gets passed when it is
initialized. As a result, some :class:`.DatabaseCredential` instances might not have a
``databasePassword`` while others do. So, if you doing the following on the bot,
``botName``'s ``databaseCredential`` that doesn't have a set ``databasePassword``:

.. code-block:: python

    bot = credentialManager.bot("botName")
    databaseCredential = bot.databaseCredential
    print(databaseCredential.databasePassword)

raises the following:

.. code-block::

    AttributeError: 'DatabaseCredential' object has no attribute 'databasePassword'
