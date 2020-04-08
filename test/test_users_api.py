import unittest

import CredentialManager
from CredentialManager.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    '''UsersApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.users_api.UsersApi()

    def tearDown(self):
        pass

    def test_delete_user_by_id(self):
        '''Test case for delete_user_by_id

        Delete a user by ID
        '''
        pass

    def test_get_apps_by_user_id(self):
        '''Test case for get_apps_by_user_id

        Get items that is owned by user
        '''
        pass

    def test_get_user_by_id(self):
        '''Test case for get_user_by_id

        Get user details by ID
        '''
        pass

    def test_get_user_me(self):
        '''Test case for get_user_me

        Get current user details
        '''
        pass

    def test_get_users(self):
        '''Test case for get_users

        List of users
        '''
        pass

    def test_options_apps_by_user_id(self):
        '''Test case for options_apps_by_user_id

        Check which methods are allowed
        '''
        pass

    def test_options_user_by_id(self):
        '''Test case for options_user_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_user_me(self):
        '''Test case for options_user_me

        Check which methods are allowed
        '''
        pass

    def test_options_users(self):
        '''Test case for options_users

        Check which methods are allowed
        '''
        pass

    def test_patch_user_by_id(self):
        '''Test case for patch_user_by_id

        Patch user details by ID
        '''
        pass

    def test_post_users(self):
        '''Test case for post_users

        Create a new user
        '''
        pass

if __name__ == '__main__':
    unittest.main()