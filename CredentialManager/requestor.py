import requests

from .const import TIMEOUT, __version__


class Requestor(object):
    '''Requestor provides an interface to HTTP requests.'''

    def __getattr__(self, attribute):
        '''Pass all undefined attributes to the _http attribute.'''
        if attribute.startswith("__"):
            raise AttributeError
        return getattr(self._http, attribute)

    def __init__(self, config, session=None):
        '''Create an instance of the Requestor class.
        :param session: (Optional) A session to handle requests, compatible
            with requests.Session(). (Default: None)
        '''
        self.config = config
        self._http = session or requests.Session()
        self._http.headers["User-Agent"] = f"CredentialManager/{__version__}"

    def close(self):
        '''Call close on the underlying session.'''
        return self._http.close()

    def request(self, *args, **kwargs):
        return self._http.request(*args, **kwargs)
