# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                               Настройки TCP-серверов
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Form_JSON.Settings.Servers.Template_JSON_Construct_Settings_Server_TCP import TemplateSettingsServer
# -------------------------------------------------------------------------------------------------------------


# Класс для добавления своих серверов
class SettingsServer(TemplateSettingsServer):

    _Server_list = None

    # Сервера что возможны :

    def __init__(self):
        self._Server_list = []

    def add_RTU327(self, port: int):
        """
        Добавление сервера RTU327
        :param port: - `int` - Номер порта

        """
        # Формируем шаблон
        server_settings = {'type': 'rtu327', 'port': int(port)}
        # Добавляем
        self._Server_list.append(server_settings)

    def add_IFace1(self, port: int):
        """
        Добавление сервера IFace1
        :param port: - `int` - Номер порта

        """
        # Формируем шаблон
        server_settings = {'type': 'iface1', 'port': int(port)}
        # Добавляем
        self._Server_list.append(server_settings)

    def add_IFace2(self, port: int):
        """
        Добавление сервера IFace2
        :param port: - `int` - Номер порта

        """
        # Формируем шаблон
        server_settings = {'type': 'iface2', 'port': int(port)}
        # Добавляем
        self._Server_list.append(server_settings)

    def add_IFace3(self, port: int):
        """
        Добавление сервера IFace3
        :param port: - `int` - Номер порта

        """
        # Формируем шаблон
        server_settings = {'type': 'iface3', 'port': int(port)}
        # Добавляем
        self._Server_list.append(server_settings)

    def add_IFace4(self, port: int):
        """
        Добавление сервера IFace4
        :param port: - `int` - Номер порта

        """
        # Формируем шаблон
        server_settings = {'type': 'iface4', 'port': int(port)}
        # Добавляем
        self._Server_list.append(server_settings)
