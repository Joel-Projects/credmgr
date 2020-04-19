from credmgr.mixins import BaseModel, DeletableMixin


class RefreshToken(BaseModel, DeletableMixin):
    _attrTypes = {
        **BaseModel._attrTypes,
        'reddit_app_id': 'str',
        'redditor': 'str',
        'refresh_token': 'str',
        'owner_id': 'int',
        'scopes': 'str',
        'issued_at': 'datetime',
        'revoked': 'bool',
        'revoked_at': 'datetime'
    }

    _path = '/refresh_tokens'
    _credmgrCallable = 'refreshToken'

    def __init__(self, credmgr, id=None, redditAppId=None, redditor=None, refreshToken=None, ownerId=None, scopes=None, issuedAt=None, revoked=None, revokedAt=None):
        super().__init__(credmgr, id)
        if redditAppId:
            self.redditAppId = redditAppId
        if redditor:
            self.redditor = redditor
        if refreshToken:
            self.refreshToken = refreshToken
        if ownerId:
            self.ownerId = ownerId
        if scopes:
            self.scopes = scopes
        if issuedAt:
            self.issuedAt = issuedAt
        if revoked:
            self.revoked = revoked
        if revokedAt:
            self.revokedAt = revokedAt