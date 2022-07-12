# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterData
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class TemplateMeterDataMoment(TemplateDeviceFunctions_MeterData):
    """
    Шаблон Опроса приборов учета - Моментные данные

    """
    # URL

    _path_url = url_path.get("MeterData_Moment")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Доступные типы данных
    _measures = [

        'GetTime',
        'PlsGetTime',
        'ElGetTime',
        'DigGetTime'

        'GetRelay',
        'PlsGetRelay',
        'ElGetRelay',
        'DigGetRelay',

        'GetSerial',
        'PlsSerial',
        'ElSerial',
        'DigSerial'


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
        'PlsJrnlTimeCorr',
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
class TemplateMeterDataMoment_Read_Measure(TemplateMeterDataMoment):

    # Основной метод
    def _read_settings(self, measure, ids, time_start, time_end, tags):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """
        from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData_Moment import FormJSON_MeterDataMoment
        # Формируем наш конструктор
        MeterData_JSON_settings = FormJSON_MeterDataMoment()

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
