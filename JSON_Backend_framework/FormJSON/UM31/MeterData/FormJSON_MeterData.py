# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                   Протокол УМ-31 СМАРТ
#                                                  Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Form_JSON.MeterData.FormJSON_MeterData import TemplateFormJSON_MeterData

# -------------------------------------------------------------------------------------------------------------


class FormJSON_MeterData(TemplateFormJSON_MeterData):
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
        'mRelay',
        "mTime",
        'mQual',
        'mEng',
        'aCfg',
        'aEng',
        'aQual',
        'aDay',
        'aDayCons',
        'aMonth',
        'aMonthCons',
        'aCons',
        'aHour', 'jrnlPwr', 'jrnlTimeCorr', 'jrnlReset', 'jrnlC1Init', 'jrnlC2Init', 'jrnlTrfCorr', 'jrnlOpen',
        'jrnlUnAyth', 'jrnlPwrA', 'jrnlPwrB', 'jrnlPwrC', 'jrnlProg', 'jrnlRelay', 'jrnlLimESumm', 'jrnlLimETrf',
        'jrnlLimETrf1', 'jrnlLimETrf2', 'jrnlLimETrf3', 'jrnlLimETrf4', 'jrnlLimUAMax', 'jrnlLimUAMin', 'jrnlLimUBMax',
        'jrnlLimUBMin', 'jrnlLimUCMax', 'jrnlLimUCMin', 'jrnlLimUABMax', 'jrnlLimUABMin', 'jrnlLimUBCMax',
        'jrnlLimUBCMin', 'jrnlLimUCAMax', 'jrnlLimUCAMin', 'jrnlLimIAMax', 'jrnlLimIBMax', 'jrnlLimICMax',
        'jrnlLimFreqMax', 'jrnlLimFreqMin', 'jrnlLimPwr', 'jrnlLimPwrPP', 'jrnlLimPwrPM', 'jrnlLimPwrQP',
        'jrnlLimPwrQM', 'jrnlRvr',
        # ---->
        # Тарифное расписание - для счетчиков СПОДЭС
        # ---->
        # Запрос - Имя календаря тарифного расписания - Активный
        "ElCalendarNameActive",
        # Запрос - Имя календаря тарифного расписания - Пассивный
        "ElCalendarNamePassive",
        # Запрос -  Сезонный профиль тарифного расписания -  Активный
        "ElCalendarSeasonActive",
        # Запрос - Сезонный профиль тарифного расписания -  Пассивный
        "ElCalendarSeasonPassive",
        # Запрос - Недельный профиль тарифного расписания - Активный
        "ElCalendarWeekActive",
        # Запрос - Недельный профиль тарифного расписания - Пассивный
        "ElCalendarWeekPassive",
        # Запрос - Суточный профиль тарифного расписания - Активный
        "ElCalendarDayActive",
        # Запрос - Суточный профиль тарифного расписания - Пассивный
        "ElCalendarDayPassive",
        # Запрос - Дата активации тарифного расписания
        "ElCalendarActivateTime",
    ]

    # Список типов данных что не требуют тагов
    _measures_with_not_tags = [
        'mRelay',
        "mTime",
        # ---->
        # Тарифное расписание - для счетчиков СПОДЭС
        # ---->
        # Запрос - Имя календаря тарифного расписания - Активный
        "ElCalendarNameActive",
        # Запрос - Имя календаря тарифного расписания - Пассивный
        "ElCalendarNamePassive",
        # Запрос -  Сезонный профиль тарифного расписания -  Активный
        "ElCalendarSeasonActive",
        # Запрос - Сезонный профиль тарифного расписания -  Пассивный
        "ElCalendarSeasonPassive",
        # Запрос - Недельный профиль тарифного расписания - Активный
        "ElCalendarWeekActive",
        # Запрос - Недельный профиль тарифного расписания - Пассивный
        "ElCalendarWeekPassive",
        # Запрос - Суточный профиль тарифного расписания - Активный
        "ElCalendarDayActive",
        # Запрос - Суточный профиль тарифного расписания - Пассивный
        "ElCalendarDayPassive",
        # Запрос - Дата активации тарифного расписания
        "ElCalendarActivateTime",
    ]

    # Список моментных показателей - не требуют времени
    _measures_with_not_time = [
        'mRelay',
        "mTime",
        'mQual',
        'mEng',
        # ---->
        # Тарифное расписание - для счетчиков СПОДЭС
        # ---->
        # Запрос - Имя календаря тарифного расписания - Активный
        "ElCalendarNameActive",
        # Запрос - Имя календаря тарифного расписания - Пассивный
        "ElCalendarNamePassive",
        # Запрос -  Сезонный профиль тарифного расписания -  Активный
        "ElCalendarSeasonActive",
        # Запрос - Сезонный профиль тарифного расписания -  Пассивный
        "ElCalendarSeasonPassive",
        # Запрос - Недельный профиль тарифного расписания - Активный
        "ElCalendarWeekActive",
        # Запрос - Недельный профиль тарифного расписания - Пассивный
        "ElCalendarWeekPassive",
        # Запрос - Суточный профиль тарифного расписания - Активный
        "ElCalendarDayActive",
        # Запрос - Суточный профиль тарифного расписания - Пассивный
        "ElCalendarDayPassive",
        # Запрос - Дата активации тарифного расписания
        "ElCalendarActivateTime",
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
        # Добавляем таги только в том случае, если в них есть необходимость
        # Все типы данных что требуют таги
        measures_do_not_tag = self._measure - set(self._measures_with_not_tags)
        # Если такие есть - без пардона добавляем
        if len(measures_do_not_tag) > 0:
            self._Settings["tags"] = list(self._tags)
        # Если таких нет, то джобавляем лишь в случае того что они есть
        else:
            if len(self._tags) > 0:
                self._Settings["tags"] = list(self._tags)

        # Добавляем время только в том случае, если в них есть необходимость
        # Все типы данных что требуют таги
        measures_with_not_time = self._measure - set(self._measures_with_not_time)
        # Если такие есть - без пардона добавляем
        if len(measures_with_not_time) > 0:
            self._Settings["time"] = list(self._time)
        # Если таких нет, то добавляем лишь в случае того что они есть
        else:
            if len(self._time) > 0:
                self._Settings["time"] = list(self._time)

        return self._Settings
# -------------------------------------------------------------------------------------------------------------
#                             Теперь такой же конструктор только с указанными Measure
# -------------------------------------------------------------------------------------------------------------
