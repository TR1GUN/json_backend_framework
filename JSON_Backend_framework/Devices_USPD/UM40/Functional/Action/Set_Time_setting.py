# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Actions.Template_Action_Time_set import TemplateActionTimeSet

from JSON_Backend_framework.Devices_USPD.settings import url_path

from JSON_Backend_framework.Service.TemplateDecorator import read_USPD_Time_Request

from JSON_Backend_framework.FormJSON.UM40.Action.JSON_Construct_Actions_Set_Time import SETYear, SETMonth, SETDay , SETHour , SETMinute , SETSecond , SETTimeZone
# -------------------------------------------------------------------------------------------------------------


class TimeSet(TemplateActionTimeSet):
    """
    Установка времени

    """

    # URL

    _path_url = url_path.get("Set_time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _Time_Set_dict = {}

    Year = None
    Month = None
    Day = None

    Hour = None
    Minute = None
    Second = None

    TimeZone = None

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

        self._Time_Set_dict = {}

        # Запрос настроек
        self._define_settings()

    def _define_settings(self):
        """
        Определяем наш JSON

        """
        self.Year = SETYear()
        self.Month = SETMonth()
        self.Day = SETDay()

        self.Hour = SETHour()
        self.Minute = SETMinute()
        self.Second = SETSecond()

        self.TimeZone = SETTimeZone()

    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        # Используем системное время ПК
        data = self._SystemTime()
        try:
            # делаем запрос - получаем ответ
            response = self._read_Time_to_Device()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    data = answer_setting

        except Exception as e:

            print("При считывании параметров возникла ошибка - Используем время системы " + str(e))

        return data

    @read_USPD_Time_Request
    def _read_Time_to_Device(self):

        """
        Запрашиваем данные для чтения времени - Это важно

        """

        from JSON_Backend_framework.Devices_USPD.UM40.Functional.InfoState.Time import StateTime

        Time = StateTime(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address).Read()

        return Time

    def _Parse_TimeDevice(self, TimeDevice):
        """
        Парсим время девайса

        """

        TimeDevice = TimeDevice.get("time")
        import re
        date_line = re.findall('\d{4}|\d{2}|\d{2}|\d{2}|\d{2}|\d{2}|\d{2}|\d{2}', TimeDevice)
        # Теперь получаем все данные
        Device_Time = {}
        Device_Time['Year'] = date_line[0]
        Device_Time['Month'] = date_line[1]
        Device_Time['Day'] = date_line[2]
        Device_Time['Hour'] = date_line[3]
        Device_Time['Minute'] = date_line[4]
        Device_Time['Second'] = date_line[5]
        Device_Time['Time_Zone'] = "+" + date_line[6] + ":" + date_line[7]

        return Device_Time

    def _define_data_set(self):
        """
        В этом методе определяем данные что будем отправлять
        """

        # Поскольку здесь нельзя задать никакие данные , вставляем данные что будем считывать
        SetTime = {}
        # Получаем наши значения
        Year = self.Year.get_Year()
        Month = self.Month.get_Month()
        Day = self.Day.get_Day()
        Hour = self.Hour.get_Hour()
        Minute = self.Minute.get_Minute()
        Second = self.Second.get_Second()
        Time_Zone = self.TimeZone.get_Time_Zone()

        # Формируем Время - Запрашиваем устройство
        data = self._request_setting()
        # Парсим
        SetTime = self._Parse_TimeDevice(TimeDevice=data)

        # Переопределяем
        if Year is not None:
            SetTime['Year'] = Year
        if Month is not None:
            SetTime['Month'] = Month
        if Day is not None:
            SetTime['Day'] = Day
        if Hour is not None:
            SetTime['Hour'] = Hour
        if Minute is not None:
            SetTime['Minute'] = Minute
        if Second is not None:
            SetTime['Second'] = Second
        if Time_Zone is not None:
            SetTime['Time_Zone'] = Time_Zone

        self._Time_Set_dict = SetTime

        data = self._Create_JSON_data()
        # Запращиваем данные

        self._define_settings()

        return data

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# data =  {"time": "2007-10-15T01:33:25+10:00"}
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
