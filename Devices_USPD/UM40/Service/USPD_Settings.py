# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле Settings
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.TemplateUSPD import Template_UM_XX_SMART_Settings


class UM_40_SMART_Settings(Template_UM_XX_SMART_Settings):
    """
    Саб класс который работает с настройками УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Таблица приборов учета , Настройки хранения архивных данных приборов учета
    Meter = None
    # # Настройки Ethernet
    Ethernet = None
    # Настройки модема
    Modem = None
    # # Настройки линий питания интерфейсов
    # Interface_power_line = None
    # # Настройки локального времени
    # Local_time = None
    # Настройки SIM-карт (Pin, APN)
    # SIM_card = None
    #
    # # Клиенты и серверы
    # # Настройки TCP-серверов
    # TCP_server = None
    # # Настройки SNTP-серверов
    # SNTP_server = None
    #
    # # Приборы учета
    # # Таблица приборов учета
    # Meter_Table = None
    #
    # # Система событий
    # # Настройки менеджера системы событий
    # Event_Manager = None
    # # Настройки шаблонов приборов учета
    # Meter_device_template = None
    # # Настройки шаблонов данных приборов учета
    # Meter_device_data_template = None
    # # Настройки расписаний
    # Schedule_settings = None
    # # Настройки регулярного опроса приборов учета
    # Polling_of_meter_device = None

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
        self.Ethernet = self._Settings_Ethernet()
        self.Modem = self._Settings_Modem()

    def _Settings_Meter(self):
        """
        Таблица приборов учета

        """
        from Devices_USPD.UM40.Service.Settings.Meter import SettingsMeter
        # Определяем настройки
        Settings_Meter = SettingsMeter(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Settings_Meter

    def _Settings_Ethernet(self):
        """

        Настройки Ethernet

        """
        from Devices_USPD.UM40.Functional.Settings.Ethernet_settings import EthernetSettings
        # Определяем настройки
        Ethernet_Settings = EthernetSettings(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Ethernet_Settings

    def _Settings_Modem(self):
        """
        Таблица приборов учета

        """
        from Devices_USPD.UM40.Service.Settings.Modem import SettingsModem
        # Определяем настройки
        Modem = SettingsModem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Modem