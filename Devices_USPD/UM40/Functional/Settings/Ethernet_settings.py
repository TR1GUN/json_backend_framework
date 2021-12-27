# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class EthernetSettings(TemplateFunctional):
    """
    Настройки Ethernet

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Ethernet_settings")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    Ethernet_Settings = None

    _settings_to_send = {}

    _eth0 = None
    _eth1 = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки Ethernet

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response

    # Итак - Здесь инициализируем наши настройки
    def _settings(self):

        """ Здесь делаем наши настройки """

        self.Ethernet_Settings = SettingsEthernet()
        self._settings_to_send = self._read_settings_by_send()

    def _read_settings_by_send(self):
        """
        Читаем данные - GET
        :return:
        """
        JSON_response = {'Settings': [
            {'iface': 'eth0', 'dhcp': False, 'ip': '', 'netmask': '', 'gw': '', 'dns1': '', 'dns2': ''},
            {'iface': 'eth1', 'dhcp': True, 'ip': '', 'netmask': '', 'gw': '', 'dns1': '', 'dns2': ''}
                            ]}

        try:
            # делаем запрос - получаем ответ
            response = self.read_settings()

            response = response.get('data')
            # ====>
            # Продолжаем если все ОК
            if response is not None :
                Settings = response['Settings']
                # Теперь перебираем все это
                for eth in Settings :
                    if eth.get('iface') == 'eth0':
                        self._eth0 = eth
                    if eth.get('iface') == 'eth1':
                        self._eth1 = eth

        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

            response = JSON_response

        return response

    def send_data(self):
        """
        Отправка введенных данных
        :return:
        """

        # Сна дача считываем данные

        settings_to_send = self._settings_to_send

        # Потом проверяем ккакие данные заданы

        ifaces = []
        settings_Eth_0 = self.Ethernet_Settings.settings_Eth_0()
        settings_Eth_1 = self.Ethernet_Settings.settings_Eth_1()

        # Проверяем интерфейсы - если они заданы - добалвяем их
        if settings_Eth_0 is not None :
            ifaces.append(settings_Eth_0)
        else:
            ifaces.append(self._eth0)

        if settings_Eth_1 is not None :
            ifaces.append(settings_Eth_1)
        else:
            ifaces.append(self._eth1)

        # Теперь формируем из этого JSON

        JSON = {'Settings':ifaces}

        # И теперь отправляем

        response = self.rewrite_settings(data=JSON)

        return response


class SettingsEthernet:
    """

    Итак - Здесь заполняем настройки

    """

    _Setting_Eth0 = None
    _Setting_Eth1 = None

    def __init__(self):
        self._Setting_Eth0 = None
        self._Setting_Eth1 = None

    def added_Eth_0(self, dhcp: bool, ip: str, netmask: str, gateway: str, dns1: str, dns2: str):
        """
        Настройки интерфейса Ethernet 1

        :param dhcp: - bool - Настройки DHCP
        :param ip: - str - Настройки IP адреса
        :param netmask: - str - Маска подсети
        :param gateway: - str - Шлюз
        :param dns1: - str - DNS Первичный Сервер
        :param dns2: - str - DNS Вторичный Сервер
        :return:
        """

        _Setting_Eth0 = \
            {
                'iface': 'eth0',
                'dhcp': bool(dhcp),
                'ip': ip,
                'netmask': netmask,
                'gw': gateway,
                'dns1': dns1,
                'dns2': dns2,
            }

        self._Setting_Eth0 = _Setting_Eth0

    def remove_Eth_0(self):
        """
        Удаление настроек интерфейса Ethernet 1, что ввели
        :return:
        """

        self._Setting_Eth0 = None

    def added_Eth_1(self, dhcp: bool, ip: str, netmask: str, gateway: str, dns1: str, dns2: str):
        """
        Настройки интерфейса Ethernet 2

        :param dhcp: - bool - Настройки DHCP
        :param ip: - str - Настройки IP адреса
        :param netmask: - str - Маска подсети
        :param gateway: - str - Шлюз
        :param dns1: - str - DNS Первичный Сервер
        :param dns2: - str - DNS Вторичный Сервер
        :return:
        """

        _Setting_Eth1 = \
            {
                'iface': 'eth1',
                'dhcp': bool(dhcp),
                'ip': ip,
                'netmask': netmask,
                'gw': gateway,
                'dns1': dns1,
                'dns2': dns2,
            }

        self._Setting_Eth1 = _Setting_Eth1

    def remove_Eth_1(self):
        """
        Удаление настроек интерфейса Ethernet 2, что ввели
        :return:
        """

        self._Setting_Eth1 = None

    def settings_Eth_0(self):
        """
        Получить настройки Ethernet 0
        :return:
        """

        return self._Setting_Eth0

    def settings_Eth_1(self):
        """
        Получить настройки Ethernet 1
        :return:
        """

        return self._Setting_Eth1


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from Service.Template_Functional import TemplateFunctional


class Ethernet(TemplateFunctional):

    """
    Настройки Ethernet

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Ethernet_settings")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    SettingsEthernet = SettingsEthernet()

    # Настройки по умолчанию



    # Настройки сим карт
    _Eth0 = {'iface': 'eth0', 'dhcp': False, 'ip': '192.168.0.1', 'netmask': '255.255.255.1', 'gw': '', 'dns1': '', 'dns2': ''}

    _Eth1 = {'iface': 'eth1', 'dhcp': True, 'ip': '', 'netmask': '', 'gw': '', 'dns1': '', 'dns2': ''}

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки Ethernet

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)

        # Обьявляем наш класс настроек
        # SettingsEthernet = SettingsEthernet()

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        if data is None:
            data_settings = self._getting_settings()
            data = {'Settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data=None):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        if data is None:
            data_settings = self._getting_settings()
            data = {'Settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response

    # Здесь расположим сервисные функции
    # Первое - Получаем настройки что уже есть

    def _getting_settings(self):

        """

        Получение настроек что задали

        """

        # Пункт первый -  читаем какие настройки у нас есть
        Ethernet1 = self.SettingsEthernet.settings_Eth_0()
        Ethernet2 = self.SettingsEthernet.settings_Eth_1()

        # ТЕПЕРЬ, если у нас оба сейтинга не заданы , запрашиваем :
        if (Ethernet1 is None) or (Ethernet2 is None):
            _Ethernet1, _Ethernet2 = self._request_setting()
            # Теперь смотрим точно что необходимо переназначить
            if Ethernet1 is None:
                # Теперь смотрим что считали
                if _Ethernet1 is None:
                    Ethernet1 = self._Eth0
                else:
                    Ethernet1 = _Ethernet1
            if Ethernet2 is None:
                # Теперь смотрим что считали
                if _Ethernet2 is None:
                    Ethernet2 = self._Eth1
                else:
                    Ethernet2 = _Ethernet2

        # Теперь формируем нужный JSON
        # JSON = {"Settings" : [SIM1, SIM2]}
        JSON = [Ethernet1, Ethernet2]
        return JSON

    # Запрос настроек
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        _Eth0 = None
        _Eth1 = None
        try:
            # делаем запрос - получаем ответ
            response = self.read_settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                sim_setting = response.get('data')
                # Теперь заполянем наши переменные
                if sim_setting is not None:

                    # print(sim_setting)
                    Settings = sim_setting['Settings']
                    # Теперь перебираем все это
                    for idx in Settings:
                        if idx.get('iface') == 'eth0':
                            _Eth0 = idx
                        if idx.get('iface') == 'eth1':
                            _Eth1 = idx

        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return _Eth0, _Eth1


# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {'Settings': [
#     {'id': 1, 'pin': '', 'addr': 'internet.beeline.ru', 'auth': False, 'login': 'beeline', 'password': 'beeline',
#      'enable': True},
#     {'id': 2, 'pin': '2527', 'addr': 'internet.beeline.ru', 'auth': True, 'login': 'beeline', 'password': 'beeline',
#      'enable': True}]}
# -------------------------------------------------------------------------------------------------------------

# lol = Ethernet().read_settings()
#
# lol = Ethernet().write_settings(data=None)
# print(lol)