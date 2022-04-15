# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Недельный профиль тарифного расписания
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterManagement.Calendar.Template_Week import \
    TemplateCalendarWeek


# -------------------------------------------------------------------------------------------------------------

class CalendarWeek(TemplateCalendarWeek):
    """
    Недельный профиль тарифного расписания
    """
    # Общие настройки
    Calendar = None

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
        self.Calendar = {}

    def _getting_settings(self):

        """ Проверяем значение JSON """

        data = None
        # Обнуляем
        self._define_JSON()
        if data is None:
            data = {}
        return data

    def Set_Calendar(self, data: None):
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
        response = self._request_PUT(JSON=data)

        return response
# -------------------------------------------------------------------------------------------------------------
# ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {"id":1, "type": "Active",
#         "settings":[{"WeekName":"44656661756C74",
#         "monday":1, "tuesday":1, "wednesday":1, "thursday":1, "friday":1, "saturday":1, "sunday":1}]}
# data =  {"id":1, "type": "Passive",
#                   "settings":[{"WeekName":"44656661756C74",
#                   "monday":1, "tuesday":1, "wednesday":1, "thursday":1, "friday":1, "saturday":1, "sunday":1}]}

# -------------------------------------------------------------------------------------------------------------
