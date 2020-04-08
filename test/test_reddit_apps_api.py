import unittest

import CredentialManager
from CredentialManager.api.reddit_apps_api import RedditAppsApi


class TestRedditAppsApi(unittest.TestCase):
    '''RedditAppsApi unit test stubs'''

    def setUp(self):
        self.api = CredentialManager.api.reddit_apps_api.RedditAppsApi()

    def tearDown(self):
        pass

    def test_delete_reddit_app_by_id(self):
        '''Test case for delete_reddit_app_by_id

        Delete a Reddit App by ID
        '''
        pass

    def test_get_reddit_app_by_id(self):
        '''Test case for get_reddit_app_by_id

        Get Reddit App details by ID
        '''
        pass

    def test_get_reddit_apps(self):
        '''Test case for get_reddit_apps

        List of Reddit Apps
        '''
        pass

    def test_options_generate_auth_url(self):
        '''Test case for options_generate_auth_url

        Check which methods are allowed
        '''
        pass

    def test_options_reddit_app_by_id(self):
        '''Test case for options_reddit_app_by_id

        Check which methods are allowed
        '''
        pass

    def test_options_reddit_apps(self):
        '''Test case for options_reddit_apps

        Check which methods are allowed
        '''
        pass

    def test_patch_reddit_app_by_id(self):
        '''Test case for patch_reddit_app_by_id

        Patch reddit_app details by ID
        '''
        pass

    def test_post_generate_auth_url(self):
        '''Test case for post_generate_auth_url

        Generate a reddit auth url
        '''
        pass

    def test_post_reddit_app_by_id(self):
        '''Test case for post_reddit_app_by_id

        Get Refresh Token by reddit app and redditor
        '''
        pass

    def test_post_reddit_apps(self):
        '''Test case for post_reddit_apps

        Create a new Reddit App
        '''
        pass

if __name__ == '__main__':
    unittest.main()