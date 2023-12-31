# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки шаблонов сообщений
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Event_System.Template_TemplatesMessages_settings import \
    TemplateTemplatesMessages


# -------------------------------------------------------------------------------------------------------------


class TemplatesMessages(TemplateTemplatesMessages):
    """
    Настройки шаблонов сообщений

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
        Настройки шаблонов сообщений

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
# 			"id":3,
# 			"meterDataTemplateId":1,
# 			"dataDepth":44,
# 			"meterTemplateId":1,
# 			"dataClass":"moment"
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
