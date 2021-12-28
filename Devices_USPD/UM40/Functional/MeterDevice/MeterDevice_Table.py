# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                           Таблица приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.TemplateDeviceFunctions import TemplateDeviceFunctions, TemplateSettingsData


class MeterDeviceTable(TemplateDeviceFunctions):
    """
     Таблица приборов учета
    """

    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Metering_device_table")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
         Таблица приборов учета

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)
        self._define_settings_ids()

    def _define_settings_ids(self):

        """
        Переопределяем Наши настройки
        :return:
        """

        self.Data_Settings = SettingsMeterTable()

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data: Данные в Формате JSON - Если None - то используем добавленные данные
        :return:
        """
        if data is None:
            data_settings = self.Data_Settings.get_settings()
            data = {'Meters': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data):
        """
        Перезаписываем данные - PUT
        :param data: Данные в Формате JSON - Если None - то используем добавленные данные
        :return:
        """
        if data is None:
            data_settings = self.Data_Settings.get_settings()
            data = {'Meters': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """

        if data is None:

            data_settings = self.Data_Settings.get_ids()

            if len(data_settings) > 0:
                data = {'Meters': data_settings}
            else:
                data = None

        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Настройки Таблица приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class SettingsMeterTable(TemplateSettingsData):
    """

    Класс настроек Зарядных станций

    """

    _Name_Meters = \
        {
            'Меркурий200': 'Mercury200',
            'Меркурий203': 'Mercury203',
            'Меркурий206': 'Mercury206',
            'Меркурий23x': 'Mercury23x',
            'Меркурий234 СПОДЭС': 'SPODES',
            'СЕ102': 'SE102',
            'СЕ102М': 'SE102M',
            'СЕ301': 'SE301',
            'СЕ303': 'SE303',
            'СЭБ2А': 'SEB2a',
            'СЭТ4ТМ': 'SETxTM',
            'ПСЧхТМ': 'PSCHxTM',
            'Альфа1140': 'A1140',
            'ТОПАЗ': 'TOPAZ',
            'НЕВА1xx': 'NEVA1xx',
            'НЕВА3xx': 'NEVA3xx',
            'МИЛУР IC': 'MILUR IC',
            'Милур10x': 'MILUR10x',
            'Милур30x': 'MILUR30x',
            'СОЭ55/215': 'SOE55_215',
            'СОЭ55/217': 'SOE55_217',
            'СОЭ55/415': 'SOE55_415',
            'СТЭ561': 'STE561',
            'ИНТЕГРА10х': 'INTEGRA10x',
            'УМТВ10': 'UMTV10',
            'Пульсар': 'Pulsar',
            'ST410': 'ST410'
        }

    _Name_Interface = {
        'Интерфейс 1': 'Iface1',
        'Интерфейс 2': 'Iface2',
        'Интерфейс 3': 'Iface3',
        'Интерфейс 4': 'Iface4',
        'Ethernet': 'Ethernet',
        'Интерфейс концентратора': 'Hub',
    }

    _list_permissible_Name_Meters = []
    _list_permissible_Name_Interface = []

    _list_permissible_Meters = []
    _list_permissible_Interface = []

    def __init__(self):

        self._data_settings = []
        self._define_type_config()


    def _define_type_config(self):
        """
        Здесь делаем список из поддерживывпаеммых счетчиков - нужно чтоб не выстрелить себе в ногу
        :return:
        """

        self._list_permissible_Name_Meters = list(self._Name_Meters.keys())
        self._list_permissible_Meters = list(self._Name_Meters.values())

        self._list_permissible_Interface = list(self._Name_Interface.values())
        self._list_permissible_Name_Interface = list(self._Name_Interface.keys())

    # {
    #     "Meters": [
    #         {
    #             "id": 1,
    #             "pId": 0,
    #             "typeName": "Mercury23x",
    #             "addr": "72",
    #             "passRd": "010101010101",
    #             "passWr": "020202020202",
    #             "ifaceName": "Iface1",
    #             "ifaceCfg": "9600,8n1",
    #             "rtuObjType": 3,
    #             "rtuObjNum": 2,
    #             "rtuFider": 1
    #         }
    #     ]
    # }
    def add_settings(self, MeterId: int, typeName_Meter: str, Interface: str,
                     address: str, password_to_read: str, password_to_write: str,
                     ParentId: int = 0, ifaceConfig: str = '9600,8n1',
                     rtuObjType: int = 0, rtuObjNum: int = 0, rtuFider: int = 0):
        """
        Добавление настроек для записи
        :param MeterId: - int - ID Счетчика. Используется для взаимодействия со счетчика в дальнейшем.
        :param typeName_Meter: - str - Имя типа счетчика.
                                Можно получить все типы поддержанных счетчиков через метод get_permissible_meters
        :param Interface: - str - Имя типа подключения по Интерфейсу.
                                Можно получить все типы поддержанных Интерфейсов через метод get_permissible_interface
        :param address: - str - Адрес счетчика
        :param password_to_read: - str - Пароль доступа 1 уровня - На чтение
        :param password_to_write: - str - Пароль доступа 2 уровня - На запись
        :param ParentId: - int - Id Родительского устройства. Если его нет, то ставиться 0. Значение по умолчанию - 0
        :param ifaceConfig: - str - Настройки интерфейса . Значение по умолчанию - '9600,8n1
        :param rtuObjType: - int - Тип объекта RTU . Значение по умолчанию - 0
        :param rtuObjNum: - int - Номер объекта RTU . Значение по умолчанию - 0
        :param rtuFider: - int - Фидер объекта RTU . Значение по умолчанию - 0
        :return:
        """
        # Здесь смотрим что мы укладываемся в необходимые условия

        # Если у нас имя которое итак корректно -
        if typeName_Meter not in self._list_permissible_Meters:
            # Теперь вытаскиваем нужные значения
            typeName_Meter = self._Name_Meters.get(typeName_Meter)

        # Теперь делаем тоже самое с интерфейсом
        if Interface not in self._list_permissible_Interface:
            # Теперь вытаскиваем нужные значения
            Interface = self._Name_Interface.get(Interface)

        # Добавляем по условиям - Если корректно ifaceName и typeName_Meter
        # и самое важное - ParentId MeterId  - int , и MeterId > 0
        if (Interface is not None) and (typeName_Meter is not None) and \
                (type(ParentId) is int) and (type(MeterId) is int) and (MeterId > 0):
            # Теперь , если не ноне формируем , добавляем
            settings = \
                {
                    "id": MeterId,
                    "pId": ParentId,
                    "typeName": typeName_Meter,
                    "addr": address,
                    "passRd": password_to_read,
                    "passWr": password_to_write,
                    "ifaceName": Interface,
                    "ifaceCfg": ifaceConfig,
                    "rtuObjType": rtuObjType,
                    "rtuObjNum": rtuObjNum,
                    "rtuFider": rtuFider
                }

            self._data_settings.append(settings)

    def remove_settings(self, idx: [int, list]):
        """
        Удаление добавленной записи settings для записи по ID
        :param idx: - list or int
        :return:
        """
        data_settings = []

        # Перебираем все настройки
        for settings in self._data_settings:
            # Если айдишник не совпадает то добавляем в список
            if settings.get('id') not in idx:
                data_settings.append(settings)

        self._data_settings = data_settings

    def get_settings(self):
        """
        Получаем добавленные Настройки счетчики

        :return:
        """

        return self._data_settings

    def add_ids(self, ids: int):
        """
        Добавляем Device_id для запроса данных или удаления

        :param ids:
        :return:
        """

        self._data_ids.append(ids)

    def remove_ids(self, ids: [int, list]):
        """
        Удаление добавленной записи ids для получения/удаления записей
        :param ids: - list or int
        :return:
        """
        data_ids = []

        # Перебираем все настройки
        for idx in self._data_ids:
            # Если айдишник не совпадает то добавляем в список
            if idx not in ids:
                data_ids.append(settings)

        self._data_ids = data_ids

    def get_ids(self):
        """
        Получаем добавленные ids

        :return:
        """

        return self._data_ids

    def get_permissible_meters(self):
        """
        Получаем размещенные счетчики

        :return:
        """
        # ["Меркурий200","Mercury200"],
        # ["Меркурий203","Mercury203"],
        # ["Меркурий206","Mercury206"],
        # ["Меркурий23x","Mercury23x"],
        # ["Меркурий234 СПОДЭС","SPODES"],
        # ["СЕ102","SE102"],
        # ["СЕ102М","SE102M"],
        # ["СЕ301","SE301"],
        # ["СЕ303","SE303"],
        # ["СЭБ2А","SEB2a"],
        # ["СЭТ4ТМ","SETxTM"],
        # ["ПСЧхТМ","PSCHxTM"],
        # ["Альфа1140","A1140"],
        # ["ТОПАЗ","TOPAZ"],
        # ["НЕВА1xx","NEVA1xx"],
        # ["НЕВА3xx","NEVA3xx"],
        # ["МИЛУР IC","MILUR IC"],
        # ["Милур10x","MILUR10x"],
        # ["Милур30x","MILUR30x"],
        # ["СОЭ55/215","SOE55_215"],
        # ["СОЭ55/217","SOE55_217"],
        # ["СОЭ55/415","SOE55_415"],
        # ["СТЭ561","STE561"],
        # ["ИНТЕГРА10х","INTEGRA10x"],
        # ["УМТВ10","UMTV10"],
        # ["Пульсар","Pulsar"],
        # ["ST410","ST410"]

        return self._Name_Meters

    def get_permissible_interface(self):
        """
        Получаем разрешенные интерфейсы
        :return:
        """
        # ["Интерфейс 1", "Iface1"],
        # ["Интерфейс 2", "Iface2"],
        # ["Интерфейс 3", "Iface3"],
        # ["Интерфейс 4", "Iface4"],
        # ["Ethernet", "Ethernet"],
        # ["Интерфейс концентратора", "Hub"]
        return self._Name_Interface


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# lol = MeterDeviceTable()
# #
# a = {'Meters': [{
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
# print(lol.read_settings())
# a = {'Meters': [{'addr': '72', 'id': 1, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Iface1', 'index': 1, 'pId': 0, 'passRd': '010101010101', 'passWr': '020202020202', 'rtuFider': 1, 'rtuObjNum': 2, 'rtuObjType': 3, 'type': 3, 'typeName': 'Mercury23x'}, {'addr': '72', 'id': 2, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Iface1', 'index': 2, 'pId': 0, 'passRd': '010101010101', 'passWr': '020202020202', 'rtuFider': 1, 'rtuObjNum': 2, 'rtuObjType': 3, 'type': 3, 'typeName': 'Mercury23x'}, {'addr': '72', 'id': 3, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Iface1', 'index': 3, 'pId': 0, 'passRd': '010101010101', 'passWr': '020202020202', 'rtuFider': 1, 'rtuObjNum': 2, 'rtuObjType': 3, 'type': 3, 'typeName': 'Mercury23x'}]}
#
# print(lol.write_settings(a))