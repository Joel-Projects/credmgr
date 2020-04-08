import unittest

import CredentialManager
from CredentialManager.api.bots_api import BotsApi


class TestBotsApi(unittest.TestCase):
    '''BotsApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.bots_api.BotsApi()

    def tearDown(self):
        pass

    def test_delete_bot_by_id(self):
        '''Test case for delete_bot_by_id

        Delete a Bot by ID
        '''
        pass

    def test_get_bot_by_id(self):
        '''Test case for get_bot_by_id

        Get Bot details by ID
        '''
        pass

    def test_get_bots(self):
        '''Test case for get_bots

        List of Bots
        '''
        pass

    def test_options_bot_by_id(self):
        '''Test case for options_bot_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_bots(self):
        '''Test case for options_bots

        Check which methods are allowed
        '''
        pass

    def test_options_get_bot_by_name(self):
        '''Test case for options_get_bot_by_name

        Check which methods are allowed
        '''
        pass

    def test_patch_bot_by_id(self):
        '''Test case for patch_bot_by_id

        Patch bot details by ID
        '''
        pass

    def test_post_bots(self):
        '''Test case for post_bots

        Create a new Bot
        '''
        pass

    def test_post_get_bot_by_name(self):
        '''Test case for post_get_bot_by_name

        Get Refresh Token by reddit app and redditor
        '''
        pass

if __name__ == '__main__':
    unittest.main()