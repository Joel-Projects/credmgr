"""Provide the SentryToken class."""
from ..mixins import BaseApp
from .utils import _resolveUser


class SentryToken(BaseApp):
    """A class for SentryToken instances."""

    _attrTypes = {**BaseApp._attrTypes, "dsn": "str"}
    _editableAttrs = BaseApp._editableAttrs + ["dsn"]
    _path = "/sentry_tokens"
    _credmgrCallable = "sentryToken"

    def __init__(self, credmgr, **kwargs):
        """Initialize a SentryToken instance.

        :param credmgr: An instance of :class:`.CredentialManager`.
        :param id: ID of the Sentry Token
        :param str name: Name of the Sentry Token.
        :param str dsn: Sentry DSN url for reporting errors.
        :param ownerId: ID of the `.User` that owns this Sentry Token.

        """
        super().__init__(credmgr, **kwargs)

    @staticmethod
    @_resolveUser()
    def _create(_credmgr, name=None, dsn=None, owner=None):
        """Create a new Sentry Token.

        Sentry Tokens are used for logging and error reporting in applications

        :param str name: Name of the Sentry Token (required)
        :param str dsn: DSN of the Sentry Token (required)
        :param Union[User,int,str] owner: Owner of the verification. Requires Admin to
            create for other users.

        :returns: SentryToken

        """
        data = {"app_name": name, "dsn": dsn}
        if owner:
            data["owner_id"] = owner
        return _credmgr.post("/sentry_tokens", data=data)
