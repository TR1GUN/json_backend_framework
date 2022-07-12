# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
#                                     Основной класс для взаимодействия
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures_Journal import \
    MeterDataMoment_Journal
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures_Electric import \
    MeterDataMoment_Electric
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures_Pulse import MeterDataMoment_Pulse
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures_Digital import \
    MeterDataMoment_Digital
from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.Moment.Measures_Meter import MeterDataMoment_Meter

# -------------------------------------------------------------------------------------------------------------


class MeterDataMoment_MeasureRead:
    """
    Чтение Данных счетчиков - Моментные показатели

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _ip_address = None

    # Журналы
    Journal = None
    # Импульсные
    Pulse = None
    # Дискретные
    Digital = None
    # Электросчетчики
    Electric = None
    # Управление счетчиками
    Meter = None

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

        self._define_functional()

    def _define_functional(self):
        """
        В этом методе делаем самое важное - определяем функционал работы по отраслям в полях этого класса

        :return:
        """

        self.Journal = MeterDataMoment_Journal(cookies=self._cookies,
                                               headers=self._headers,
                                               ip_address=self._ip_address)

        self.Pulse = MeterDataMoment_Pulse(cookies=self._cookies,
                                           headers=self._headers,
                                           ip_address=self._ip_address)

        self.Digital = MeterDataMoment_Digital(cookies=self._cookies,
                                               headers=self._headers,
                                               ip_address=self._ip_address)

        self.Electric = MeterDataMoment_Electric(cookies=self._cookies,
                                                 headers=self._headers,
                                                 ip_address=self._ip_address)

        self.Meter = MeterDataMoment_Meter(cookies=self._cookies,
                                           headers=self._headers,
                                           ip_address=self._ip_address)

    @staticmethod
    def get_measures():

        """
        получение словаря всех типов данных measures в формате "measures_name":"расшифровка"
        :return:
        """
        measures = {
            "GetTime": "Текущее показание времени прибора учета	Любое время. Одно значение",
            "PlsGetTime": "Текущее показание времени импульсного концентратора . Любое время. Одно значение",
            "ElGetTime": "Текущее показание времени Электросчетчика	Любое время. Одно значение",
            "DigGetTime": "Текущее показание времени Дискретного прибора учета.	Любое время. Одно значение",
            "SetTime": "Установка времени прибора учета",
            "PlsSetTime": "Установка времени импульсного концентратора",
            "ElSetTime": "Установка времени Электросчетчика",
            'DigSetTime': "Установка времени Дискретного прибора учета",
            "SyncTime": "Синхронизация времени прибора учета	Требует запроса текущего времени.",
            "PlsSyncTime": "Синхронизация времени импульсного концентратора.	Требует запроса текущего времени.",
            "ElSyncTime": "Синхронизация времени Электросчетчика. Требует запроса текущего времени.",
            "DigSyncTime": "Синхронизация времени Дискретного прибора учета.	Требует запроса текущего времени.",
            "GetRelay": "Запрос состояний реле прибора учета",
            "PlsGetRelay": "Запрос состояний реле импульсного концентратора",
            "ElGetRelay": "Запрос состояний реле Электросчетчика",
            "DigGetRelay": "Запрос состояний реле Дискретного прибора учета",
            "SetRelay": "Установка состояний реле прибора учета",
            "PlsSetRelay": "Установка состояний реле импульсного концентратора",
            "ElSetRelay": "Установка состояний реле Электросчетчика",
            "DigSetRelay": "Установка состояний реле Дискретного прибора учета",
            "GetSerial": "Запрос серийного номера",
            "PlsSerial": "Запрос серийного номера импульсного концентратора",
            "ElSerial": "Запрос серийного номера Электросчетчика",
            "DigSerial": "Запрос серийного номера Дискретного прибора учета",

            'ElConfig': 'конфигурация электросчетчика',
            'DigConfig': 'конфигурация модуля дискретных вводов/выводов',
            'PlsConfig': 'конфигурация концентратора импульсных счетчиков',
            'ElMomentEnergy': 'мгновенные показания энергии электросчетчика',
            'ElMomentQuality': 'мгновенные ПКЭ',
            'ElDayEnergy': 'показания электросчетчика на начало суток',
            'ElDayConsEnergy': 'потребление электросчетчика за сутки',
            'ElMonthEnergy': 'показания электросчетчика на начало месяца',
            'ElMonthConsEnergy': 'потребление электросчетчика за месяц',
            'ElArr1ConsPower': 'профили мощности первого массива профилей мощности электросчетчика',
            'DigMomentState': 'мгновенные показания модуля дискретных вводов/выводов',
            'DigJournalState': 'архив изменения состояний модуля дискретных вводов/выводов',
            'PlsMomentPulse': 'мгновенные показания энергии концентратора импульсных счетчиков',
            'PlsDayPulse': 'показания концентратора импульсных счетчиков на начало суток',
            'PlsMonthPulse': 'показания концентратора импульсных счетчиков на начало месяца',
            'PlsHourPulse': 'показания на начало часа концентратора импульсных счетчиков',
            'ElJrnlPwr': 'управление питанием',
            'ElJrnlTimeCorr': 'коррекция времени электросчетчика',
            'PlsJrnlTimeCorr': 'коррекция времени концентратора импульсных счетчиков',
            'ElJrnlReset': 'сброс показаний',
            'ElJrnlC1Init': 'инициализация первого массива профилей',
            'ElJrnlC2Init': 'инициализация второго массива профилей',
            'ElJrnlTrfCorr': 'коррекция тарификатора',
            'ElJrnlOpen': 'открытие крышки',
            'ElJrnlUnAyth': 'неавторизованный доступ',
            'ElJrnlPwrA': 'управление фазой А',
            'ElJrnlPwrB': 'управление фазой В',
            'ElJrnlPwrC': 'управление фазой С',
            'ElJrnlProg': 'программирование',
            'ElJrnlRelay': 'управление реле',
            'ElJrnlLimESumm': 'лимит суммарной энергии',
            'ElJrnlLimETrf': 'потарифиный лимит энергии',
            'ElJrnlLimETrf1': 'лимит энергии тарифа 1',
            'ElJrnlLimETrf2': 'лимит энергии тарифа 2',
            'ElJrnlLimETrf3': 'лимит энергии тарифа 3',
            'ElJrnlLimETrf4': 'лимит энергии тарифа 4',
            'ElJrnlLimUAMax': 'ограничение максимального напряжения фазы А',
            'ElJrnlLimUAMin': 'ограничение минимального напряжения фазы А',
            'ElJrnlLimUBMax': 'ограничение максимального напряжения фазы В',
            'ElJrnlLimUBMin': 'ограничение минимального напряжения фазы В',
            'ElJrnlLimUCMax': 'ограничение максимального напряжения фазы С',
            'ElJrnlLimUCMin': 'ограничение минимального напряжения фазы С',
            'ElJrnlLimUABMax': 'ограничение максимального расхождения напряжения фаз А и В',
            'ElJrnlLimUABMin': 'ограничение минимального расхождения напряжения фаз А и В',
            'ElJrnlLimUBCMax': 'ограничение максимального расхождения напряжения фаз В и С',
            'ElJrnlLimUBCMin': 'ограничение минимального расхождения напряжения фаз В и С',
            'ElJrnlLimUCAMax': 'ограничение максимального расхождения напряжения фаз С и А',
            'ElJrnlLimUCAMin': 'ограничение минимального расхождения напряжения фаз С и А',
            'ElJrnlLimIAMax': 'ограничение максимального тока фазы А',
            'ElJrnlLimIBMax': 'ограничение максимального тока фазы В',
            'ElJrnlLimICMax': 'ограничение максимального тока фазы С',
            'ElJrnlLimFreqMax': 'ограничение максимальной частоты сети',
            'ElJrnlLimFreqMin': 'ограничение минимальной частоты сети',
            'ElJrnlLimPwr': 'ограничение мощности',
            'ElJrnlLimPwrPP': 'ограничение прямой активной мощности',
            'ElJrnlLimPwrPM': 'ограничение прямой реактивной мощности',
            'ElJrnlLimPwrQP': 'ограничение обратной реактивной мощности',
            'ElJrnlReverce': 'реверс',

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
