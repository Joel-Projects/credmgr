import pytest

from credmgr.exceptions import NotFound
from credmgr.models import RefreshToken


def testDeleteRefreshToken(credentialManager):
    refreshToken = credentialManager.refreshToken(id=1)
    refreshToken.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.refreshToken(id=1)


def testListRefreshTokens(credentialManager):
    refreshTokens = credentialManager.refreshTokens()
    for refreshToken in refreshTokens:
        assert isinstance(refreshToken, RefreshToken)
