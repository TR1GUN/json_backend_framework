# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки MQTT-серверов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Servers.Template_MQTT_server_settings import \
    TemplateServer_MQTT


# -------------------------------------------------------------------------------------------------------------


class ServerMQTT(TemplateServer_MQTT):
    """

    Настройки MQTT-серверов
    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    # Settings = None

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки TCP-серверов

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # Получение настроек если поле Data не задано - В Качестве основного используется Запрос GET
    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса
        """
        data = self._request_setting()
        return data
# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# {
# 	"Settings":[
# 		{
# 			"id":1,
# 			"type":				1,
# 			"addr":"test.mosquitto.org",
# 			"port":1883,
# 			"prefix":"asd321",
# 			"login":"ivan",
# 			"password":"taranov",
# 			"deviceID":"123asd",
# 			"crypto":				2,
# 			"certCheck":false,
# 			"cert":""
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------