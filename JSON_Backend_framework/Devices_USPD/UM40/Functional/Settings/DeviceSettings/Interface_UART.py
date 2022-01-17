# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки последовательных интерфейсов(UART)
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_UART_settings import \
    TemplateInterface_UART


# -------------------------------------------------------------------------------------------------------------
class SettingsUART:
    """

    Класс настроек для UART портов

    """
    _Settings = None

    def __init__(self):
        self._Settings = []

    def add_Iface1(self, line: int, br: int, size: int, parity: int, stop: int):

        """
        Добавление настроек для Интерфейса 1
        """
        setting = {
            "id": 1,
            "line": line,
            "iface": 0,
            "br": br,
            "size": size,
            "parity": parity,
            "stop": stop
        }
        self._Settings.append(setting)


    def add_Iface2(self, line: int, br: int, size: int, parity: int, stop: int):

        """
        Добавление настроек для Интерфейса 2
        """
        setting = {
            "id": 2,
            "line": line,
            "iface": 1,
            "br": br,
            "size": size,
            "parity": parity,
            "stop": stop
        }
        self._Settings.append(setting)


    def add_Iface3(self, line: int, br: int, size: int, parity: int, stop: int):

        """
        Добавление настроек для Интерфейса 3
        """
        setting = {
            "id": 3,
            "line": line,
            "iface": 2,
            "br": br,
            "size": size,
            "parity": parity,
            "stop": stop
        }
        self._Settings.append(setting)


    def add_Iface4(self, line: int, br: int, size: int, parity: int, stop: int):

        """
        Добавление настроек для Интерфейса 4
        """
        setting = {
            "id": 4,
            "line": line,
            "iface": 3,
            "br": br,
            "size": size,
            "parity": parity,
            "stop": stop
        }
        self._Settings.append(setting)

    def remove_Iface(self, Iface: int ):

        """
        Удаляем интерфес , что добавили
        """

        if type(Iface) is int:
            Iface = [Iface]

        for iface_int in Iface:
            iface_int = iface_int - 1

        # Образовываем новый список
        _Settings = []
        # Теперь проходимся по нашему списку и удаляем если есть соответствия
        for setting in self._Settings:
            if setting.get('iface') not in Iface:
                _Settings.append(setting)

        # Переопредлеляем
        self._Settings = _Settings

    def get_settings(self):
        """
        Получаем наш список настроек
        """
        return self._Settings

class Interface_UART(TemplateInterface_UART):
    """
    Настройки последовательных интерфейсов(UART)

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = SettingsUART

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки последовательных интерфейсов(UART)

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

        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса

        """
        # Читаем что задали
        SettingsUART = self.Settings.get_settings()

        # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
        if len(SettingsUART) > 0:
            data = SettingsUART
        else:
            data = self._request_setting()

        return data




# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------------------------
