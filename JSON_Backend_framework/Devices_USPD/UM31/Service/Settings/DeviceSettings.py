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
    Interface_DIn = None
    # Настройки линий питания интерфейсов
    Interface_DOut = None
    # Настройки локального времени
    Time_Local = None
    # Настройки доступа к файловой системе
    FileSystem = None
    # Настройки имени устройства
    Name = None

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
        # Настройки Ethernet
        self.Interface_Ethernet = self._DeviceSettings_Interface_Ethernet()
        # Настройки последовательных интерфейсов(UART)
        self.Interface_UART = self._DeviceSettings_Interface_UART()
        # Настройки дискретных входов
        self.Interface_DIn = self._DeviceSettings_Interface_DIn()
        # Настройки линий питания интерфейсов
        self.Interface_DOut = self._DeviceSettings_Interface_DOut()
        # Настройки локального времени
        self.Time_Local = self._DeviceSettings_Time_Local()
        # Настройки доступа к файловой системе
        self.FileSystem = self._DeviceSettings_FileSystem()
        # Настройки имени устройства
        self.Name = self._DeviceSettings_Name()

    # Здесь генерируем сам функционал :
    # Настройки Ethernet
    def _DeviceSettings_Interface_Ethernet(self):
        """
        Настройки Ethernet
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Interface_Ethernet import \
            Interface_Ethernet
        Ethernet = Interface_Ethernet(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Ethernet

    # Настройки последовательных интерфейсов(UART)
    def _DeviceSettings_Interface_UART(self):
        """
        Настройки последовательных интерфейсов(UART)
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Interface_UART import Interface_UART

        UART = Interface_UART(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return UART

    # Настройки дискретных входов
    def _DeviceSettings_Interface_DIn(self):
        """
        Настройки дискретных входов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Interface_DIn import Interface_DIn_DiscreteInput

        DiscreteInput = Interface_DIn_DiscreteInput(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DiscreteInput

    # Настройки линий питания интерфейсов
    def _DeviceSettings_Interface_DOut(self):
        """
        Настройки линий питания интерфейсов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Interface_DOut import Interface_DOut_PowerLine

        PowerLine = Interface_DOut_PowerLine(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return PowerLine

    # Настройки локального времени
    def _DeviceSettings_Time_Local(self):
        """
        Настройки локального времени
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Local_Time import TimeZone

        LocalTime = TimeZone(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return LocalTime

    # Настройки доступа к файловой системе
    def _DeviceSettings_FileSystem(self):
        """
        Настройки доступа к файловой системе
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.FileSystem_Access import FileSystemAccess

        FileSystem = FileSystemAccess(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return FileSystem

    # Настройки имени устройства
    def _DeviceSettings_Name(self):
        """
        Настройки имени устройства
        :return:
        """

        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.DeviceSettings.Name import \
            Name

        NameUSPD = Name(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return NameUSPD
