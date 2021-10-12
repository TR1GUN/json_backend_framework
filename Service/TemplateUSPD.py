# Здесь расположим Шаблоны USPD
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            ШАБЛОН Прибора учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class Template_USPD:
    """
    класс - интерфейс от которого наследуются классы УСПД
    """
    # Переменные нужные для авторизации
    # Логин
    _Login = ''
    # Пароль
    _Password = ''

    # Куки
    _cookies = None
    # headers - заголовки
    _headers = None
    # IP Адрес
    _ip_address = None

    # Поля Необходимые для доступа
    # Настройки
    Settings = None
    Actions = None
    USPD = None
    MeterDevices = None

    @staticmethod
    def _IP_address_from_config():
        """
        Получаем IP адрес из конфига .ini
        :return:
        """
        from Service.config import machine_ip

        return str(machine_ip)

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу
        :return:
        """


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            ШАБЛОН Графы НАСТРОЕК у прибора учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class Template_UM_XX_SMART_Settings:
    """
    Саб класс который работает с настройками УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Настройки Ethernet
    Ethernet = None
    # Настройки линий питания интерфейсов
    Interface_power_line = None
    # Настройки локального времени
    Local_time = None
    # Настройки SIM-карт (Pin, APN)
    SIM_card = None

    # Клиенты и серверы
    # Настройки TCP-серверов
    TCP_server = None
    # Настройки SNTP-серверов
    SNTP_server = None

    # Приборы учета
    # Таблица приборов учета
    Meter_Table = None

    # Система событий
    # Настройки менеджера системы событий
    Event_Manager = None
    # Настройки шаблонов приборов учета
    Meter_device_template = None
    # Настройки шаблонов данных приборов учета
    Meter_device_data_template = None
    # Настройки расписаний
    Schedule_settings = None
    # Настройки регулярного опроса приборов учета
    Polling_of_meter_device = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # Теперь обновляем
        self.Ethernet = self._Ethernet()
        self.Interface_Power_Line = self._Interface_Power_Line()

        # Настройки локального времени
        self.Local_time = self._Local_Time()
        # Настройки SIM-карт (Pin, APN)
        self.SIM_card = self._SIM_card()

        # Клиенты и серверы
        # Настройки TCP-серверов
        self.TCP_server = self._TCP_server()
        # Настройки SNTP-серверов
        self.SNTP_server = self._SNTP_server()

        # Приборы учета
        # Таблица приборов учета
        self.Meter_Table = self._Meter_Table()

        # Система событий
        # Настройки менеджера системы событий
        self.Event_Manager = self._Event_Manager()
        # Настройки шаблонов приборов учета
        self.Meter_device_template = self._Meter_device_template()
        # Настройки шаблонов данных приборов учета
        self.Meter_device_data_template = self._Meter_device_data_template()
        # Настройки расписаний
        self.Schedule_settings = self._Schedule_settings()
        # Настройки регулярного опроса приборов учета
        self.Polling_of_meter_device = self._Polling_of_meter_device()

    def _Ethernet(self):
        from Devices_USPD.Devices_Functions.Settings.Ethernet_settings import EthernetSettings

        return EthernetSettings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Interface_Power_Line(self):
        from Devices_USPD.Devices_Functions.Settings.Interface_power_line_settings import InterfacePowerLine

        return InterfacePowerLine(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Local_Time(self):
        from Devices_USPD.Devices_Functions.Settings.Local_time_settings import LocalTime

        return LocalTime(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _SIM_card(self):
        from Devices_USPD.Devices_Functions.Settings.SIM_card_settings import SIM_card

        return SIM_card(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _TCP_server(self):
        from Devices_USPD.Devices_Functions.Settings.TCP_server_settings import TCP_server

        return TCP_server(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _SNTP_server(self):
        from Devices_USPD.Devices_Functions.Settings.SNTP_server_settings import SNTP_server

        return SNTP_server(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Meter_Table(self):
        from Devices_USPD.Devices_Functions.UM40.MeterDevice.MeterDevice_Table import MeteringDeviceTable

        return MeteringDeviceTable(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Event_Manager(self):
        from Devices_USPD.Devices_Functions.Settings.Event_Manager_Settings import EventManager

        return EventManager(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Meter_device_template(self):
        from Devices_USPD.Devices_Functions.Settings.Metering_device_templates_settings import MeteringDeviceTemplates

        return MeteringDeviceTemplates(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Meter_device_data_template(self):
        from Devices_USPD.Devices_Functions.Settings.Settings_for_metering_devices_data_templates import \
            SettingsForMeteringDevicesDataTemplates

        return SettingsForMeteringDevicesDataTemplates(cookies=self._cookies, headers=self._headers,
                                                       ip_address=self._ip_address)

    def _Schedule_settings(self):
        from Devices_USPD.Devices_Functions.Settings.Schedule_settings import Schedule

        return Schedule(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Polling_of_meter_device(self):
        from Devices_USPD.Devices_Functions.Settings.Settings_for_regular_polling_of_metering_devices import \
            SettingsForRegularPollingOfMeteringDevices

        return SettingsForRegularPollingOfMeteringDevices(cookies=self._cookies, headers=self._headers,
                                                          ip_address=self._ip_address)



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            ШАБЛОН Графы данных счетчика
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class Template_UM_XX_SMART_Meter:
    """
    Саб класс который работает с данными счетчиков УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал

    MeterData_Arch = None
    MeterData_Moment = None

    Meter_RelayControl = None
    Meter_TimeSetting = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # Теперь обновляем
        self.MeterData_Arch = self._Meter_data_arch()
        self.MeterData_Moment = self._Meter_data_moment()

        self.Meter_RelayControl = self._RelayControl()
        self.Meter_TimeSetting = self._TimeSetting()


    def _Meter_data_arch(self):
        from Devices_USPD.Devices_Functions.MeterData.Meter_Data_arch import MeterDataArch

        return MeterDataArch(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Meter_data_moment(self):
        from Devices_USPD.Devices_Functions.MeterData.Meter_Data_moment import MeterDataMoment

        return MeterDataMoment(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _RelayControl(self):
        from Devices_USPD.Devices_Functions.MeterManagement.Relay_control import RelayControl

        return RelayControl(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _TimeSetting(self):
        from Devices_USPD.Devices_Functions.MeterManagement.Time_setting import TimeSetting

        return TimeSetting(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            ШАБЛОН управления УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------



class Template_UM_XX_SMART_USPD:
    """
    Саб класс который работает с данными счетчиков УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал

    Set_Time = None
    Current_Time = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # Теперь обновляем

        self.Set_Time = self._Set_Time()

        self.Current_Time = self._Current_Time()


    def _Current_Time(self):
        from Devices_USPD.Devices_Functions.StatusInformation.Current_time import CurrentTime

        return CurrentTime(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


    def _Set_Time(self):
        from Devices_USPD.Devices_Functions.Actions.Set_Time_setting import SetTimeSetting

        return SetTimeSetting(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)