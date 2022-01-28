# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                          Настройки линий питания интерфейсов
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
class SettingsDOut:
    """

    Класс настроек для линий питания интерфейсов

    """
    # Имя поля настроек
    _Settings_name = 'Settings'

    _Settings = None

    def __init__(self):
        self._Settings = []

    def add_State_Iface1(self, state: int):

        """
        Добавление настроек для Интерфейса 1
        """
        setting = {
            "id": 0,
            'addr': '/dev/ttyUSB3',
            'state': state
        }
        self._Settings.append(setting)

    def add_State_Iface2(self, state: int):

        """
        Добавление настроек для Интерфейса 2
        """
        setting = {
            "id": 1,
            'addr': '/dev/ttyUSB2',
            'state': state
        }
        self._Settings.append(setting)

    def add_State_Iface3(self, state: int):

        """
        Добавление настроек для Интерфейса 3
        """
        setting = {
            "id": 2,
            'addr': '/dev/ttyUSB1',
            'state': state
        }
        self._Settings.append(setting)

    def add_State_Iface4(self, state: int):

        """
        Добавление настроек для Интерфейса 4
        """
        setting = {
            "id": 3,
            'addr': '/dev/ttyUSB0',
            'state': state
        }
        self._Settings.append(setting)

    def remove_State_Iface(self, Iface: int):

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
            if setting.get('id') not in Iface:
                _Settings.append(setting)

        # Переопредлеляем
        self._Settings = _Settings

    def get_settings(self):
        """
        Получаем наш список настроек
        """
        return {self._Settings_name : self._Settings}
