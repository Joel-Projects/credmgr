import pytest
from credmgr.models import DatabaseCredential

from credmgr.exceptions import Conflict, NotFound, ServerError

data = {
    'appName': 'testDatabaseCredential',
    'databaseUsername': 'databaseUsername',
    'databaseHost': 'databaseHost',
    'database': 'database',
    'databaseFlavor': 'databaseFlavor',
    'databasePort': 6543,
    'databasePassword': 'databasePassword',
    'useSsh': True,
    'sshHost': 'sshHost',
    'sshPort': 1234,
    'sshUsername': 'sshUsername',
    'sshPassword': 'sshPassword',
    'useSshKey': True,
    'privateKey': 'privateKey',
    'privateKeyPassphrase': 'privateKeyPassphrase',
}

def testCreateDatabaseCredential(credmgr):
    databaseCredential = credmgr.databaseCredential.create(**data)
    print(databaseCredential.id)
    for key, value in data.items():
        assert getattr(databaseCredential, key) == value

def testCreateDatabaseCredentialOtherUser(credmgr):
    newData = {**data, 'owner': 4}
    databaseCredential = credmgr.databaseCredential.create(**{**newData, 'owner': 4})
    for key, value in newData.items():
        if key == 'owner':
            assert getattr(databaseCredential, key).id == value
            continue
        assert getattr(databaseCredential, key) == value

def testCreateDatabaseCredentialBadParams(credmgr):
    data = {'appName': 'se'}
    with pytest.raises(ServerError):
        _ = credmgr.databaseCredential.create(**data)

def testCreateDatabaseCredentialExisting(credmgr):
    with pytest.raises(Conflict):
        _ = credmgr.databaseCredential.create(**data)

def testDeleteDatabaseCredential(credmgr):
    databaseCredential = credmgr.databaseCredential(3)
    databaseCredential.delete()
    with pytest.raises(NotFound):
        _ = credmgr.databaseCredential(3)

def testEditDatabaseCredential(credmgr):
    databaseCredential = credmgr.databaseCredential(3)
    databaseCredential.edit(databaseUsername='newUsername')
    assert databaseCredential.databaseUsername == 'newUsername'

def testEditDatabaseCredentialConflictingData(credmgr):
    databaseCredential = credmgr.databaseCredential(4)
    with pytest.raises(Conflict):
        databaseCredential.edit(appName='testDatabaseCredential')

def testListDatabaseCredentials(credmgr):
    databaseCredentials = credmgr.databaseCredentials()
    for databaseCredential in databaseCredentials:
        assert isinstance(databaseCredential, DatabaseCredential)
