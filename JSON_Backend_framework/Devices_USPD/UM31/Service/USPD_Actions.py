# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 31 СМАРТ - Поле Actions
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_Actions


class UM_31_SMART_Actions(Template_UM_XX_SMART_Actions):
    """
    Саб класс который работает с разделом УСПД :  : Действия
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Перезагрузка
    Restart = None
    # Установка времени – Системное время устройства
    Set_Time = None

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

        # self.Restart = self._Actions_Restart()
        # self.Set_Time = self._Actions_Set_Time()

    def _Actions_Set_Time(self):
        """
        Состояние линий питания интерфейсов
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Action.Set_Time_setting import SetTime
        Time = SetTime(
                        cookies=self._cookies,
                        headers=self._headers,
                        ip_address=self._ip_address
                      )
        return Time

    def _Actions_Restart(self):
        """
        Текущее время

        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Action.Device_Restart import DeviceRestart
        Restart = DeviceRestart(
                                cookies=self._cookies,
                                headers=self._headers,
                                ip_address=self._ip_address
                               )
        return Restart
