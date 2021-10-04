# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# импортируем наши классы

from Service.TemplateUSPD import Template_USPD, \
                                 Template_UM_XX_SMART_Settings, \
                                 Template_UM_XX_SMART_USPD, \
                                 Template_UM_XX_SMART_Meter


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 31 СМАРТ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class UM_31_SMART(Template_USPD):
    """
    Функционал УМ - 31 СМАРТ

    """
    # Переменные нужные для авторизации
    # Логин
    _Login = 'admin'
    # Пароль
    _Password = 'admin'
    # IP адрес УСПД
    _ip_address = 'localhost'

    # Поля Необходимые для доступа
    # Настройки
    Settings = None

    def __init__(self, Login: str = 'admin', Password: str = 'admin', ip_address=None):
        """
        Функционал УМ - 31 СМАРТ

        :param Login: Логин - стоит значение по умолчанию
        :param Password: Пароль - Стоит значение по умолчанию
        :param ip_address: IP адрес УСПД - Если не заданно - Берется из файла ini
        """
        # Куки - Перед началом работы обнуляем их
        self._cookies = None

        # Теперь - если не пустота - то перезаписываем
        if Login is not None:
            self._Login = str(Login)
        # Теперь - если не пустота - то перезаписываем
        if Password is not None:
            self._Password = str(Password)

        # Устанавливаем IP адрес если его дали
        if ip_address is not None:
            self._ip_address = str(ip_address)
        # Иначе - Используем адрес из настроек
        else:
            self._ip_address = self._IP_address_from_config()

        # А Теперь - авторизуемся
        self._Authorization()

        # И обновляем функционал
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу
        :return:
        """
        # Обновляем Настройки
        self._Settings()

    # АВТОРИАЗЦИЯ - должна происходить автоматически - при протухании кукис - перелогиниваться
    def _Authorization(self):
        """
        Метод Авторизации - для УМ 31 смарт
        :return:
        """
        from Devices_USPD.Authorization import Authorization

        Authorization_cookie = Authorization(Login=str(self._Login),
                                             Password=str(self._Password),
                                             ip_address=str(self._ip_address))

        # Если авториазия была успешна

        if Authorization_cookie.result_code == 200:
            self._cookies = Authorization_cookie.get_cookies()
        else:
            print('Авторизация - не выполнено')

            assert Authorization_cookie.result_code == 200, Authorization_cookie.get_result()

    def _Settings(self):
        """
        Получаем Класс который работает с настройками УСПД
        :return:
        """
        self.Settings = UM_31_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


class UM_31_SMART_Settings(Template_UM_XX_SMART_Settings):
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

    # def __init__(self, cookies=None, headers=None, ip_address=None):
    #     self._cookies = cookies
    #     self._headers = headers
    #     self._ip_address = ip_address
    #
    #     # Теперь обновляем
    #     self.Ethernet = self._Ethernet()

    # def _Ethernet(self):
    #     from Devices_USPD.Devices_Functions.Ethernet_settings import EthernetSettings
    #
    #     return EthernetSettings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class UM_40_SMART(Template_USPD):
    """
    Функционал УМ - 40 СМАРТ

    """
    # IP Адрес
    from Service.config import machine_ip
    ip_address = str(machine_ip)

    def __init__(self, ip_address=None):
        """
        Получаем функционал доступный в УМ-40 СМАРТ

        :param ip_address: IP адрес УСПД. Значение по умолчанию - None - Используется значение из файла settings.ini
        """
        # Устанавливаем IP адрес если его дали
        if ip_address is not None:
            self._ip_address = str(ip_address)
        # Иначе - Используем адрес из настроек
        else:
            self._ip_address = self._IP_address_from_config()

        # И обновляем функционал
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу
        :return:
        """
        # Обновляем Настройки
        self._Settings()

    def _Settings(self):
        """
        Получаем Класс который работает с настройками УСПД
        :return:
        """
        self.Settings = UM_40_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.USPD = UM_40_SMART_USPD(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.MeterDevices = UM_40_SMART_Meter(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


# Настройки
class UM_40_SMART_Settings(Template_UM_XX_SMART_Settings):
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

    # def __init__(self, cookies=None, headers=None, ip_address=None):
    #     self._cookies = cookies
    #     self._headers = headers
    #     self._ip_address = ip_address
    #
    #     # Теперь обновляем
    #     self.Ethernet = self._Ethernet()
    #
    # def _Ethernet(self):
    #     from Devices_USPD.Devices_Functions.Ethernet_settings import EthernetSettings
    #
    #     return EthernetSettings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


class UM_40_SMART_Meter(Template_UM_XX_SMART_Meter):
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


class UM_40_SMART_USPD(Template_UM_XX_SMART_USPD):
    """
    Саб класс который работает с данными счетчиков УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал

    Set_Time = None
    Current_Time = None
