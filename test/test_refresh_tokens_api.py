import unittest

import CredentialManager
from CredentialManager.api.refresh_tokens_api import RefreshTokensApi


class TestRefreshTokensApi(unittest.TestCase):
    '''RefreshTokensApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.refresh_tokens_api.RefreshTokensApi()

    def tearDown(self):
        pass

    def test_delete_refresh_token_by_id(self):
        '''Test case for delete_refresh_token_by_id

        Delete a Refresh Token by ID
        '''
        pass

    def test_get_refresh_token_by_id(self):
        '''Test case for get_refresh_token_by_id

        Get Refresh Token details by ID
        '''
        pass

    def test_get_refresh_tokens(self):
        '''Test case for get_refresh_tokens

        List of Refresh Tokens
        '''
        pass

    def test_options_get_refresh_token_by_redditor(self):
        '''Test case for options_get_refresh_token_by_redditor

        Check which methods are allowed
        '''
        pass

    def test_options_refresh_token_by_id(self):
        '''Test case for options_refresh_token_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_refresh_tokens(self):
        '''Test case for options_refresh_tokens

        Check which methods are allowed
        '''
        pass

    def test_patch_refresh_token_by_id(self):
        '''Test case for patch_refresh_token_by_id

        Patch refresh_token details by ID
        '''
        pass

    def test_post_get_refresh_token_by_redditor(self):
        '''Test case for post_get_refresh_token_by_redditor

        Get Refresh Token by reddit app and redditor
        '''
        pass

if __name__ == '__main__':
    unittest.main()