class CredentialManagerException(Exception):
    '''The base CredentialManager Exception that all other exception classes extend.'''

class InitializationError(CredentialManagerException):
    '''Invalid initialization paramaters were used.'''

class SerializerException(CredentialManagerException):
    '''Serializaton/deserialzation error occured.'''

class APIException(CredentialManagerException):
    '''Base exception class'''

    def __init__(self, response):
        self.status = response.status_code
        self.reason = response.reason
        self.body = response.text
        self.headers = response.headers

    def __str__(self):
        '''Custom error messages for exception'''
        error_message = f'\n{self.status}: {self.reason}'
        if self.headers:
            error_message += f'\nResponse headers: {self.headers}'
        if self.body:
            error_message += f'\nResponse body: {self.body}'

        return error_message

class Conflict(APIException):
    '''Made a conflicting request.'''

class Forbidden(APIException):
    '''Made request to a resource without required permissions.'''

class InvalidJSON(APIException):
    '''Response returned invalid JSON.'''

class InvalidRequest(APIException):
    '''Made request with invalid parameters.'''

class NotFound(APIException):
    '''Could not find requested resource.'''

class ServerError(APIException):
    '''Error occured on server during request.'''

class Unauthorized(APIException):
    '''Made request to resource without authenticating.'''