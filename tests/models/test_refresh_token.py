import pytest

from credmgr.exceptions import NotFound
from credmgr.models import RefreshToken


def testDeleteRefreshToken(recorder, credentialManager):
    refreshToken = credentialManager.refreshToken(id=1)
    refreshToken.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.refreshToken(id=1)


def testListRefreshTokens(recorder, credentialManager):
    refreshTokens = credentialManager.refreshTokens()
    for refreshToken in refreshTokens:
        assert isinstance(refreshToken, RefreshToken)
