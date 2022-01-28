# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                     Настройки локального времени(Часовой пояс)
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



class SettingsSetTime:
    """

    Собираем в общий JSON

    """
    _Time_Tag = "time"
    _Time_Set_dict = {}
    _Time_string = None
    # Общие настройки

    Year = SETYear()
    Month = SETMonth()
    Day = SETDay()

    Hour = SETHour()
    Minute = SETMinute()
    Second = SETSecond()
    TimeZone = SETTimeZone()

    def __init__(self):
        self._Settings = {}
        self._Time_Set_dict = {}
        self._date_time_now()

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

    def get_TimeZone(self):

        """
        Получаем собранный JSON
        """
        SetTime = self._Time_Set_dict

        # Получаем наши значения
        Year = self.Year.get_Year()
        Month = self.Month.get_Month()
        Day = self.Day.get_Day()
        Hour = self.Hour.get_Hour()
        Minute = self.Minute.get_Minute()
        Second = self.Second.get_Second()
        Time_Zone = self.TimeZone.get_Time_Zone()

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

        Year = SetTime['Year']
        Month = SetTime['Month']
        Day = SetTime['Day']
        Hour = SetTime['Hour']
        Minute = SetTime['Minute']
        Second = SetTime['Second']
        Time_Zone = SetTime['Time_Zone']
        # Теперь собираем в единую стрингу
        self._Time_string = Year + '-' + Month + '-' + Day + 'T' + Hour + ':' + Minute + ':' + Second + Time_Zone

        data = {self._Time_Tag: self._Time_string}

        return data