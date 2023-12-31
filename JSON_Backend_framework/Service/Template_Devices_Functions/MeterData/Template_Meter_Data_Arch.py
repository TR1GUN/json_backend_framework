# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterData
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class TemplateMeterDataArch(TemplateDeviceFunctions_MeterData):
    """
    Шаблон Опроса приборов учета - Архивные данные

    """
    # URL

    _path_url = url_path.get("MeterData_Arch")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
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


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Класс шаблон для чтения необходимых Measures
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class TemplateMeterDataArch_Read_Measure(TemplateMeterDataArch):

    # Основной метод
    def _read_settings(self, measure, ids, time_start, time_end, tags):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """
        from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData_Arch import FormJSON_MeterDataArch
        # Формируем наш конструктор
        MeterData_JSON_settings = FormJSON_MeterDataArch()

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
