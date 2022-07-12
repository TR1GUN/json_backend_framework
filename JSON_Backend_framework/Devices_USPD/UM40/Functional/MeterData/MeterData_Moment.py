
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                        Чтение Данных счетчиков - Моментные показатели
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия


from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_Moment import TemplateMeterDataMoment
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures import MeterDataMoment_MeasureRead
from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData_Moment import FormJSON_MeterDataMoment


# -------------------------------------------------------------------------------------------------------------
#                 Основной класс с конструктором JSON в зависимости от того что мы читаем
# -------------------------------------------------------------------------------------------------------------
class MeterDataMoment(TemplateMeterDataMoment):
    """
    Чтение Данных счетчиков - Моментные показатели

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Генерация JSON
    MeterData_JSON = None

    # Запрос Отдельных Measures

    Measures = None

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

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Чтение Данных счетчиков - Моментные показатели

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        self.Measures = MeterDataMoment_MeasureRead(cookies=cookies, headers=headers, ip_address=ip_address)

        # Сбрасываем настройки JSON
        self._define_JSON()

    # Основной метод который торчит наружу
    def Read_MeterData(self, data=None):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """

        # Если данных не спустили , то  определяем их
        if data is None:
            data = self.MeterData_JSON.get_JSON()
            # Сбрасываем настройки JSON
            self._define_JSON()

        response = self._Read(data=data)

        return response

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.MeterData_JSON = FormJSON_MeterDataMoment()

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {
# 	        "ids":[1],
# 	        "tags":["A+0"],
# 	        "time":[{"start":1649100459 ,"end":1650903063}],
# 	        "measures":["ElConfig"]
# 	     }
# -------------------------------------------------------------------------------------------------------------
