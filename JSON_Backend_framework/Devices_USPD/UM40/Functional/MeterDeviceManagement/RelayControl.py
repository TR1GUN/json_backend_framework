# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Управление реле
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterManagement.Template_RelayControl import TemplateRelayControl


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


class RelayControl(TemplateRelayControl):
    """
     Управление реле

    """
    # Общие настройки
    Relay = SettingsRelay()

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Шаблон Установки времени на счетчике

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    def _getting_settings(self):

        """ Проверяем значение реле"""

        data = self.Relay.get_Relay_settings()

        if data is None:
            data = {}
        return data

    def SetRelay(self, data):
        """
        Запросить данные - POST

        :param data:
        :return:
        """
        if data is None:
            data = self._getting_settings()
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response
# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = { "id": 1, "relayId": 1, "relayState": 1 }
# -------------------------------------------------------------------------------------------------------------
