# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 31 СМАРТ - Поле Settings
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_Settings


class UM_31_SMART_Settings(Template_UM_XX_SMART_Settings):
    """
    Саб класс который работает с настройками УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Таблица приборов учета , Настройки хранения архивных данных приборов учета
    Meter = None
    # Файловая система
    DeviceSettings = None

    # Система событий
    EventSystem = None

    # Настройки модема
    Modem = None

    # Настройки Серверов
    Servers = None

    # Настройки протокола
    Proto = None

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

        self.Meter = self._Settings_Meter()
        self.Modem = self._Settings_Modem()
        self.Servers = self._Settings_Servers()
        self.EventSystem = self._Settings_EventSystem()
        self.DeviceSettings = self._Settings_DeviceSettings()
        self.Proto = self._Settings_Proto()

    def _Settings_Meter(self):
        """
        Таблица приборов учета

        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.Meter import SettingsMeter
        # Определяем настройки
        Settings_Meter = SettingsMeter(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Settings_Meter

    def _Settings_Modem(self):
        """
        Настройки Модема

        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.Modem import SettingsModem
        # Определяем настройки
        Modem = SettingsModem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Modem

    def _Settings_Servers(self):
        """

        Настройки Сервера

        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.Servers import SettingsServers
        # Определяем настройки
        Servers = SettingsServers(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Servers

    def _Settings_EventSystem(self):
        """

        Настройки Системы событий

        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.EventSystem import SettingsEventSystem
        # Определяем настройки
        Servers = SettingsEventSystem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Servers

    def _Settings_DeviceSettings(self):
        """

        Настройки Самого прибора учета

        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.DeviceSettings import DeviceSettings
        # Определяем настройки
        Device = DeviceSettings(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Device

    def _Settings_Proto(self):
        """

        Настройки протоколов обмена
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.Settings.Proto import SettingsProto
        # Определяем настройки
        Proto = SettingsProto(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Proto
