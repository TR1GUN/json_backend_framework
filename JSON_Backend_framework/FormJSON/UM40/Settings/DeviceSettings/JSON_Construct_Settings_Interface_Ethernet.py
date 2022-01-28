# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                               Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
class SettingsEthernet:
    """

    Итак - Здесь заполняем настройки

    """
    # Имя поля настроек
    _Settings_name = 'Settings'

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

    # def settings_Eth_0(self):
    #     """
    #     Получить настройки Ethernet 0
    #     :return:
    #     """
    #
    #
    #
    #     return self._Setting_Eth0
    #
    # def settings_Eth_1(self):
    #     """
    #     Получить настройки Ethernet 1
    #     :return:
    #     """
    #
    #     return self._Setting_Eth1

    def get_settings_Ethernet(self):
        """
        Получить настройки Ethernet
        :return:
        """
        Settings = []
        if self._Setting_Eth0 is not None:
            Settings.append(self._Setting_Eth0)

        if self._Setting_Eth1 is not None:
            Settings.append(self._Setting_Eth1)

        return {self._Settings_name: Settings}



