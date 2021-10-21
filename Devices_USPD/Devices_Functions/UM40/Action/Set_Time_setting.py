# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class SetTimeSetting(TemplateFunctional):
    """
    Установка времени

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Set_Time_setting")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _Time_Set_dict = {}

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Установка времени

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        self._date_time_now()

        # self._Time_Set_dict = {Year Month Day Hour Minute Second Time Zone}

        # print(self.headers)
        # print(self.cookies)

    def _date_time_now(self):
        """
        Вспомогательный метод Получающий сегодняшние время сейчас
        и заполняет правильно им _Time_Set_dict
        :return:
        """
        # Вспомомгательный метод Получающий сегоднянее время сейчас

        import datetime
        # Year Month Day Hour Minute Second Time_Zone
        self._Time_Set_dict = {}

        date_now = datetime.datetime.now(datetime.timezone.utc).astimezone().replace(microsecond=0)
        self._Time_Set_dict['Year'] = str(date_now.year)
        self._Time_Set_dict['Month'] = str(date_now.month)
        self._Time_Set_dict['Day'] = str(date_now.day)
        self._Time_Set_dict['Hour'] = str(date_now.hour)
        self._Time_Set_dict['Minute'] = str(date_now.minute)
        self._Time_Set_dict['Second'] = str(date_now.second)
        # self._Time_Set_dict['Time_Zone'] = str(date_now.timetz())
        Time_Zone = date_now.strftime('%z')
        # Если наша строка не пустая - разделяем точкой
        if len(Time_Zone) > 0:
            Time_Zone = Time_Zone[:3] + ':' + Time_Zone[3:]
        self._Time_Set_dict['Time_Zone'] = str(Time_Zone)

    def Setup_JSON(self, data):
        """
        Перезаписываем данные - PUT

        Формат JSON
        {"time": "2007-10-15T01:33:25+10:00"}

        :param data: JSON На запись , который игнорирует
        :return:
        """
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def add_Year(self, Year: int):
        """
        Добавляем Год
        :param Year: Год - Формат - 2021
        :return:
        """

        self._Time_Set_dict['Year'] = str(Year)

    def add_Month(self, Month: int):
        """
        Добавляем Месяц
        :param Month: Месяц - Формат - 02
        :return:
        """

        self._Time_Set_dict['Month'] = str(Month)

    def add_Day(self, Day: int):
        """
        Добавляем День
        :param Day: День - Формат - 01
        :return:
        """

        self._Time_Set_dict['Day'] = str(Day)

    def add_Hour(self, Hour: int):
        """
        Добавляем Час
        :param Hour: ЧАС - Формат - 24 часа - 18 или 01
        :return:
        """

        self._Time_Set_dict['Hour'] = str(Hour)

    def add_Minute(self, Minute: int):
        """
        Добавляем Минуты
        :param Minute: Минуты - Формат - 09
        :return:
        """

        self._Time_Set_dict['Minute'] = str(Minute)

    def add_Second(self, Second: int):
        """
        Добавляем Секунды
        :param Second: Секунды - Формат - 07
        :return:
        """

        self._Time_Set_dict['Second'] = str(Second)

    def add_Time_Zone(self, Time_Zone: str):
        """
        Добавляем Часовой пояс
        :param Time_Zone: Часовой пояс - Формат +03:00
        :return:
        """

        self._Time_Set_dict['Time_Zone'] = str(Time_Zone)

    def Setup_Time_Set(self):
        """
        Отправляем добавленные данные.
        Значения по умолчанию - текущее время
        Если время не изменялось то используются значения по Умолчанию.

        :return:
        """
        # Получаем наши значения
        Year = self._Time_Set_dict.get('Year')
        Month = self._Time_Set_dict.get('Month')
        Day = self._Time_Set_dict.get('Day')
        Hour = self._Time_Set_dict.get('Hour')
        Minute = self._Time_Set_dict.get('Minute')
        Second = self._Time_Set_dict.get('Second')
        Time_Zone = self._Time_Set_dict.get('Time_Zone')

        # Теперь собираем в единую стрингу
        Time_string = Year + '-' + Month + '-' + Day + 'T' + Hour + ':' + Minute + ':' + Second + Time_Zone

        data = {"time": Time_string}
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# lol = SetTimeSetting().Setup_JSON(data={"time": "2007-10-15T01:33:25+10:00"})
# SetTimeSetting_ = SetTimeSetting()
# SetTimeSetting_.add_Year(1960)
# SetTimeSetting_.add_Month(10)
# SetTimeSetting_.add_Day(15)
# SetTimeSetting_.add_Hour(1)
# SetTimeSetting_.add_Minute(33)
# SetTimeSetting_.add_Second(25)
# SetTimeSetting_.add_Time_Zone("")
# lol = SetTimeSetting_.Setup_Time_Set()
# print(lol)
