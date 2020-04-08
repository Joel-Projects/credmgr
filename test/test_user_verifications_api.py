import unittest

import CredentialManager
from CredentialManager.api.user_verifications_api import UserVerificationsApi


class TestUserVerificationsApi(unittest.TestCase):
    '''UserVerificationsApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.user_verifications_api.UserVerificationsApi()

    def tearDown(self):
        pass

    def test_delete_user_verification_by_id(self):
        '''Test case for delete_user_verification_by_id

        Delete a User Verification by ID
        '''
        pass

    def test_get_user_verification_by_id(self):
        '''Test case for get_user_verification_by_id

        Get User Verification details by ID
        '''
        pass

    def test_get_user_verifications(self):
        '''Test case for get_user_verifications

        List of User Verifications
        '''
        pass

    def test_options_get_user_verification_by_user_id(self):
        '''Test case for options_get_user_verification_by_user_id

        Check which methods are allowed
        '''
        pass

    def test_options_user_verification_by_id(self):
        '''Test case for options_user_verification_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_user_verifications(self):
        '''Test case for options_user_verifications

        Check which methods are allowed
        '''
        pass

    def test_patch_user_verification_by_id(self):
        '''Test case for patch_user_verification_by_id

        Patch user_verification details by ID
        '''
        pass

    def test_post_get_user_verification_by_user_id(self):
        '''Test case for post_get_user_verification_by_user_id

        Get User Verification by User ID
        '''
        pass

    def test_post_user_verifications(self):
        '''Test case for post_user_verifications

        Create a new User Verification
        '''
        pass

if __name__ == '__main__':
    unittest.main()