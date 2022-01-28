# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                                   Управление реле
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
class SettingsRelay:
    _Setting_Relay = None

    def __init__(self):
        self._Setting_Relay = None

    def set_Relay(self, MeterIdx: int, RelayId: int, RelayState: int):
        """
        Установка положения реле на счетчике по его MeterIdx

        """

        data = {
                "id": int(MeterIdx),
                "relayId": int(RelayId),
                "relayState": int(RelayState),
                }

        self._Setting_Relay = data

    def remove_Relay(self):
        """
        Удаление записанного положения Реле
        """
        self._Setting_Relay = None

    def get_Relay_settings(self):
        """ Получаем положение что задали """

        return self._Setting_Relay