from requests.auth import AuthBase

class ApiTokenAuth(AuthBase):

    def __init__(self, api_token):
        self.api_token = api_token

    def __call__(self, request):
        request.headers['X-API-TOKEN'] = self.api_token
        return request