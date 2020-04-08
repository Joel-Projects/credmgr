

class OwnerMixin:
    _editableAttrs = []

    @property
    def owner(self):
        user = self._credmgr.user(id=self.owner_id)
        return user