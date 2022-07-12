# -------------------------------------------------------------------------------------------------------------
#                                     Поле MeterDeviceManagement.Calendar
#                                         Тарифное расписание
# -------------------------------------------------------------------------------------------------------------

class MeterDeviceManagementCalendar:
    _cookies = None
    _headers = None
    _ip_address = None

    # // Активация тарифного расписания
    Activate = None

    # // Имя календаря тарифного расписания
    Name = None

    # // Сезонный профиль тарифного расписания
    Season = None

    # // Недельный профиль тарифного расписания
    Week = None

    # // Суточный профиль тарифного расписания
    Day = None

    # // Дата активации тарифного расписания
    Time = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address
        # ---->

        self._define_functionality()

    def _define_functionality(self):
        """

        Получение функционала

        """
        # Активация тарифного расписания
        self.Activate = self._Calendar_Activate()
        # Имя календаря тарифного расписания
        self.Name = self._Calendar_Name()
        # Сезонный профиль тарифного расписания
        self.Season = self._Calendar_Season()
        # Недельный профиль тарифного расписания
        self.Week = self._Calendar_Week()
        # Суточный профиль тарифного расписания
        self.Day = self._Calendar_Day()
        # Дата активации тарифного расписания
        self.Time = self._Calendar_Time()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Активация тарифного расписания
    def _Calendar_Activate(self):
        """
        Активация тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Activate import CalendarActivate

        Calendar_Activate = CalendarActivate(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Activate

    # ГЕНЕРИРУЕМ Имя календаря тарифного расписания
    def _Calendar_Name(self):
        """
        Имя календаря тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Name import CalendarName

        Calendar_Name = CalendarName(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Name

    # ГЕНЕРИРУЕМ Сезонный профиль тарифного расписания
    def _Calendar_Season(self):
        """
        Сезонный профиль тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Season import CalendarSeason

        Calendar_Season = CalendarSeason(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Season

    # ГЕНЕРИРУЕМ Недельный профиль тарифного расписания
    def _Calendar_Week(self):
        """
        Недельный профиль тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Week import CalendarWeek

        Calendar_Week = CalendarWeek(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Week

    # ГЕНЕРИРУЕМ Суточный профиль тарифного расписания
    def _Calendar_Day(self):
        """
        Суточный профиль тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Day import CalendarDay

        Calendar_Day = CalendarDay(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Day

    # ГЕНЕРИРУЕМ Дата активации тарифного расписания
    def _Calendar_Time(self):
        """
        Дата активации тарифного расписания
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.Calendar.Time import CalendarTime

        Calendar_Time = CalendarTime(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Time