# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  ШАБЛОН ЧТЕНИЯ АРХИВНЫХ ДАННЫХ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


# ПОСКОЛЬКУ ЭТО ШАБЛОН - он не имеет конструктора
class TemplateMeterArchData(TemplateFunctional):
    """

    Шаблон для считывания архивных данных

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Meter_Data_arch")
    # _path_url ="/charge/data/arch"
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

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

    def _read_settings(self, measure: str,
                       ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):
        """
         Формирование запроса на чтение данных в нужной таблице :

        :param measure: - str - Обязательное значение - типа данных что читаем. Допустимые значения :
        :param ids: - int/list/None - Meter ID  - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :return:
        """
        # Задаем тип данных
        measure = str(measure)

        # и ищем его в качестве основы -  и лишь тогда продолжаем
        if measure in self._measures:
            # Создаем шаблон запроса
            data = {'measure': measure}
            # Если задан ids
            if ids is not None:
                # если он инт - формируем список
                if type(ids) is int:
                    data["ids"] = [ids]
                # если у нас список
                if type(ids) is list:
                    data["ids"] = ids
            # Теперь формируем массив из времени если оно заданно
            if (time_start is not None) or (time_end is not None):
                # Теперь нужно сделать защиту от дебилов - проверяем на инт значение - иначе ставим значение по
                # умолчанию для старта - 0 для финиша - текущие время + 1000
                if type(time_start) is int:
                    start = time_start
                else:
                    start = 0
                if type(time_end) is int:
                    end = time_end
                else:
                    from datetime import datetime
                    from time import mktime
                    # Берем текущие время
                    end = datetime.now()
                    # переводим в UNIX time
                    end = mktime(end.timetuple())
                    # Переводим в int
                    end = int(end) + 1000
                # Теперь формируем все это
                data["time"] = [{"start": start, "end": end}]

            # работает с тэгами
            if tags is not None:
                # Если у нас один тэг -строка - обрабатываем его
                if type(tags) is str:
                    data["tags"] = [tags]
                elif type(tags) is list:
                    added = []
                    for tag in tags:
                        added.append(str(tag))
                    data["tags"] = added

            # Запаковываем бэк
            data = self._coding(data=data)
            # делаем запрос - получаем ответ

            response = self._request_POST(JSON=data)
        else:

            response = None

        return response


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Журналов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterDataArchJournal(TemplateMeterArchData):
    """
    Чтение Журналов
    """

    # # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Meter_Data_arch")
    # # _path_url ="/charge/data/arch"
    # # хедерс - Иногда нужен
    # _headers = None
    # # куки
    # _cookies = None

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlPwr(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    # tags: [None, list, str] = None
                    ):
        """
        Чтение из БД Журнала ElJrnlPwr - управление питанием

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlTimeCorr(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlTimeCorr - коррекция времени электросчетчика

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlTimeCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def PlsJrnlTimeCorr(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала PlsJrnlTimeCorr - коррекция времени концентратора импульсных счетчиков

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsJrnlTimeCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlReset(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    # tags: [None, list, str] = None
                    ):
        """
        Чтение из БД Журнала ElJrnlReset - сброс показаний

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlReset'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlC1Init(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlC1Init - инициализация первого массива профилей

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlC1Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlC2Init(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlC2Init - инициализация второго массива профилей

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlC2Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlTrfCorr(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      # tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlTrfCorr - коррекция тарификатора

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlTrfCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlOpen(self, ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
                   # tags: [None, list, str] = None
                   ):
        """
        Чтение из БД Журнала ElJrnlOpen - открытие крышки

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlOpen'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlUnAyth(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     # tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlUnAyth - неавторизованный доступ

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlUnAyth'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlPwrA(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     # tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlPwrA - управление фазой А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlPwrA'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlPwrB(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     # tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlPwrB - управление фазой В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlPwrB'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlPwrC(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     # tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlPwrC - управление фазой С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlPwrC'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlProg(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlProg - программирование

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlProg'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlRelay(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    # tags: [None, list, str] = None
                    ):
        """
        Чтение из БД Журнала ElJrnlRelay - управление реле

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimESumm(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimESumm - лимит суммарной энергии

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimESumm'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimETrf(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      # tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimETrf - потарифиный лимит энергии

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimETrf'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimETrf1(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimETrf1 - лимит энергии тарифа 1

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimETrf1'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimETrf2(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimETrf2 - лимит энергии тарифа 2

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimETrf2'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimETrf3(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimETrf3 - лимит энергии тарифа 3

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimETrf3'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlLimETrf4(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimETrf4 - лимит энергии тарифа 4

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimETrf4'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlLimUAMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUAMax - ограничение максимального напряжения фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUAMin(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUAMin - ограничение минимального напряжения фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlLimUBMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUBMax - ограничение максимального напряжения фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUBMin(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUBMin - ограничение минимального напряжения фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUBMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUCMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUCMax - ограничение максимального напряжения фазы С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUCMin(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimUCMin - ограничение минимального напряжения фазы С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUABMax(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUABMax - ограничение максимального расхождения напряжения фаз А и В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUABMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUABMin(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUABMin - ограничение минимального расхождения напряжения фаз А и В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUABMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUBCMax(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUBCMax - ограничение максимального расхождения напряжения фаз В и С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUBCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUBCMin(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUBCMin - ограничение минимального расхождения напряжения фаз В и С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUBCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUCAMax(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUCAMax - ограничение максимального расхождения напряжения фаз С и А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUCAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimUCAMin(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        # tags: [None, list, str] = None
                        ):
        """
        Чтение из БД Журнала ElJrnlLimUCAMin - ограничение минимального расхождения напряжения фаз С и А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimUCAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimIAMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimIAMax - ограничение максимального тока фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimIAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimIBMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimIBMax - ограничение максимального тока фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimIBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimICMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimICMax - ограничение максимального тока фазы С
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimICMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimFreqMax(self, ids: [None, list, int] = None,
                         time_start: [int, None] = None,
                         time_end: [int, None] = None,
                         # tags: [None, list, str] = None
                         ):
        """
        Чтение из БД Журнала ElJrnlLimFreqMax - ограничение максимальной частоты сети

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimFreqMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimFreqMin(self, ids: [None, list, int] = None,
                         time_start: [int, None] = None,
                         time_end: [int, None] = None,
                         # tags: [None, list, str] = None
                         ):
        """
        Чтение из БД Журнала ElJrnlLimFreqMin - ограничение минимальной частоты сети

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimFreqMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    def ElJrnlLimPwr(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     # tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimPwr - ограничение мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimPwrPP(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimPwrPP - ограничение прямой активной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimPwrPP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimPwrPM(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimPwrPM - ограничение прямой реактивной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimPwrPM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimPwrQP(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimPwrQP - ограничение обратной активной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimPwrQP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlLimPwrQM(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       # tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimPwrQM - ограничение обратной реактивной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlLimPwrQM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)

    # -------------------------------------------------------------------------------------------------------------
    def ElJrnlReverce(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      # tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlReverce - реверс

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElJrnlReverce'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=None)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Импульсных значений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterDataArchPulse(TemplateMeterArchData):
    """
    Чтение импульсных данных счетчиков
    """

    # # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Meter_Data_arch")
    # # _path_url ="/charge/data/arch"
    # # хедерс - Иногда нужен
    # _headers = None
    # # куки
    # _cookies = None

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    def PlsHourPulse(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
                     tags: [None, list, str] = None):
        """
        Чтение из БД параметра PlsHourPulse - Показания на начало часа

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsHourPulse'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def PlsMomentPulse(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):
        """
        Чтение из БД параметра PlsMomentPulse - Моментные показания

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания.
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsMomentPulse'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def PlsDayPulse(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    tags: [None, list, str] = None):
        """
        Чтение из БД параметра PlsDayPulse - Импульсные значения на начало дня

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsDayPulse'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def PlsMonthPulse(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      tags: [None, list, str] = None):
        """
        Чтение из БД параметра PlsMonthPulse - Импульсные значения на начало месяца

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsMonthPulse'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def PlsConfig(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
                  tags: [None, list, str] = None):
        """
        Чтение из БД параметра PlsConfig - Конфиг импульсного счетчика

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'PlsConfig'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Дискретных значений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterDataArchDigital(TemplateMeterArchData):
    """
    Чтение Дискретных данных счетчиков
    """

    # # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Meter_Data_arch")
    # # _path_url ="/charge/data/arch"
    # # хедерс - Иногда нужен
    # _headers = None
    # # куки
    # _cookies = None

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    def DigJournalState(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        tags: [None, list, str] = None):
        """
        Чтение из БД параметра DigJournalState - Архивы показаний дискретных модулей ввода/вывода

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'DigJournalState'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    def DigConfig(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
                  tags: [None, list, str] = None):
        """
        Чтение из БД параметра DigConfig - Моментная энергия

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'DigConfig'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def DigMomentState(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):
        """
        Чтение из БД параметра DigMomentState - Текущие показания дискретных модулей ввода/вывода

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'DigMomentState'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение значений Электросчетчиков
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterDataArchElectric(TemplateMeterArchData):
    """
    Чтение значений Электросчетчиков
    """

    # # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Meter_Data_arch")
    # # _path_url ="/charge/data/arch"
    # # хедерс - Иногда нужен
    # _headers = None
    # # куки
    # _cookies = None

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # -------------------------------------------------------------------------------------------------------------
    def ElMomentEnergy(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
                       tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElMomentEnergy - Моментная энергия

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElMomentEnergy'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElDayEnergy(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElDayEnergy -  Энергия на начало дня

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElDayEnergy'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElMonthEnergy(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElMonthEnergy -  Энергия на начало месяца

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElMonthEnergy'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElDayConsEnergy(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElDayConsEnergy -  Потребленная энергия на начало суток.

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElDayConsEnergy'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElMonthConsEnergy(self, ids: [None, list, int] = None,
                          time_start: [int, None] = None,
                          time_end: [int, None] = None,
                          tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElMonthConsEnergy -  Энергия потребленная на начало месяца

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElMonthConsEnergy'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElMomentQuality(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElMomentQuality - Показатели качества сети

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElMomentQuality'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElArr1ConsPower(self, ids: [None, list, int] = None,
                        time_start: [int, None] = None,
                        time_end: [int, None] = None,
                        tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElArr1ConsPower - Профиль мощности

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElArr1ConsPower'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElConfig(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
                 tags: [None, list, str] = None):
        """
        Чтение из БД параметра ElConfig - Конфиг

        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'ElConfig'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Основной класс работы с Архивными данными
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class MeterArchData(TemplateMeterArchData):
    """
    Считывание архивных данных
    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Meter_Data_arch")
    # _path_url ="/charge/data/arch"
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Журналы
    Journal = None
    # Импульсные
    Pulse = None
    # Дискретные
    Digital = None
    # Электросчетчики
    Electric = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Опрос зарядных станций

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
        # print(self.headers)
        # print(self.cookies)

    def _define_functional(self):
        """
        В этом методе делаем самое важное - определяем функционал работы по отраслям в полях этого класса

        :return:
        """

        self.Journal = MeterDataArchJournal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Digital = MeterDataArchDigital(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Pulse = MeterDataArchPulse(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Electric = MeterDataArchElectric(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    def read_data_to_measure(self, measure: str,
                             ids: [None, list, int] = None,
                             time_start: [int, None] = None,
                             time_end: [int, None] = None,
                             tags: [None, list, str] = None):
        """
         Формирование запроса на чтение данных в нужной таблице :

        :param measure: - str - Обязательное значение - типа данных что читаем. Допустимые значения :
        :param ids: - int/list/None - Meter ID  - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве.
        :return:
        """

        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    def get_measures(self):

        """
        получение словаря всех типов данных measures в формате "measures_name":"расшифровка"


        :return:
        """
        measures = {
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
                    'ElJrnlReverce': 'реверс'
        }

        return measures

    def read(self, data):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """

        # Запаковываем бэк

        data = self._coding(data=data)
        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

# -------------------------------------------------------------------------------------------------------------
Elconfig = MeterArchData().Electric.ElConfig(ids=1, time_end=10000 , time_start=1 , tags=['pId'])

print(Elconfig)


