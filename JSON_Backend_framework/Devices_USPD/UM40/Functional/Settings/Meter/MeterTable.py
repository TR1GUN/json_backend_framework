# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                           Таблица приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.MeterDevice.Template_MeterTable_settings import TemplateMeterTable
from JSON_Backend_framework.Service.TemplateDecorator import print_log_use_GET_data
from JSON_Backend_framework.FormJSON.UM40.Settings.Meter.JSON_Construct_Settings_MeterTable import SettingsMeterTable
# -------------------------------------------------------------------------------------------------------------


class MeterTable(TemplateMeterTable):
    """
    Таблица приборов учета

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = SettingsMeterTable()

    # Массив из счетчиков
    _Meters = [{'addr': '72', 'id': 1, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Iface1', 'index': 1, 'pId': 0, 'passRd': '010101010101', 'passWr': '020202020202', 'rtuFider': 1, 'rtuObjNum': 2, 'rtuObjType': 3, 'type': 3, 'typeName': 'Mercury23x'}]

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
       Настройки - Таблица Счетчиков

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # Пункт Первый - Переделываем ВСЕ параметры
    def _getting_settings(self):

        """

        В Классе шаблоне метод получения настроек отвечает за встравку GET запроса


        """
        # Смотрим - есть ли добавленые счетчики
        data = self.Settings.get_settings()
        data = data.get(self._Settings_name)
        if len(data) == 0 :
            # Теперь если у нас есть данные - Считываем их

            data = self._request_setting()
        return data

    # Запрос настроек

    @print_log_use_GET_data
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """

        data = []
        try:
            # делаем запрос - получаем ответ
            response = self.read_settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    Settings = answer_setting[self._Settings_name]
                    if Settings is not None :
                        data = Settings
        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return data


# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data= {'Meters': [{
#                 'addr': '72',
#                  'id': 6,
#                  'ifaceCfg': '9600,8n1',
#                  'ifaceName': 'Iface1',
#                  'index': 1,
#                  'pId': 0,
#                  'passRd': '010101010101',
#                  'passWr': '020202020202',
#                  'rtuFider': 1,
#                  'rtuObjNum': 2,
#                  'rtuObjType': 3,
#                  'type': 3,
#                  'typeName': 'Mercury23x'
#                 }]}
# -------------------------------------------------------------------------------------------------------------
