import configparser

import pytest
from betamax import Betamax

from credmgr import CredentialManager, config
from credmgr.exceptions import InitializationError
from tests.utils import genCassetteName


def _initialize_config_override(self):
    self.server = self._fetch("server")
    self.endpoint = self._fetch("endpoint")
    self.apiToken = None
    self.username = self._fetch("username")
    self.password = self._fetch("password")
    self.dateFormat = self._fetch("dateformat")


def testCredmgrInit(recorder, credentialManager):
    assert credentialManager.currentUser.username == "spaz"


def testCredmgrInitBadParams(credentialManager):
    with pytest.raises(InitializationError):
        _ = CredentialManager(
            apiToken="token", username="username", password="password"
        )


def testCredmgrInitBadSectionName(credentialManager):
    with pytest.raises(configparser.NoSectionError):
        _ = CredentialManager("invalid")


def testCredmgrNoParams():
    config.Config._initializeConfig = _initialize_config_override
    with pytest.raises(InitializationError):
        _ = CredentialManager()


def testCredmgrInitUsernamePassword():
    config.Config._initializeConfig = _initialize_config_override
    credmgr = CredentialManager(username="username", password="password")
    with Betamax(credmgr._requestor._session).use_cassette(genCassetteName()):
        assert credmgr.currentUser.username == "username"
