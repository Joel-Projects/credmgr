class ToggableMixin:

    _enabledAttr = 'enabled'

    def toggle(self, enabled=True):
        return self._credmgr.patch(self, f'{self._path}/{id.id}', body=[{'op': 'replace', 'path': f'/{self._enabledAttr}', 'value': enabled}])