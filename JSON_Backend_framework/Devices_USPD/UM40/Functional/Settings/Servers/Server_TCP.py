# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки TCP-серверов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Servers.Template_TCP_server_settings import \
    TemplateServer_TCP


# -------------------------------------------------------------------------------------------------------------
# Класс для добавления своих серверов
class Server:

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

    def get_servers(self):
        """
        Отдаем наши введенные порты

        """
        return self._Server_list

    def delete_server_for_port(self, ports:(int, list)):

        if type(ports) is int:
            ports = [ports]

        # Образовываем новый список
        Server_list = []
        # Теперь проходимся по нашему списку и удаляем если есть соответствия
        for setting in self._Server_list:
            if setting.get('port') not in ports:
                Server_list.append(setting)

        # Переопредлеляем
        self._Server_list = Server_list


class ServerTCP(TemplateServer_TCP):
    """

    Настройки TCP-серверов
    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = Server()

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки TCP-серверов

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # Здесь расположим сервисные функции
    # Первое - Получаем настройки что уже есть

    def _getting_settings(self):

        """
        В Классе метод получения настроек отвечает за
        Если добавлены настройки, вставляем их ,
        Если нет, вставку GET запроса

        """
        # Сначала получаем наши данные что ввели
        server_list = self.Settings.get_servers()

        # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
        if len(server_list) > 0:
            data = server_list
        else:
            data = self._request_setting()

        return data

# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data =  {'Settings': [{'type': 'rtu327', 'por t': '7777'}]}
# -------------------------------------------------------------------------------------------------------------


