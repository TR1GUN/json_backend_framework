# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Meter
# -------------------------------------------------------------------------------------------------------------

class SettingsMeter:
    _cookies = None
    _headers = None
    _ip_address = None

    # Таблица приборов учета
    Table = None
    # Настройки хранения архивных данных приборов учета
    # ArchInfo = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # Обновляем функционал
        # ---->
        self._define_functionality()

    def _define_functionality(self):
        """
        Получение функционала
        """

        # Обновляем функционал
        # Таблица приборов учета
        self.Table = self._Meter_Table()
        # Настройки хранения архивных данных приборов учета
        # self.ArchInfo = self._Meter_Arch()

    # Таблица приборов учета
    def _Meter_Table(self):
        """
        Таблица приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.Meter.MeterTable import MeterTable
        Table = MeterTable(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Table

    # # Настройки хранения архивных данных приборов учета
    # def _Meter_Arch(self):
    #     """
    #     Настройки хранения архивных данных приборов учета
    #     :return:
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.Meter.MeterArchInfo import MeterArchInfo
    #
    #     ArchInfo = MeterArchInfo(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return ArchInfo