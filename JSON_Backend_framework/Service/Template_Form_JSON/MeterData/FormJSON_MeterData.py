# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                  Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------

class FormJSON_MeterData:

    _Settings = None

    def __init__(self):

        self._Settings = None


    def add_settings(self, measure: str,
                       ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):

        """
        Формирование запроса на чтение данных в нужной таблице :

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

        # Первое - Проверяем
        pass

    def _read_settings(self, measure: str,
                       ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):
        """
         Формирование запроса на чтение данных в нужной таблице :

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
        # Задаем тип данных
        measure = str(measure)

        # и ищем его в качестве основы -  и лишь тогда продолжаем
        if measure in self._measures:
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
                # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по
                # умолчанию для старта - 0 для финиша - текущие время + 1000
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

            # работает с тэгами
            if tags is not None:
                # Если у нас один тэг -строка - обрабатываем его
                if type(tags) is str:
                    data["tags"] = [tags]
                elif type(tags) is list:
                    added = []
                    for tag in tags:
                        added.append(str(tag))
                    data["tags"] = added