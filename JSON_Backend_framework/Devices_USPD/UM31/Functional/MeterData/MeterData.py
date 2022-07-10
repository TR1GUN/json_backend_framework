# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_arch import \
    TemplateMeterDataArch, TemplateMeterDataArch_Read_Measure
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data import TemplateMeterData, \
    TemplateMeterData_Read_Measure

from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData import FormJSON_MeterData


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

    # Настройки
    MeterData = None

    # Запрорс Отдельных Measures

    Measures = None

    # Доступные типы данных
    _measures = [
        'mRelay',
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
        'jrnlLimPwrQM', 'jrnlRvr'

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

    @staticmethod
    def get_measures():

        """
        получение словаря всех типов данных measures в формате "measures_name":"расшифровка"


        :return:
        """
        measures = {
            'mRelay': 'текущие состояния реле',
            'mQual': 'текущие ПКЭ',
            'mEng': 'текущие показания энергии',
            'aCfg': 'конфигурация',
            'aEng': 'срезы показаний энергии',
            'aQual': 'срезы ПКЭ',
            'aDay': 'показания на начало суток',
            'aDayCons': 'потребление за сутки',
            'aMonth': 'показания на начало месяца',
            'aMonthCons': 'потребление за месяц',
            'aCons': 'профили мощности',
            'aHour': 'Показания на начало часа',
            'jrnlPwr': 'журнал управление питанием',
            'jrnlTimeCorr': 'журнал коррекция времени',
            'jrnlReset': 'журнал сброс показаний',
            'jrnlC1Init': 'журнал инициализация первого массива профилей',
            'jrnlC2Init': 'журнал инициализация второго массива профилей',
            'jrnlTrfCorr': 'журнал коррекция тарификатора',
            'jrnlOpen': 'журнал открытие крышки',
            'jrnlUnAyth': 'журнал неавторизованный доступ',
            'jrnlPwrA': 'журнал управление фазой А',
            'jrnlPwrB': 'журнал управление фазой В',
            'jrnlPwrC': 'журнал управление фазой С',
            'jrnlProg': 'журнал программирование',
            'jrnlRelay': 'журнал управление реле',
            'jrnlLimESumm': 'журнал лимит суммарной энергии',
            'jrnlLimETrf': 'журнал потарифный лимит энергии',
            'jrnlLimETrf1': 'журнал лимит энергии тарифа 1',
            'jrnlLimETrf2': 'журнал лимит энергии тарифа 2',
            'jrnlLimETrf3': 'журнал лимит энергии тарифа 3',
            'jrnlLimETrf4': 'журнал лимит энергии тарифа 4',
            'jrnlLimUAMax': 'журнал ограничение максимального напряжения фазы А',
            'jrnlLimUAMin': 'журнал ограничение минимального напряжения фазы А',
            'jrnlLimUBMax': 'журнал ограничение максимального напряжения фазы В',
            'jrnlLimUBMin': 'журнал ограничение минимального напряжения фазы В',
            'jrnlLimUCMax': 'журнал ограничение максимального напряжения фазы С',
            'jrnlLimUCMin': 'журнал ограничение минимального напряжения фазы С',
            'jrnlLimUABMax': 'журнал ограничение максимального расхождения напряжения фаз А и В',
            'jrnlLimUABMin': 'журнал ограничение минимального расхождения напряжения фаз А и В',
            'jrnlLimUBCMax': 'журнал ограничение максимального расхождения напряжения фаз В и С',
            'jrnlLimUBCMin': 'журнал ограничение минимального расхождения напряжения фаз В и С',
            'jrnlLimUCAMax': 'журнал ограничение максимального расхождения напряжения фаз С и А',
            'jrnlLimUCAMin': 'журнал ограничение минимального расхождения напряжения фаз С и А',
            'jrnlLimIAMax': 'журнал ограничение максимального тока фазы А',
            'jrnlLimIBMax': 'журнал ограничение максимального тока фазы В',
            'jrnlLimICMax': 'журнал ограничение максимального тока фазы С',
            'jrnlLimFreqMax': 'журнал ограничение максимальной частоты сети',
            'jrnlLimFreqMin': 'журнал ограничение минимальной частоты сети',
            'jrnlLimPwr': 'ограничение мощности',
            'jrnlLimPwrPP': 'журнал ограничение прямой активной мощности',
            'jrnlLimPwrPM': 'журнал ограничение прямой реактивной мощности',
            'jrnlLimPwrQP': 'журнал ограничение обратной активной мощности',
            'jrnlLimPwrQM': 'журнал ограничение обратной реактивной мощности',
            'jrnlRvr': 'журнал реверс',
        }

        return measures

    # Основной метод который торчит наружу
    def Read_MeterData(self, data=None):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """

        # Если данных не спустили , то  определяем их
        if data is None:
            data = self.MeterData.get_settings()
            # Сбрасываем настройки JSON
            self._define_JSON()

        response = self._Read(data=data)

        return response

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.MeterData = FormJSON_MeterData()
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
