# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                     Настройки последовательных интерфейсов(UART)
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------

class SettingsUART:
    """

    Класс настроек для UART портов

    """
    _Settings = None
    # Имя поля настроек
    _Settings_name = 'Settings'

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

    def remove_Iface(self, Iface: int):

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
        return {self._Settings_name: self._Settings}
