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
    # Действия
    Action = None

    # USPD = None
    # MeterDevices = None

    # Информация о состоянии изделия
    StateInfo = None
    # Журналы изделия
    Journal = None


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

    # Настройки протокола
    Proto = None
    # Настройки Ethernet
    Ethernet = None
    # Настройки последовательных интерфейсов(UART)
    Uart = None
    # Настройки дискретных входов
    Din = None
    # Настройки линий питания интерфейсов
    Dout = None

    # Настройки локального времени
    Local_time = None
    # Настройки модема
    Modem = None
    # Настройки Серверов
    Servers = None

    # Приборы учета
    # Таблица приборов учета
    Meter = None

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

    # def __init__(self, cookies=None, headers=None, ip_address=None):
    #     self._cookies = cookies
    #     self._headers = headers
    #     self._ip_address = ip_address
    #
    #     # Теперь обновляем
    #     self.Ethernet = self._Ethernet()
    #     self.Interface_Power_Line = self._Interface_Power_Line()
    #
    #     # Настройки локального времени
    #     self.Local_time = self._Local_Time()
    #     # Настройки SIM-карт (Pin, APN)
    #     self.SIM_card = self._SIM_card()
    #
    #     # Клиенты и серверы
    #     # Настройки TCP-серверов
    #     self.TCP_server = self._TCP_server()
    #     # Настройки SNTP-серверов
    #     self.SNTP_server = self._SNTP_server()
    #
    #     # Приборы учета
    #     # Таблица приборов учета
    #     self.Meter_Table = self._Meter_Table()
    #
    #     # Система событий
    #     # Настройки менеджера системы событий
    #     self.Event_Manager = self._Event_Manager()
    #     # Настройки шаблонов приборов учета
    #     self.Meter_device_template = self._Meter_device_template()
    #     # Настройки шаблонов данных приборов учета
    #     self.Meter_device_data_template = self._Meter_device_data_template()
    #     # Настройки расписаний
    #     self.Schedule_settings = self._Schedule_settings()
    #     # Настройки регулярного опроса приборов учета
    #     self.Polling_of_meter_device = self._Polling_of_meter_device()


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            ШАБЛОН Графы НАСТРОЕК у прибора учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class Template_UM_XX_SMART_State:
    """
    Саб класс который работает с разделом УСПД :  Информация о состоянии изделия
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал

    #   Состояние линий питания интерфейсов
    DOut = None
    #   Состояние дискретных входов
    DIn = None
    #   Состояние аналоговых входов
    AIn = None
    # Ожидаемое время срабатывания расписаний
    Scheduler = None
    # 	Состояние последовательных интерфейсов
    UART = None
    #   Состояние сетевых подключений
    Network = None
    # 	Состояние сокетов
    Socket = None
    # 	Состояние микросхем памяти
    DataFlash = None
    # 	Состояние файловой системы
    FileSystem = None
    # 	Состояние модема
    Modem = None
    # 	Состояние операционной системы
    OS = None
    # 	Состояние таблицы приборов учета
    MeterTable = None
    # 	Текущее время
    Time = None
    # Информация о конфигурации системы
    System = None


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
        from Devices_USPD.Devices_Functions.MeterData.Template_Meter_Data_arch import MeterDataArch

        return MeterDataArch(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def _Meter_data_moment(self):
        from Devices_USPD.Devices_Functions.MeterData.Template_Meter_Data_moment import MeterDataMoment

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
