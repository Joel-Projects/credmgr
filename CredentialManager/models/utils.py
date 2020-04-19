from CredentialManager.exceptions import NotFound


def resolveUser(userAttr='owner', returnAttr='id'):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            from . import User
            value = None
            user = kwargs.get(userAttr, None)
            if user:
                if isinstance(user, User):
                    value = getattr(user, returnAttr)
                elif isinstance(user, int):
                    value = user
                elif isinstance(user, str):
                    foundUser = self._credmgr.user(user)
                    if foundUser:
                        value = getattr(foundUser, returnAttr)
                kwargs[userAttr] = value
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def resolveModelFromInput(credmgr, model, input, returnAttr='id'):
    value = None
    if isinstance(input, model):
        value = getattr(input, returnAttr)
    elif isinstance(input, int):
        value = input
    elif isinstance(input, str):
        try:
            foundItem = getattr(credmgr, model._credmgrCallable)(input)
        except NotFound:
            foundItem = None
        if foundItem:
            value = getattr(foundItem, returnAttr)
    return value