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

        self.Activate = self._Generate_Activate()
        self.Name = self._Generate_Name()
        self.Season = self._Generate_Season()
        self.Week = self._Generate_Week()
        self.Day = self._Generate_Day()
        self.Time = self._Generate_Time()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Активация тарифного расписания
    def _Generate_Activate(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Activate import CalendarActivate

        Calendar_Activate = CalendarActivate(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Activate

    # ГЕНЕРИРУЕМ Имя календаря тарифного расписания
    def _Generate_Name(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Name import CalendarName

        Calendar_Name = CalendarName(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Name

    # ГЕНЕРИРУЕМ Сезонный профиль тарифного расписания
    def _Generate_Season(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Season import CalendarSeason

        Calendar_Season = CalendarSeason(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Season

    # ГЕНЕРИРУЕМ Недельный профиль тарифного расписания
    def _Generate_Week(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Week import CalendarWeek

        Calendar_Week = CalendarWeek(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Week

    # ГЕНЕРИРУЕМ Суточный профиль тарифного расписания
    def _Generate_Day(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Day import CalendarDay

        Calendar_Day = CalendarDay(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Day

    # ГЕНЕРИРУЕМ Дата активации тарифного расписания
    def _Generate_Time(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterDeviceManagement.Calendar.Time import CalendarTime

        Calendar_Time = CalendarTime(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Calendar_Time