import configparser

import pytest

from credmgr.exceptions import InitializationError

from credmgr import CredentialManager


def testCredmgrInit(credentialManager):
    assert credentialManager.currentUser.username == 'spaz'

def testCredmgrInitBadParams(credentialManager):
    with pytest.raises(InitializationError):
        _ = CredentialManager(apiToken='token', username='username', password='password')

def testCredmgrInitBadSectionName(credentialManager):
    with pytest.raises(configparser.NoSectionError):
        _ = CredentialManager('invalid')

def testCredmgrNoParams(credentialManager):
    with pytest.raises(InitializationError):
        _ = CredentialManager()

def testCredmgrInitUsernamePassword():
    credentialManager = CredentialManager(username='username', password='password')
    assert credentialManager.currentUser.username == 'username'