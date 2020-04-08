import unittest

import CredentialManager
from CredentialManager.api.api_tokens_api import ApiTokensApi


class TestApiTokensApi(unittest.TestCase):
    '''ApiTokensApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.api_tokens_api.ApiTokensApi()

    def tearDown(self):
        pass

    def test_delete(self):
        '''Test case for delete

        Delete a API Token by ID
        '''
        pass

    def test_get_api_token_by_id(self):
        '''Test case for get_api_token_by_id

        Get API Token details by ID
        '''
        pass

    def test_get_api_tokens(self):
        '''Test case for get_api_tokens

        List of API Tokens
        '''
        pass

    def test_options_api_token_by_id(self):
        '''Test case for options_api_token_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_api_tokens(self):
        '''Test case for options_api_tokens

        Check which methods are allowed
        '''
        pass

    def test_patch_api_token_by_id(self):
        '''Test case for patch_api_token_by_id

        Patch api_token details by ID
        '''
        pass

    def test_post_api_tokens(self):
        '''Test case for post_api_tokens

        Create a new API Token
        '''
        pass

if __name__ == '__main__':
    unittest.main()