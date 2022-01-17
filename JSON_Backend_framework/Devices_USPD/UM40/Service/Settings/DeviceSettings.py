# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.DeviceSettings
# -------------------------------------------------------------------------------------------------------------

class DeviceSettings:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки Ethernet
    Interface_Ethernet = None
    # Настройки последовательных интерфейсов(UART)
    Interface_UART = None
    # Настройки дискретных входов

    # Настройки линий питания интерфейсов
    Interface_DOut = None
    # Настройки локального времени
    Time_Local = None
    # Настройки доступа к файловой системе

    # Настройки имени устройства

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        self.Interface_Ethernet = self._Generate_Ethernet()
        self.Interface_UART = self._Generate_UART()
        self.Interface_DOut = self._Generate_DOut()
        self.Time_Local = self._Generate_Time_Local()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Настройки Ethernet
    def _Generate_Ethernet(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.DeviceSettings.Interface_Ethernet import Interface_Ethernet
        Ethernet = Interface_Ethernet(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Ethernet

    # ГЕНЕРИРУЕМ Настройки последовательных интерфейсов(UART)
    def _Generate_UART(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.DeviceSettings.Interface_UART import Interface_UART

        UART = Interface_UART(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return UART

    # ГЕНЕРИРУЕМ Настройки Питания линий интерфейсов
    def _Generate_DOut(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.DeviceSettings.Interface_DOut import Interface_DOut_PowerLine

        PowerLine = Interface_DOut_PowerLine(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return PowerLine

    # ГЕНЕРИРУЕМ Настройки часового пояса
    def _Generate_Time_Local(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.DeviceSettings.Local_Time import TimeZone

        LocalTime = TimeZone(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return LocalTime