import praw
import pytest
from credmgr.models import RefreshToken

from credmgr.exceptions import Conflict, NotFound, ServerError


def testDeleteRefreshToken(credmgr):
    refreshToken = credmgr.refreshToken(id=1)
    refreshToken.delete()
    with pytest.raises(NotFound):
        _ = credmgr.refreshToken(id=1)

def testListRefreshTokens(credmgr):
    refreshTokens = credmgr.refreshTokens()
    for refreshToken in refreshTokens:
        assert isinstance(refreshToken, RefreshToken)
