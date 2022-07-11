# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterData


class TemplateMeterData(TemplateDeviceFunctions_MeterData):
    """
    Шаблон Опроса приборов учета

    """
    # URL

    _path_url = url_path.get("MeterData")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
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


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Класс шаблон для чтения необходимых Measures
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class TemplateMeterData_Read_Measure(TemplateMeterData):

    # Основной метод
    def _read_settings(self, measure, ids, time_start, time_end, tags):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """
        from JSON_Backend_framework.FormJSON.UM31.MeterData.FormJSON_MeterData import FormJSON_MeterData
        # Формируем наш конструктор
        MeterData_JSON_settings = FormJSON_MeterData()

        MeterData_JSON_settings.add_Value(measure=measure,
                                          ids=ids,
                                          time_start=time_start,
                                          time_end=time_end,
                                          tags=tags)

        MeterData_JSON = MeterData_JSON_settings.get_JSON()
        # Если данных не спустили , то  определяем их

        response = self._Read(data=MeterData_JSON)

        return response

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
