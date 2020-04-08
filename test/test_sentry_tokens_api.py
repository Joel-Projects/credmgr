import unittest

import CredentialManager
from CredentialManager.api.sentry_tokens_api import SentryTokensApi


class TestSentryTokensApi(unittest.TestCase):
    '''SentryTokensApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.sentry_tokens_api.SentryTokensApi()

    def tearDown(self):
        pass

    def test_delete_sentry_token_by_id(self):
        '''Test case for delete_sentry_token_by_id

        Delete a Sentry Token by ID
        '''
        pass

    def test_get_sentry_token_by_id(self):
        '''Test case for get_sentry_token_by_id

        Get Sentry Token details by ID
        '''
        pass

    def test_get_sentry_tokens(self):
        '''Test case for get_sentry_tokens

        List of Sentry Tokens
        '''
        pass

    def test_options_sentry_token_by_id(self):
        '''Test case for options_sentry_token_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_sentry_tokens(self):
        '''Test case for options_sentry_tokens

        Check which methods are allowed
        '''
        pass

    def test_patch_sentry_token_by_id(self):
        '''Test case for patch_sentry_token_by_id

        Patch sentry_token details by ID
        '''
        pass

    def test_post_sentry_tokens(self):
        '''Test case for post_sentry_tokens

        Create a new Sentry Token
        '''
        pass

if __name__ == '__main__':
    unittest.main()