# -------------------------------------------------------------------------------------------------------------
#                                     Шаблон для JSON - Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------

class TemplateFormJSON_MeterData:
    """
    Шаблон для JSON - Чтение Данных счетчиков
    """
    # Готовый запрос
    _Settings = None

    # Типы данных для добавления
    _measure = None
    # Добавление - айдишники
    _ids = None
    # Добавление - Время
    _time = None
    # Добавление - Таги
    _tags = None
    # Доступные типы данных
    _measures = []

    # В этом методе
    # UTC время в UNIX TIME
    def _convert_UTC_to_UNIXTIME(self, time_str: str):
        """
        В этом методе переводим UTC время в UNIX TIME
        :param time_str:
        :return:
        """
        from datetime import datetime
        # Вводим понятие паттерна времени
        pattern = "%Y-%m-%dT%H:%M:%S%z"

        try:
            # Пытаемся спарсить
            timestamp_datetime = datetime.strptime(time_str, pattern)
            timestamp_unixtime = int(timestamp_datetime.timestamp())
        except Exception as e:
            # Иначе логируем ошибку
            error = "Error convert time. received time value : " + str(time_str) + ".\n Error Exception : " + str(e)
            print(error)
            timestamp_unixtime = None

        return timestamp_unixtime

    # В этом методе переводим UNIX TIME во время в UTC
    def _convert_UNIXTIME_to_UTC(self, time_int: int):
        """
        В этом методе переводим UNIX TIME время в UTC
        :param time_int:
        :return:
        """
        from datetime import datetime, timezone

        try:
            time_utc = datetime.fromtimestamp(time_int, timezone.utc).astimezone().isoformat()

        except Exception as e:
            # Иначе логируем ошибку
            error = "Error convert time. received time value : " + str(time_int) + ".\n Error Exception : " + str(e)
            print(error)
            time_utc = ""

        return time_utc

    # Формируем поле Measure - Тип данных
    def _form_key_Measure(self, measure):
        """
        Формируем поле Measure - Тип данных
        """
        # Measure - Тип данных
        # Если у нас строка - делаем из нее массив
        if type(measure) is str:
            measure = [measure]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(measure) is list:
            for measure_element in measure:
                if measure_element in self._measures:
                    self._measure.add(measure_element)

    # Формируем поле Ids - внешний id
    def _form_key_Ids(self, ids):
        """
        Формируем поле Ids - внешний id
        """
        # Ids - внешний id
        if type(ids) is str or type(ids) is int:
            ids = [ids]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(ids) in list:
            for ids_element in ids:
                self._ids.add(ids_element)

    # Формируем поле tags - Массив тэгов что спускаем
    def _form_key_Tags(self, tags):
        """
        Формируем поле tags - Массив тэгов что спускаем
        """
        # tags - Массив тэгов что спускаем
        if type(tags) is str:
            tags = [tags]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(tags) is list:
            for tags_element in tags:
                if tags_element in self._measures:
                    self._tags.add(tags_element)

    # Формируем поле Time - Массив времени что задаем для чтения данных
    def _form_key_Time(self, time_start, time_end):
        """
        Формируем поле Time - Массив времени что задаем для чтения данных
        """
        # Time - Массив времени что задаем для чтения данных
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по
            # умолчанию для старта - 0 для финиша - текущие время + 1000
            if type(time_start) is int:
                start = self._convert_UNIXTIME_to_UTC(time_int=time_start)
            elif type(time_start) is str:
                start = time_start
            else:
                start = self._convert_UNIXTIME_to_UTC(time_int=1)

            if type(time_end) is int:
                end = self._convert_UNIXTIME_to_UTC(time_int=time_end)

            elif type(time_end) is str:
                end = time_end

            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                time_end_datatime = datetime.now()
                # переводим в UNIX time
                time_end = mktime(time_end_datatime.timetuple())
                # Переводим в int
                time_end = int(time_end) + 1000
                # Теперь формируем все это
                end = self._convert_UNIXTIME_to_UTC(time_int=time_end)

            time_dict = {"start": start, "end": end}
            self._time.append(time_dict)

    # удаляем нужное поле Measure - Тип данных
    def _delete_key_Measure(self, measure):
        """
        Удаляем нужное поле  Measure - Тип данных
        """
        # Measure - Тип данных
        # Если у нас строка - делаем из нее массив
        if type(measure) is str:
            measure = [measure]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(measure) is list:
            for measure_element in measure:
                if measure_element in self._measure:
                    self._measure.remove(measure_element)

    # удаляем нужное поле Ids - внешний id
    def _delete_key_Ids(self, ids):
        """
        Удаляем нужное поле Ids - внешний id
        """
        # Ids - внешний id
        if type(ids) is str or type(ids) is int:
            ids = [ids]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(ids) in list:
            for ids_element in self._ids:
                self._ids.remove(ids_element)

    # удаляем нужное поле tags - Массив тэгов что спускаем
    def _delete_key_Tags(self, tags):
        """
        Удаляем нужное поле tags - Массив тэгов что спускаем
        """
        # tags - Массив тэгов что спускаем
        if type(tags) is str:
            tags = [tags]
        # Теперь перебираем все элементы массива и добавляем только корректные типы данных
        if type(tags) is list:
            for tags_element in tags:
                if tags_element in self._tags:
                    self._tags.remove(tags_element)

    # удаляем нужное поле Time - Массив времени что задаем для чтения данных
    def _delete_key_Time(self, time_start, time_end):
        """
        Удаляем нужное поле Time - Массив времени что задаем для чтения данных
        """
        # Time - Массив времени что задаем для чтения данных
        # Теперь формируем массив из времени если оно заданно
        if (time_start is not None) or (time_end is not None):
            # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по
            # умолчанию для старта - 0 для финиша - текущие время + 1000
            if type(time_start) is int:
                start = self._convert_UNIXTIME_to_UTC(time_int=time_start)
            elif type(time_start) is str:
                start = time_start
            else:
                start = self._convert_UNIXTIME_to_UTC(time_int=1)

            if type(time_end) is int:
                end = self._convert_UNIXTIME_to_UTC(time_int=time_end)

            elif type(time_end) is str:
                end = time_end

            else:
                from datetime import datetime
                from time import mktime
                # Берем текущие время
                time_end_datatime = datetime.now()
                # переводим в UNIX time
                time_end = mktime(time_end_datatime.timetuple())
                # Переводим в int
                time_end = int(time_end) + 1000
                # Теперь формируем все это
                end = self._convert_UNIXTIME_to_UTC(time_int=time_end)

            time_dict = {"start": start, "end": end}

            if time_dict in self._time:
                self._time.remove(time_dict)

    # Добавляем
    def add_Value(self,
                  measure: [str, list] = None,
                  ids: [None, list, str, int] = None,
                  time_start: [None, list, str, int] = None,
                  time_end: [None, list, str, int] = None,
                  tags: [None, list, str] = None):

        """
        Формирование значений запроса на чтение данных в нужной таблице :

        :param measure: - str - Обязательное значение - типа данных что читаем. Допустимые значения :
        :param ids: - int/list/None - Meter ID  - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                            если строка - то тэг что указан в строке,
                                            если список , то список тэгов что указан в массиве.
        :return:
        """
        # Добавляем поле Measure
        if measure:
            self._form_key_Measure(measure=measure)

        # Добавляем поле ids
        if ids:
            self._form_key_Ids(ids=ids)

        # Добавляем поле tags
        if tags:
            self._form_key_Tags(tags=tags)

        # Добавляем поле time
        if time_start or time_end:
            self._form_key_Time(time_start=time_start, time_end=time_end)

    # Удаляем
    def remove_Value(self,
                     measure: [str, list] = None,
                     ids: [None, list, str, int] = None,
                     time_start: [None, list, str, int] = None,
                     time_end: [None, list, str, int] = None,
                     tags: [None, list, str] = None):

        """
        Удаление значений из запроса на чтение данных в нужной таблице :

        :param measure: - str - Обязательное значение - типа данных что читаем. Допустимые значения :
        :param ids: - int/list/None - Meter ID  - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                            если строка - то тэг что указан в строке,
                                            если список , то список тэгов что указан в массиве.
        :return:
        """
        # Добавляем поле Measure
        if measure:
            self._delete_key_Measure(measure=measure)

        # Добавляем поле ids
        if ids:
            self._delete_key_Ids(ids=ids)

        # Добавляем поле tags
        if tags:
            self._delete_key_Tags(tags=tags)

        # Добавляем поле time
        if time_start or time_end:
            self._delete_key_Time(time_start=time_start, time_end=time_end)

    def get_JSON(self):
        """
        Получаем наши данные что составили
        """
        self._Settings = \
            {
                "measure": list(self._measure),
                "ids": list(self._ids),
                "tags": list(self._tags)
            }
        if len(self._time) > 0:
            self._Settings["time"] = list(self._time)

        return self._Settings
