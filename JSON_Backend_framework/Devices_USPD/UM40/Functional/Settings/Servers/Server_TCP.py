# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки TCP-серверов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Servers.Template_TCP_server_settings import \
    TemplateServer_TCP

# Импортируем шаблон Настроек
from JSON_Backend_framework.FormJSON.UM40.Settings.Servers.JSON_Construct_Settings_Server_TCP import SettingsServer
# -------------------------------------------------------------------------------------------------------------


class ServerTCP(TemplateServer_TCP):
    """

    Настройки TCP-серверов
    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = SettingsServer()

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
        servers_data = self.Settings.get_servers()
        # Теперь что делаем - смотрим что в дата таге
        servers_list = servers_data.get(self._Settings_name)
        # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
        if servers_list is not None:
            if len(servers_list) > 0:
                data = servers_list
            else:
                data = self._request_setting()
        else:
            data = self._request_setting()

        return data

# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data =  {'Settings': [{'type': 'rtu327', 'port': '7777'}]}
# -------------------------------------------------------------------------------------------------------------


