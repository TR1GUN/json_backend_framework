# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки дискретных входов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_DIn_settings import \
    TemplateInterface_DIn_DiscreteInput

# -------------------------------------------------------------------------------------------------------------


class Interface_DIn_DiscreteInput(TemplateInterface_DIn_DiscreteInput):
    """
    Настройки дискретных входов

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
        Настройки дискретных входов

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
# 			"id":0,
# 			"addr":0,
# 			"filter":100,
# 			"state":				1
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
