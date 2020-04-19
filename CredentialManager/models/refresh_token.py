from CredentialManager.mixins import BaseModel, DeletableMixin


class RefreshToken(BaseModel, DeletableMixin):
    _attrTypes = {
        **BaseModel._attrTypes,
        'reddit_app_id': 'str',
        'redditor': 'str',
        'refresh_token': 'str',
        'owner_id': 'str',
        'scopes': 'str',
        'issued_at': 'datetime',
        'revoked': 'bool',
        'revoked_at': 'datetime'
        }

    _path = '/refresh_tokens'
    _credmgrCallable = 'refresh_token'

    def __init__(self, credmgr, id=None, reddit_app_id=None, redditor=None, refresh_token=None, owner_id=None, scopes=None, issued_at=None,
                 revoked=None, revoked_at=None):
        super().__init__(credmgr, id)
        if reddit_app_id:
            self.reddit_app_id = reddit_app_id
        if redditor:
            self.redditor = redditor
        if refresh_token:
            self.refresh_token = refresh_token
        if owner_id:
            self.owner_id = owner_id
        if scopes:
            self.scopes = scopes
        if issued_at:
            self.issued_at = issued_at
        if revoked:
            self.revoked = revoked
        if revoked_at:
            self.revoked_at = revoked_at