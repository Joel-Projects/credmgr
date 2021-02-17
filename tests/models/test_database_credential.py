import pytest
from credmgr.models import DatabaseCredential

from credmgr.exceptions import Conflict, NotFound, ServerError

data = {
    "name": "testDatabaseCredential",
    "databaseUsername": "databaseUsername",
    "databaseHost": "databaseHost",
    "database": "database",
    "databaseFlavor": "databaseFlavor",
    "databasePort": 6543,
    "databasePassword": "databasePassword",
    "useSsh": True,
    "sshHost": "sshHost",
    "sshPort": 1234,
    "sshUsername": "sshUsername",
    "sshPassword": "sshPassword",
    "useSshKey": True,
    "privateKey": "privateKey",
    "privateKeyPassphrase": "privateKeyPassphrase",
}


def testCreateDatabaseCredential(credentialManager):
    databaseCredential = credentialManager.databaseCredential.create(**data)
    print(databaseCredential.id)
    for key, value in data.items():
        assert getattr(databaseCredential, key) == value


def testCreateDatabaseCredentialOtherUser(credentialManager):
    newData = {**data, "owner": 4}
    databaseCredential = credentialManager.databaseCredential.create(
        **{**newData, "owner": 4}
    )
    for key, value in newData.items():
        if key == "owner":
            assert getattr(databaseCredential, key).id == value
            continue
        assert getattr(databaseCredential, key) == value


def testCreateDatabaseCredentialBadParams(credentialManager):
    data = {"name": "se"}
    with pytest.raises(ServerError):
        _ = credentialManager.databaseCredential.create(**data)


def testCreateDatabaseCredentialExisting(credentialManager):
    with pytest.raises(Conflict):
        _ = credentialManager.databaseCredential.create(**data)


def testDeleteDatabaseCredential(credentialManager):
    databaseCredential = credentialManager.databaseCredential(3)
    databaseCredential.delete()
    with pytest.raises(NotFound):
        _ = credentialManager.databaseCredential(3)


def testEditDatabaseCredential(credentialManager):
    databaseCredential = credentialManager.databaseCredential(3)
    databaseCredential.edit(databaseUsername="newUsername")
    assert databaseCredential.databaseUsername == "newUsername"


def testEditDatabaseCredentialConflictingData(credentialManager):
    databaseCredential = credentialManager.databaseCredential(4)
    with pytest.raises(Conflict):
        databaseCredential.edit(name="testDatabaseCredential")


def testListDatabaseCredentials(credentialManager):
    databaseCredentials = credentialManager.databaseCredentials()
    for databaseCredential in databaseCredentials:
        assert isinstance(databaseCredential, DatabaseCredential)
