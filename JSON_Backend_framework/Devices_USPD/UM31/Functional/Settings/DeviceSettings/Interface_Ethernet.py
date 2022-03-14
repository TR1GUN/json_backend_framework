# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_Ethernet_settings import TemplateInterface_Ethernet
from JSON_Backend_framework.Service.TemplateDecorator import print_log_use_GET_data
from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_Ethernet import SettingsEthernet
# -------------------------------------------------------------------------------------------------------------


class Interface_Ethernet(TemplateInterface_Ethernet):
    """
    Настройки Ethernet

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = None
    # Имя поля настроек
    _Settings_name = 'Settings'
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
        # Обнуляем
        self._define_JSON()

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.Settings = SettingsEthernet()

    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса -
        Здесь переопределяем

        """
        data = self._getting_settings_Ethernet()
        data = {self._Settings_name: data}
        return data

    def _getting_settings_Ethernet(self):

        """
        Получение настроек что задали
        """

        # Пункт первый -  читаем какие настройки у нас есть
        settings_Ethernet = self.Settings.get_settings_Ethernet()

        Ethernet1 = None
        Ethernet2 = None
        Ethernet = settings_Ethernet.get(self._Settings_name)



        for i in Ethernet:
            if i.get('iface') == 'eth0':
                Ethernet1 = i
            if i.get('iface') == 'eth1':
                Ethernet2 = i

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

        # Обнуляем
        self._define_JSON()
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
            response = self.Read_Settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                sim_setting = response.get('data')
                # Теперь заполянем наши переменные
                if sim_setting is not None:

                    # print(sim_setting)
                    Settings = sim_setting[self._Settings_name]
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
