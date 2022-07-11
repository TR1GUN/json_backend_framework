# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия


from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data import TemplateMeterData
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures import MeterData_MeasureRead
from JSON_Backend_framework.FormJSON.UM31.MeterData.FormJSON_MeterData import FormJSON_MeterData


# -------------------------------------------------------------------------------------------------------------
#                 Основной класс с конструктором JSON в зависимости от того что мы читаем
# -------------------------------------------------------------------------------------------------------------
class MeterData(TemplateMeterData):
    """
    Чтение Данных счетчиков

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

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Чтение Данных счетчиков

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        self.Measures = MeterData_MeasureRead(cookies=cookies, headers=headers, ip_address=ip_address)

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
        self.MeterData_JSON = FormJSON_MeterData()
# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {
# 	        "ids":[1],
# 	        "tags":["A+0"],
# 	        "time":[{"start":"2018-09-03T14:17:33+03:00","end":"2018-09-03T14:17:33+03:00"}],
# 	        "measures":["aDay"]
# 	     }
# -------------------------------------------------------------------------------------------------------------
