from ..mixins import BaseApp


class SentryToken(BaseApp):
    _attrTypes = {**BaseApp._attrTypes, 'dsn': 'str'}
    _editableAttrs = BaseApp._editableAttrs + ['dsn']
    _path = '/sentry_tokens'
    _credmgrCallable = 'sentryToken'

    def __init__(self, credmgr, id=None, appName=None, dsn=None, enabled=None, ownerId=None, created=None):
        super().__init__(credmgr, id, appName, enabled, ownerId)
        if dsn:
            self.dsn = dsn
        if created:
            self.created = created