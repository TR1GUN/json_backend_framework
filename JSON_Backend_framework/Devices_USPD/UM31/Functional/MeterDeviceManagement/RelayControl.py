# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Управление реле
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterManagement.Template_RelayControl import TemplateRelayControl

from JSON_Backend_framework.FormJSON.UM40.MeterDeviceManagement.JSON_Construct_Management_RelayControl import SettingsRelay

# -------------------------------------------------------------------------------------------------------------


class RelayControl(TemplateRelayControl):
    """
     Управление реле

    """
    # Генерация JSON
    Relay_JSON = None

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

        # Обнуляем
        self._define_JSON()

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.MeterData = FormJSON_MeterData()

    def _getting_settings(self):

        """ Проверяем значение реле"""

        data = self.Relay.get_Relay_settings()

        # Обнуляем
        self._define_JSON()
        if data is None:
            data = {}
        return data

    def Set_Relay(self, data):
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
