# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле MeterDeviceManagement
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.TemplateUSPD import Template_UM_XX_SMART_MeterDeviceManagement


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

    # ----->
    def _RelayControl(self):
        """
        Состояние линий питания интерфейсов
        """
        from Devices_USPD.UM40.Functional.Action.Set_Time_setting import SetTime
        Time = SetTime(
                        cookies=self._cookies,
                        headers=self._headers,
                        ip_address=self._ip_address
                      )
        return Time

    def _MeterTimeControl(self):
        """
        Текущее время СЧЕТЧИКА

        """
        from Devices_USPD.UM40.Functional.Action.Device_Restart import DeviceRestart
        Restart = DeviceRestart(
                                cookies=self._cookies,
                                headers=self._headers,
                                ip_address=self._ip_address
                               )
        return Restart
