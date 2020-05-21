import praw
import pytest
from credmgr.models import RefreshToken

from credmgr.exceptions import Conflict, NotFound, ServerError


def testDeleteRefreshToken(credentialManager):
    refreshToken = credmgr.refreshToken(id=1)
    refreshToken.delete()
    with pytest.raises(NotFound):
        _ = credmgr.refreshToken(id=1)

def testListRefreshTokens(credentialManager):
    refreshTokens = credmgr.refreshTokens()
    for refreshToken in refreshTokens:
        assert isinstance(refreshToken, RefreshToken)
