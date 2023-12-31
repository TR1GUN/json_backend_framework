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

# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# {
# 	"Settings":[
# 		{
# 			"id":1,
# 			"addr":"test.mosquitto.org",
# 			"login":"test_login",
# 			"password":"1234567890",
# 			"port":1883,
# 			"prefix":"asd321",
# 			"deviceID":"123asd",
# 			"cropt":				2
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
