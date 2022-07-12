# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                   Настройки событий изменения состояния дискретных входов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Event_System.Template_Events_DIn_settings import \
    TemplateEventsDIn

# -------------------------------------------------------------------------------------------------------------


class EventsDIn(TemplateEventsDIn):
    """
    Настройки событий изменения состояния дискретных входов

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
        Настройки событий изменения состояния дискретных входов

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
# 			"id":2,
# 			"addr":1,
# 			"type":				3
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------