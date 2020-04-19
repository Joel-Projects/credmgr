class ToggableMixin:
    _enabledAttr = 'enabled'

    def toggle(self, enabled):
        return self._credmgr.patch(f'{self._path}/{id.id}', body=[{'op': 'replace', 'path': f'/{self._enabledAttr}', 'value': enabled}])