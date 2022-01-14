# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки для Ethernet
# -------------------------------------------------------------------------------------------------------------

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
#                                         Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_Ethernet_settings import TemplateInterface_Ethernet

# -------------------------------------------------------------------------------------------------------------


class Interface_Ethernet(TemplateInterface_Ethernet):
    """
    Настройки Ethernet

    """
    from Service.TemplateDecorator import print_log_use_GET_data
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    SettingsEthernet = SettingsEthernet()

    # Настройки по умолчанию

    # Настройки Ethernet
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

    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса -
        Здесь переопределяем

        """
        data = self._getting_settings_Ethernet()
        data = {'Settings': data}
        return data

    def _getting_settings_Ethernet(self):

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
        JSON = [Ethernet1, Ethernet2]
        return JSON

    # Запрос настроек
    @print_log_use_GET_data
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
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {'Settings': [
#                      {'iface': 'eth0', 'dhcp': False, 'ip': '', 'netmask': '', 'gw': '', 'dns1': '', 'dns2': ''},
#                      {'iface': 'eth1', 'dhcp': True, 'ip': '', 'netmask': '', 'gw': '', 'dns1': '', 'dns2': ''}
#                     ]}
# -------------------------------------------------------------------------------------------------------------
