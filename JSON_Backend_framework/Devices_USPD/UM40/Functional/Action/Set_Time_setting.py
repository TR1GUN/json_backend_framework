# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
#                                         Классы настроек времени
# -------------------------------------------------------------------------------------------------------------


# ГОД
class SETYear:
    """
    ГОД
    """
    _Year = None

    def __init__(self):
        self._Year = None

    def add_Year(self, Year: int):
        """
        Добавляем Год
        :param Year: Год - Формат - 2021
        :return:
        """
        if (Year > 999) and (Year < 10000):
            self._Year = str(Year)

    def remove_Year(self):
        """
        Удаляем год

        """
        self._Year = None

    def get_Year(self):
        """
        Берем Год

        :return:
        """
        return self._Year


# Месяц
class SETMonth:
    """
    Месяц
    """
    _Month = None

    def __init__(self):
        self._Month = None

    def add_Month(self, Month: int):
        """
        Добавляем Месяц
        :param Month: Месяц - Формат - 02
        :return:
        """
        if (Month > 0) and (Month < 13):
            # Теперь , если у нас меньше 10 , то теперь добавляем 0
            if Month > 9:
                Month = str(Month)
            else:
                Month = '0' + str(Month)

            self._Month = str(Month)

    def remove_Month(self):
        """
        Удаляем Месяц

        """
        self._Month = None

    def get_Month(self):
        """
        Берем Месяц

        :return:
        """
        return self._Month


# День
class SETDay:
    """
    День
    """
    _Day = None

    def __init__(self):
        self._Day = None

    def add_Day(self, Day: int):
        """
        Добавляем День
        :param Day: День - Формат - 01
        :return:
        """
        if (Day > 0) and (Day < 32):

            if Day > 9:
                Day = str(Day)
            else:
                Day = '0' + str(Day)

            self._Day = str(Day)

    def remove_Day(self):
        """
        Удаляем День

        """
        self._Day = None

    def get_Day(self):
        """
        Берем День

        :return:
        """
        return self._Day


# Час
class SETHour:
    """
        Час
    """
    _Hour = None

    def __init__(self):
        self._Hour = None

    def add_Hour(self, Hour: int):
        """
        Добавляем Час
        :param Hour: ЧАС - Формат - 24 часа - 18 или 01
        """
        if (Hour > 0) and (Hour < 25):

            if Hour > 9:
                Hour = str(Hour)
            else:
                Hour = '0' + str(Hour)

            self._Hour = str(Hour)

    def remove_Hour(self):
        """
        Удаляем ЧАС

        """
        self._Hour = None

    def get_Hour(self):
        """
        Берем ЧАС

        :return:
        """
        return self._Hour


# Минута
class SETMinute:
    """
    Минута
    """
    _Minute = None

    def __init__(self):
        self._Minute = None

    def add_Minute(self, Minute: int):
        """
        Добавляем Минуты
        :param Minute: Минуты - Формат - 09
        :return:
        """
        if (Minute > 0) and (Minute < 61):

            if Minute > 9:
                Minute = str(Minute)
            else:
                Minute = '0' + str(Minute)
            self._Minute = str(Minute)

    def remove_Minute(self):
        """
        Удаляем Минуты

        """
        self._Minute = None

    def get_Minute(self):
        """
        Берем Минуты

        :return:
        """
        return self._Minute


# Секунда
class SETSecond:
    """
    Секунда
    """
    _Second = None

    def __init__(self):
        self._Second = None

    def add_Second(self, Second: int):
        """
        Добавляем Секунды
        :param Second: Секунды - Формат - 07
        :return:
        """
        if (Second > 0) and (Second < 61):

            if Second > 9:
                Second = str(Second)
            else:
                Second = '0' + str(Second)
            self._Second = str(Second)

    def remove_Second(self):
        """
        Удаляем Секунда

        """
        self._Second = None

    def get_Second(self):
        """
        Берем Секунда

        :return:
        """
        return self._Second


# Часовой Пояс
class SETTimeZone:
    """
    Часовой Пояс
    """
    _TimeZone = None

    def __init__(self):
        self._TimeZone = None

    def add_Time_Zone(self, Time_Zone: str):
        """
        Добавляем Часовой пояс
        :param Time_Zone: Часовой пояс - Формат +03:00
        :return:
        """

        self._TimeZone = str(Time_Zone)

    def remove_Time_Zone(self):
        """
        Удаляем Секунда

        """
        self._TimeZone = None

    def get_Time_Zone(self):
        """
        Берем Секунда

        :return:
        """
        return self._TimeZone


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Actions.Template_SetTime import TemplateSetTime

from JSON_Backend_framework.Devices_USPD.settings import url_path

from JSON_Backend_framework.Service.TemplateDecorator import read_USPD_Time_Request


# -------------------------------------------------------------------------------------------------------------


class SetTime(TemplateSetTime):
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

    Year = SETYear()
    Month = SETMonth()
    Day = SETDay()

    Hour = SETHour()
    Minute = SETMinute()
    Second = SETSecond()

    TimeZone = SETTimeZone()

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

        Time = StateTime(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address).Time_USPD_Read()

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
        return data

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# data =  {"time": "2007-10-15T01:33:25+10:00"}
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
