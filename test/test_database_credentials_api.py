import unittest

import CredentialManager
from CredentialManager.api.database_credentials_api import DatabaseCredentialsApi


class TestDatabaseCredentialsApi(unittest.TestCase):
    '''DatabaseCredentialsApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.database_credentials_api.DatabaseCredentialsApi()

    def tearDown(self):
        pass

    def test_delete_database_credential_by_id(self):
        '''Test case for delete_database_credential_by_id

        Delete a Database Credential by ID
        '''
        pass

    def test_get_database_credential_by_id(self):
        '''Test case for get_database_credential_by_id

        Get Database Credential details by ID
        '''
        pass

    def test_get_database_credentials(self):
        '''Test case for get_database_credentials

        List of Database Credentials
        '''
        pass

    def test_options_database_credential_by_id(self):
        '''Test case for options_database_credential_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_database_credentials(self):
        '''Test case for options_database_credentials

        Check which methods are allowed
        '''
        pass

    def test_patch_database_credential_by_id(self):
        '''Test case for patch_database_credential_by_id

        Patch database_credential details by ID
        '''
        pass

    def test_post_database_credentials(self):
        '''Test case for post_database_credentials

        Create a new Database Credential
        '''
        pass

if __name__ == '__main__':
    unittest.main()