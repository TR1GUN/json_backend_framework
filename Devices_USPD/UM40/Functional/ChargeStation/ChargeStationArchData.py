# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Таблица данных зарядных станций
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class ChargeStationArchData(TemplateFunctional):
    """
    Опрос зарядных станций
    """
    # URL
    from Devices_USPD.settings import url_path_smart40
    _path_url = url_path_smart40.get("ChargeStationArchData")
    # _path_url ="/charge/data/arch"
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

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

    def read_settings_StationParams(self, ids: [None, list, int] = None,
                                    time_start: [int, None] = None,
                                    time_end: [int, None] = None):
        """
        Состояние зарядных станций - чтение

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """
        # Задаем Таблицу
        measure = 'stationParams'

        # Создаем шаблон запроса
        data = {'measure': measure}
        # Если задан ids
        if ids is not None:
            # если он инт - формируем список
            if type(ids) is int:
                data["ids"] = [ids]
            # если у нас список
            if type(ids) is list:
                data["ids"] = ids
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по умолчанию
            # для старта - 0
            # для финиша - текущие время + 1000
            if type(time_start) is int:
                start = time_start
            else:
                start = 0
            if type(time_end) is int:
                end = time_end
            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                end = datetime.now()
                # переводим в UNIX time
                end = mktime(end.timetuple())
                # Переводим в int
                end = int(end) + 1000
            # Теперь формируем все это
            data["time"] = [{"start": start, "end": end}]

        # Запаковываембэк
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def read_settings_chargeProcessParams(self, ids: [None, list, int] = None,
                                          time_start: [int, None] = None,
                                          time_end: [int, None] = None):
        """
        Состояние процесса заряда - чтение

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """
        # Задаем Таблицу
        measure = 'chargeProcessParams'

        # Создаем шаблон запроса
        data = {'measure': measure}
        # Если задан ids
        if ids is not None:
            # если он инт - формируем список
            if type(ids) is int:
                data["ids"] = [ids]
            # если у нас список
            if type(ids) is list:
                data["ids"] = ids
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по умолчанию
            # для старта - 0
            # для финиша - текущие время + 1000
            if type(time_start) is int:
                start = time_start
            else:
                start = 0
            if type(time_end) is int:
                end = time_end
            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                end = datetime.now()
                # переводим в UNIX time
                end = mktime(end.timetuple())
                # Переводим в int
                end = int(end) + 1000
            # Теперь формируем все это
            data["time"] = [{"start": start, "end": end}]

        # Запаковываембэк
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def read_settings_chargeSessionParams(self, ids: [None, list, int] = None,
                                          time_start: [int, None] = None,
                                          time_end: [int, None] = None):
        """
        История зарядных сессий - чтение

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """
        # Задаем Таблицу
        measure = 'chargeSessionParams'

        # Создаем шаблон запроса
        data = {'measure': measure}
        # Если задан ids
        if ids is not None:
            # если он инт - формируем список
            if type(ids) is int:
                data["ids"] = [ids]
            # если у нас список
            if type(ids) is list:
                data["ids"] = ids
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по умолчанию
            # для старта - 0
            # для финиша - текущие время + 1000
            if type(time_start) is int:
                start = time_start
            else:
                start = 0
            if type(time_end) is int:
                end = time_end
            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                end = datetime.now()
                # переводим в UNIX time
                end = mktime(end.timetuple())
                # Переводим в int
                end = int(end) + 1000
            # Теперь формируем все это
            data["time"] = [{"start": start, "end": end}]

        # Запаковываембэк
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def read_settings(self, measure: str,
                      ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None):
        """
         Формирование запроса на чтение данных в нужной таблице :

        :param measure: - str - Обязательное значение - имя таблицы что читаем. Допустимые значения : chargeSessionParams ,
        chargeProcessParams , stationParams , chargeStations
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """
        # Задаем Таблицу
        measure = str(measure)

        # Создаем шаблон запроса
        data = {'measure': measure}
        # Если задан ids
        if ids is not None:
            # если он инт - формируем список
            if type(ids) is int:
                data["ids"] = [ids]
            # если у нас список
            if type(ids) is list:
                data["ids"] = ids
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по умолчанию
            # для старта - 0
            # для финиша - текущие время + 1000
            if type(time_start) is int:
                start = time_start
            else:
                start = 0
            if type(time_end) is int:
                end = time_end
            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                end = datetime.now()
                # переводим в UNIX time
                end = mktime(end.timetuple())
                # Переводим в int
                end = int(end) + 1000
            # Теперь формируем все это
            data["time"] = [{"start": start, "end": end}]

        # Запаковываембэк
        data = self._coding(data=data)
        print(data)
        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response


# {ids: [2], time: [], measure: "stationParams"}
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# chargeSessionParams ,
#         chargeProcessParams , stationParams , chargeStations
# lol = ChargeStationArchData()
#
# print(lol.read_settings(measure='chargeSessionParams',ids=[1,2] , time_start=0 , time_end=None))
