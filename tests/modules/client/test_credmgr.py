import configparser

import pytest

from credmgr.exceptions import InitializationError

from credmgr import CredentialManager


def testCredmgrInit(credmgr):
    assert credmgr.currentUser.username == 'spaz'

def testCredmgrInitBadParams(credmgr):
    with pytest.raises(InitializationError):
        _ = CredentialManager(apiToken='token', username='username', password='password')

def testCredmgrInitBadSectionName(credmgr):
    with pytest.raises(configparser.NoSectionError):
        _ = CredentialManager('invalid')

def testCredmgrNoParams(credmgr):
    with pytest.raises(InitializationError):
        _ = CredentialManager()

def testCredmgrInitUsernamePassword():
    credmgr = CredentialManager(username='username', password='password')
    assert credmgr.currentUser.username == 'username'