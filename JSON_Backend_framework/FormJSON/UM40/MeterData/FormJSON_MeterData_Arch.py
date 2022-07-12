# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                   Протокол УМ-40 СМАРТ
#                                             Чтение Данных счетчиков - Архивные
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Form_JSON.MeterData.FormJSON_MeterData import TemplateFormJSON_MeterData

# -------------------------------------------------------------------------------------------------------------


class FormJSON_MeterDataArch(TemplateFormJSON_MeterData):
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

    # доступные тэги типов данных

    def __init__(self):
        self._Settings = {}
        # Обновляем переменные
        # Типы данных
        self._measure = set()
        # айдишники
        self._ids = set()
        # Тайм штампы времени
        self._time = []
        # таги
        self._tags = set()

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
            if type(time_start) is str:
                start = self._convert_UTC_to_UNIXTIME(time_str=time_start)
            elif type(time_start) is int:
                start = time_start
            else:
                start = 1

            if type(time_end) is str:
                end = self._convert_UTC_to_UNIXTIME(time_str=time_end)

            elif type(time_end) is int:
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
                end = time_end

            time_dict = {"start": start, "end": end}
            self._time.append(time_dict)

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
# -------------------------------------------------------------------------------------------------------------
#                             Теперь такой же конструктор только с указанными Measure
# -------------------------------------------------------------------------------------------------------------
