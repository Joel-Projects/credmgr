from ..mixins import BaseApp


class SentryToken(BaseApp):
    _attrTypes = {**BaseApp._attrTypes, 'dsn': 'str'}
    _editableAttrs = BaseApp._editableAttrs + ['dsn']
    _path = '/sentry_tokens'
    _credmgrCallable = 'sentry_token'

    def __init__(self, credmgr, id=None, app_name=None, dsn=None, enabled=None, owner_id=None, created=None):
        super().__init__(credmgr, id, app_name, enabled, owner_id)
        if dsn:
            self.dsn = dsn
        if created:
            self.created = created