# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки линий питания интерфейсов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_DOut_settings import \
    TemplateInterface_DOut_PowerLine
from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_DOut import SettingsDOut
# -------------------------------------------------------------------------------------------------------------


class Interface_DOut_PowerLine(TemplateInterface_DOut_PowerLine):
    """
    Настройки линий питания интерфейсов

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # # Общие настройки
    # Settings = None
    #
    # # Таблица соответствий
    # DOut_name = {
    #             1: '/dev/ttyUSB3',
    #             2: '/dev/ttyUSB2',
    #             3: '/dev/ttyUSB1',
    #             4: '/dev/ttyUSB0',
    #             }

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
        # # Обнуляем
        # self._define_JSON()
    #
    # def _define_JSON(self):
    #     """
    #     Здесь Сбрасываем настройки
    #     """
    #     # Сбрасываем настройки
    #     self.Settings = SettingsDOut()
    #
    # def _getting_settings(self):
    #
    #     """
    #
    #     В Классе шаблоне метод получения настроек отвечает за вставку GET запроса
    #
    #     """
    #     # Читаем что задали
    #     SettingsDOut_dict = self.Settings.get_settings()
    #     SettingsDOut_list = SettingsDOut_dict.get(self._Settings_name)
    #     # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
    #     StateDOut1 = None
    #     StateDOut2 = None
    #     StateDOut3 = None
    #     StateDOut4 = None
    #
    #     state_dict = \
    #         {
    #             0: StateDOut1,
    #             1: StateDOut2,
    #             2: StateDOut3,
    #             3: StateDOut4,
    #
    #         }
    #     # Определяем
    #     for DOut in SettingsDOut_list:
    #         state_dict[DOut.get('id')] = DOut
    #
    #     # ЕСЛИ ЕСТЬ ГДЕ То None , то запрашиваем данные
    #     if (StateDOut1 is None) or (StateDOut2 is None) or (StateDOut3 is None) or (StateDOut4 is None):
    #         data_request = self._request_setting()
    #         # Теперь перебираем
    #         for NumberUart in state_dict:
    #             if state_dict[NumberUart] is None:
    #                 # Теперь ищем их положение в ответе
    #                 for i in data_request:
    #                     # Ищем соответсвия по их адресу
    #                     if i.get('addr') == self.DOut_name[NumberUart + 1]:
    #                         state_dict[NumberUart] = i
    #
    #     data = []
    #     for i in state_dict :
    #         data.append(state_dict[i])
    #
    #     self._define_JSON()
    #     return data
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
