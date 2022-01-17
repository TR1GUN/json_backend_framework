# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки линий питания интерфейсов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_DOut_settings import \
    TemplateInterface_DOut_PowerLine


# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
class SettingsDOut:
    """

    Класс настроек для линий питания интерфейсов

    """
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
        return self._Settings


class Interface_DOut_PowerLine(TemplateInterface_DOut_PowerLine):
    """
    Настройки линий питания интерфейсов

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = SettingsDOut()

    # Таблица соответствий
    DOut_name = {
                1: '/dev/ttyUSB3',
                2: '/dev/ttyUSB2',
                3: '/dev/ttyUSB1',
                4: '/dev/ttyUSB0',
                }

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки линий питания интерфейсов

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
        SettingsDOut_list = self.Settings.get_settings()

        # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
        StateDOut1 = None
        StateDOut2 = None
        StateDOut3 = None
        StateDOut4 = None

        state_dict = \
            {
                0: StateDOut1,
                1: StateDOut2,
                2: StateDOut3,
                3: StateDOut4,

            }
        # Определяем
        for DOut in SettingsDOut_list:
            state_dict[DOut.get('id')] = DOut

        # ЕСЛИ ЕСТЬ ГДЕ То None , то запрашиваем данные
        if (StateDOut1 is None) or (StateDOut2 is None) or (StateDOut3 is None) or (StateDOut4 is None):
            data_request = self._request_setting()
            # Теперь перебираем
            for NumberUart in state_dict:
                if state_dict[NumberUart] is None:
                    # Теперь ищем их положение в ответе
                    for i in data_request:
                        # Ищем соответсвия по их адресу
                        if i.get('addr') == self.DOut_name[NumberUart + 1]:


                            state_dict[NumberUart] = i

        data = []
        for i in state_dict :
            data.append(state_dict[i])
        return data
# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data': {'Settings': [
#                      {'addr': '/dev/ttyUSB3', 'state': 'toggle'},
#                      {'addr': '/dev/ttyUSB2', 'state': 'toggle'},
#                      {'addr': '/dev/ttyUSB1', 'state': 'toggle'},
#                      {'addr': '/dev/ttyUSB0', 'state': 'toggle'}
#                      ]}
# -------------------------------------------------------------------------------------------------------------
