# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
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

    @staticmethod
    def _IP_address_from_config():
        """
        Получаем IP адрес из конфига .ini
        :return:
        """
        from Service.config import machine_ip

        return str(machine_ip)


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

    Settings = {}

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


class UM_31_SMART_Settings:
    """
    Саб класс который работает с настройками УСПД
    """

    _cookies = None
    _headers = None
    _ip_address = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

    def Ethernet(self):
        from Devices_USPD.Devices_Functions.Ethernet_settings import EthernetSettings

        return EthernetSettings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


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

    def Ethernet_settings(self):
        """
        Настройки Ethernet

        :return:
        """
        from Devices_USPD.Devices_Functions.Ethernet_settings import EthernetSettings

        return EthernetSettings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
