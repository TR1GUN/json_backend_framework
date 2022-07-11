# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
#                                     Основной класс для взаимодействия
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Journal import MeterData_Journal
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Moment import MeterData_Moment
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Archive import MeterData_Arch


# -------------------------------------------------------------------------------------------------------------


class MeterData_MeasureRead:
    """
    Чтение Данных счетчиков

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _ip_address = None
    # Журналы
    Journal = None

    # Данные со счетчика - Моментные показатели
    MeterData_Moment = None
    # Данные со счетчика - Архивные показатели
    MeterData_Arch = None

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

        self._define_functional()

    def _define_functional(self):
        """
        В этом методе делаем самое важное - определяем функционал работы по отраслям в полях этого класса

        :return:
        """

        self.Journal = MeterData_Journal(cookies=self._cookies,
                                         headers=self._headers,
                                         ip_address=self._ip_address)
        self.MeterData_Moment = MeterData_Moment(cookies=self._cookies,
                                                 headers=self._headers,
                                                 ip_address=self._ip_address)
        self.MeterData_Arch = MeterData_Arch(cookies=self._cookies,
                                             headers=self._headers,
                                             ip_address=self._ip_address)

    @staticmethod
    def get_measures():

        """
        получение словаря всех типов данных measures в формате "measures_name":"расшифровка"
        :return:
        """
        measures = {
            'mRelay': 'текущие состояния реле',
            "mTime": 'текущие время счетчика',
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
            "ElCalendarNameActive": 'Тарифное расписание для счетчиков СПОДЭС - Имя календаря тарифного расписания - '
                                    'Активный',
            "ElCalendarNamePassive": 'Тарифное расписание для счетчиков СПОДЭС - Имя календаря тарифного расписания - '
                                     'Пассивный',
            "ElCalendarSeasonActive": 'Тарифное расписание для счетчиков СПОДЭС -  Сезонный профиль тарифного '
                                      'расписания -  Активный',
            "ElCalendarSeasonPassive": 'Тарифное расписание для счетчиков СПОДЭС - Сезонный профиль тарифного '
                                       'расписания -  Пассивный',
            "ElCalendarWeekActive": 'Тарифное расписание для счетчиков СПОДЭС - Недельный профиль тарифного '
                                    'расписания - Активный',
            "ElCalendarWeekPassive": 'Тарифное расписание для счетчиков СПОДЭС - Недельный профиль тарифного '
                                     'расписания - Пассивный',
            "ElCalendarDayActive": 'Тарифное расписание для счетчиков СПОДЭС - Суточный профиль тарифного расписания '
                                   '- Активный',
            "ElCalendarDayPassive": 'Тарифное расписание для счетчиков СПОДЭС - Суточный профиль тарифного расписания '
                                    '- Пассивный',
            "ElCalendarActivateTime": 'Тарифное расписание для счетчиков СПОДЭС - Дата активации тарифного расписания',
        }

        return measures
