import configparser

import pytest

from credmgr import CredentialManager
from credmgr.exceptions import InitializationError


def testCredmgrInit(credentialManager):
    assert credentialManager.currentUser.username == "spaz"


def testCredmgrInitBadParams(credentialManager):
    with pytest.raises(InitializationError):
        _ = CredentialManager(
            apiToken="token", username="username", password="password"
        )


def testCredmgrInitBadSectionName(credentialManager):
    with pytest.raises(configparser.NoSectionError):
        _ = CredentialManager("invalid")


def testCredmgrNoParams(credentialManager):
    with pytest.raises(InitializationError):
        _ = CredentialManager()


def testCredmgrInitUsernamePassword(credentialManager):
    credmgr = CredentialManager(username="username", password="password")
    credmgr._requestor._session = credentialManager._requestor._session
    credmgr._requestor._session.auth = credmgr._auth
    assert credmgr.currentUser.username == "username"
