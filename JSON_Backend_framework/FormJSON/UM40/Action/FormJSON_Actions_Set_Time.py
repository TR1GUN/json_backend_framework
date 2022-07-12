# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                     Настройки локального времени(Часовой пояс)
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
#                                         Основной класс
# -------------------------------------------------------------------------------------------------------------


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

    def get_Time(self):

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