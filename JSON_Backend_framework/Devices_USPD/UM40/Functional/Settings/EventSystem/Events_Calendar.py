# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки событий календаря
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Event_System.Template_Events_Calendar_settings import \
    TemplateCalendar


# -------------------------------------------------------------------------------------------------------------


class Calendar(TemplateCalendar):
    """
    Настройки событий календаря

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
        Настройки событий календаря

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
# 			"schedulerIds":[
# 				1
# 			],
# 			"calendarName":"test"
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
