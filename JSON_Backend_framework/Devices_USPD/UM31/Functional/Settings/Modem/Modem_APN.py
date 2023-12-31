# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки APN(точки доступа) -  СИМ карт
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Modem.Template_APN_settings import \
    TemplateAPN


# -------------------------------------------------------------------------------------------------------------

class ModemAPN(TemplateAPN):
    """
    Настройки APN(точки доступа)
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
        Настройки APN(точки доступа) -  СИМ карт

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
        # self._define_JSON()

    # Получение настроек если поле Data не задано - В Качестве основного используется Запрос GET
    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса
        """
        data = self._request_setting()
        return data

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# {
# 	"Settings":[
# 		{
# 			"id":1,
# 			"enable":true,
# 			"addr":"static.beeline.ru",
# 			"auth":true,
# 			"login":"beeline",
# 			"password":"beeline"
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
