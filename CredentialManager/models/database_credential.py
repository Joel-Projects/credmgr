from ..mixins import BaseApp


class DatabaseCredential(BaseApp):
    _attr_types = {**BaseApp._attr_types,
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

    _attribute_map = {**BaseApp._attribute_map,
        'database_username': 'database_username',
        'database_host': 'database_host',
        'database': 'database',
        'database_flavor': 'database_flavor',
        'database_port': 'database_port',
        'database_password': 'database_password',
        'use_ssh': 'use_ssh',
        'ssh_host': 'ssh_host',
        'ssh_port': 'ssh_port',
        'ssh_username': 'ssh_username',
        'ssh_password': 'ssh_password',
        'use_ssh_key': 'use_ssh_key',
        'private_key': 'private_key',
        'private_key_passphrase': 'private_key_passphrase'
        }
    editableAttrs = BaseApp._editableAttrs + [
        'database_username',
        'database_host',
        'database',
        'database_flavor',
        'database_port',
        'database_password',
        'use_ssh',
        'ssh_host',
        'ssh_port',
        'ssh_username',
        'ssh_password',
        'use_ssh_key',
        'private_key',
        'private_key_passphrase',
         ]
    _path = '/database_credentials'
    def __init__(self, credmgr, id=None, app_name=None, database_username=None, database_host=None, database=None, database_flavor=None,
                 database_port=None, database_password=None, use_ssh=None, ssh_host=None, ssh_port=None, ssh_username=None, ssh_password=None,
                 use_ssh_key=None, private_key=None, private_key_passphrase=None, enabled=None, owner_id=None):
        super().__init__(credmgr, id, app_name, enabled, owner_id)
        if database_username:
            self.database_username = database_username
        if database_host:
            self.database_host = database_host
        if database:
            self.database = database
        if database_flavor:
            self.database_flavor = database_flavor
        if database_port:
            self.database_port = database_port
        if database_password:
            self.database_password = database_password
        if use_ssh:
            self.use_ssh = use_ssh
        if ssh_host:
            self.ssh_host = ssh_host
        if ssh_port:
            self.ssh_port = ssh_port
        if ssh_username:
            self.ssh_username = ssh_username
        if ssh_password:
            self.ssh_password = ssh_password
        if use_ssh_key:
            self.use_ssh_key = use_ssh_key
        if private_key:
            self.private_key = private_key
        if private_key_passphrase:
            self.private_key_passphrase = private_key_passphrase
        if enabled:
            self.enabled = enabled
        if owner_id:
            self.owner_id = owner_id