# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле MeterDeviceManagement
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_MeterDeviceManagement


class UM_40_SMART_MeterDeviceManagement(Template_UM_XX_SMART_MeterDeviceManagement):
    """

    Саб класс который работает с разделом УСПД :  Управление приборами учета

    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Управление реле
    Relay = None
    # Установка времени – Системное время счетчика
    Set_Time_Meter = None

    # Tарифное расписание
    Calendar = None

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

        self.Relay = self._RelayControl()
        self.Set_Time_Meter = self._MeterTimeControl()
        self.Calendar = self._Calendar()

    # ----->
    def _RelayControl(self):
        """
        Состояние линий питания интерфейсов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.RelayControl import RelayControl
        Relay = RelayControl(
                        cookies=self._cookies,
                        headers=self._headers,
                        ip_address=self._ip_address
                      )
        return Relay

    def _MeterTimeControl(self):
        """
        Текущее время СЧЕТЧИКА

        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterDeviceManagement.MeterTime import TimeMeterSetting
        TimeMeter = TimeMeterSetting(
                                cookies=self._cookies,
                                headers=self._headers,
                                ip_address=self._ip_address
                               )
        return TimeMeter

    def _Calendar(self):
        """
        Тарифное расписание

        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.Calendar.Calendar import MeterDeviceManagementCalendar
        Calendar = MeterDeviceManagementCalendar(
                                cookies=self._cookies,
                                headers=self._headers,
                                ip_address=self._ip_address
                               )
        return Calendar
