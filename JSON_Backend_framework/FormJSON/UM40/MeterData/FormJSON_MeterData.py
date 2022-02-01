# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                  Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------

class FormJSON_MeterData:
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
    _measures = [
        'ElConfig',
        'PlsConfig',
        'DigConfig',

        'ElMomentEnergy',
        'ElDayEnergy',
        'ElMonthEnergy',
        'ElDayConsEnergy',
        'ElMonthConsEnergy',
        'ElMomentQuality',
        'ElArr1ConsPower',
        'PlsMomentPulse',
        'PlsDayPulse',
        'PlsMonthPulse',
        'PlsHourPulse',
        'DigMomentState',
        'DigJournalState',
        'ElJrnlPwr',
        'ElJrnlTimeCorr',
        'ElJrnlReset',
        'ElJrnlC1Init',
        'ElJrnlC2Init',
        'ElJrnlTrfCorr',
        'ElJrnlOpen',
        'ElJrnlUnAyth',
        'ElJrnlPwrA',
        'ElJrnlPwrB',
        'ElJrnlPwrC',
        'ElJrnlProg',
        'ElJrnlRelay',
        'ElJrnlLimESumm',
        'ElJrnlLimETrf',
        'ElJrnlLimETrf1',
        'ElJrnlLimETrf2',
        'ElJrnlLimETrf3',
        'ElJrnlLimETrf4',
        'ElJrnlLimUAMax',
        'ElJrnlLimUAMin',
        'ElJrnlLimUBMax',
        'ElJrnlLimUBMin',
        'ElJrnlLimUCMax',
        'ElJrnlLimUCMin',
        'ElJrnlLimUABMax',
        'ElJrnlLimUABMin',
        'ElJrnlLimUBCMax',
        'ElJrnlLimUBCMin',
        'ElJrnlLimUCAMax',
        'ElJrnlLimUCAMin',
        'ElJrnlLimIAMax',
        'ElJrnlLimIBMax',
        'ElJrnlLimICMax',
        'ElJrnlLimFreqMax',
        'ElJrnlLimFreqMin',
        'ElJrnlLimPwr',
        'ElJrnlLimPwrPP',
        'ElJrnlLimPwrPM',
        'ElJrnlLimPwrQP',
        'ElJrnlLimPwrQM',
        'ElJrnlReverce',
        'PlsJrnlTimeCorr'
    ]

    def __init__(self):

        self._Settings = {}
        # Обновляем переменные
        # айдишники
        self._ids = []
        # Тайм штампы времени
        self._time = []
        # таги
        self._tags = []

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
        measure = str(measure)
        # и ищем его в качестве основы -  и лишь тогда продолжаем
        if measure in self._measures:
            # Создаем шаблон запроса
            self._measure = measure

            # Если задан ids
            if ids is not None:
                # если он инт - формируем список
                ids_set = set(self._ids)
                if type(ids) is int:
                    ids_set.add(ids)

                # если у нас список
                if type(ids) is list:
                    ids_set.update(ids)

                self._ids = list(ids_set)

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
                time_dict = {"start": start, "end": end}
                self._time.append(time_dict)
            # работает с тэгами
            if tags is not None:
                # Если у нас один тэг -строка - обрабатываем его
                if type(tags) is str:
                    if tags not in self._tags:
                        self._tags.append(tags)
                elif type(tags) is list:
                    for tag in tags:
                        if tag not in self._tags:
                            self._tags.append(tag)

            # self._Settings = {
            #     'measure': self._measure,
            #     "ids": self._ids,
            #     "time": self._time,
            #     "tags": self._tags,
            # }

    def get_settings(self):
        """
        Получаем наши данные что составили
        """
        self._Settings = \
            {
                "measure": self._measure,
                "ids": self._ids,
                "time": self._time,
                "tags": self._tags,
            }

        return self._Settings


# -------------------------------------------------------------------------------------------------------------
#                             Теперь такой же конструктор только с указанными Measure
# -------------------------------------------------------------------------------------------------------------
