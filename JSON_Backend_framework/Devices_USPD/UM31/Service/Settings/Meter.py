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
    ArchInfo = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        self.Table = self._Meter_Table()
        self.ArchInfo = self._Meter_Arch()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Meter_Table(self):
        """
        Таблица приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Meter.MeterTable import MeterTable
        Table = MeterTable(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Table

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Meter_Arch(self):
        """
        Настройки хранения архивных данных приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Meter.MeterArchInfo import MeterArchInfo

        ArchInfo = MeterArchInfo(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return ArchInfo
