from ..mixins import BaseApp


class DatabaseCredential(BaseApp):
    _attrTypes = {
        **BaseApp._attrTypes,
        'database_username': 'str',
        'database_host': 'str',
        'database': 'str',
        'database_flavor': 'str',
        'database_port': 'int',
        'database_password': 'str',
        'use_ssh': 'bool',
        'ssh_host': 'str',
        'ssh_port': 'int',
        'ssh_username': 'str',
        'ssh_password': 'str',
        'use_ssh_key': 'bool',
        'private_key': 'str',
        'private_key_passphrase': 'str'
        }

    _editableAttrs = BaseApp._editableAttrs + ['databaseUsername', 'databaseHost', 'database', 'databaseFlavor', 'databasePort',
        'databasePassword', 'useSsh', 'sshHost', 'sshPort', 'sshUsername', 'sshPassword', 'useSshKey', 'privateKey',
        'privateKeyPassphrase']
    _path = '/database_credentials'
    _credmgrCallable = 'databaseCredential'

    def _Init_(self, credmgr, id=None, appName=None, databaseUsername=None, databaseHost=None, database=None, databaseFlavor=None,
                 databasePort=None, databasePassword=None, useSsh=None, sshHost=None, sshPort=None, sshUsername=None, sshPassword=None,
                 useSshKey=None, privateKey=None, privateKeyPassphrase=None, enabled=None, ownerId=None):
        super()._Init_(credmgr, id, appName, enabled, ownerId)
        if databaseUsername:
            self.databaseUsername = databaseUsername
        if databaseHost:
            self.databaseHost = databaseHost
        if database:
            self.database = database
        if databaseFlavor:
            self.databaseFlavor = databaseFlavor
        if databasePort:
            self.databasePort = databasePort
        if databasePassword:
            self.databasePassword = databasePassword
        if useSsh:
            self.useSsh = useSsh
        if sshHost:
            self.sshHost = sshHost
        if sshPort:
            self.sshPort = sshPort
        if sshUsername:
            self.sshUsername = sshUsername
        if sshPassword:
            self.sshPassword = sshPassword
        if useSshKey:
            self.useSshKey = useSshKey
        if privateKey:
            self.privateKey = privateKey
        if privateKeyPassphrase:
            self.privateKeyPassphrase = privateKeyPassphrase
        if enabled:
            self.enabled = enabled
        if ownerId:
            self.ownerId = ownerId