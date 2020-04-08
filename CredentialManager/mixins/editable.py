class EditableMixin:
    _editableAttrs = []

    def edit(self, **kwargs):
        payload = []
        for attr in self._editableAttrs:
            value = kwargs.get(attr, None)
            if value:
                payload.append({'op': 'replace', 'path': f'/{attr}', 'value': value})
        return self._credmgr.patch(self, f'{self._path}/{id.id}', body=payload)