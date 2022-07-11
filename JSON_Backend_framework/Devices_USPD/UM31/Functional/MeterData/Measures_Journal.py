# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Журналов
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data import \
    TemplateMeterData_Read_Measure


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterData_Journal(TemplateMeterData_Read_Measure):
    """
    Чтение Журналов счетчиков
    """

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Чтение Журналов счетчиков

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
    def jrnlPwr(self, ids: [None, list, str, int] = None,
                time_start: [int, str, None] = None,
                time_end: [int, str, None] = None,
                tags: [None, list, str] = None):
        """
        Чтение из БД Журнала jrnlPwr - управление питанием

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlTimeCorr(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlTimeCorr - коррекция времени электросчетчика

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlTimeCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlReset(self, ids: [None, list, str, int] = None,
                  time_start: [int, str, None] = None,
                  time_end: [int, str, None] = None,
                  tags: [None, list, str] = None
                  ):
        """
        Чтение из БД Журнала ElJrnlReset - сброс показаний

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlReset'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlC1Init(self, ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
                   tags: [None, list, str] = None
                   ):
        """
        Чтение из БД Журнала ElJrnlC1Init - инициализация первого массива профилей

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlC1Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlC2Init(self, ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
                   tags: [None, list, str] = None
                   ):
        """
        Чтение из БД Журнала ElJrnlC2Init - инициализация второго массива профилей

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlC2Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlTrfCorr(self, ids: [None, list, str, int] = None,
                    time_start: [int, str, None] = None,
                    time_end: [int, str, None] = None,
                    tags: [None, list, str] = None
                    ):
        """
        Чтение из БД Журнала ElJrnlTrfCorr - коррекция тарификатора

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlTrfCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlOpen(self, ids: [None, list, str, int] = None,
                 time_start: [int, str, None] = None,
                 time_end: [int, str, None] = None,
                 tags: [None, list, str] = None
                 ):
        """
        Чтение из БД Журнала ElJrnlOpen - открытие крышки

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlOpen'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlUnAyth(self, ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
                   tags: [None, list, str] = None
                   ):
        """
        Чтение из БД Журнала ElJrnlUnAyth - неавторизованный доступ

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlUnAyth'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrA(self, ids: [None, list, str, int] = None,
                 time_start: [int, str, None] = None,
                 time_end: [int, str, None] = None,
                 tags: [None, list, str] = None
                 ):
        """
        Чтение из БД Журнала ElJrnlPwrA - управление фазой А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlPwrA'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrB(self, ids: [None, list, str, int] = None,
                 time_start: [int, str, None] = None,
                 time_end: [int, str, None] = None,
                 tags: [None, list, str] = None
                 ):
        """
        Чтение из БД Журнала ElJrnlPwrB - управление фазой В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlPwrB'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrC(self, ids: [None, list, str, int] = None,
                 time_start: [int, str, None] = None,
                 time_end: [int, str, None] = None,
                 tags: [None, list, str] = None
                 ):
        """
        Чтение из БД Журнала ElJrnlPwrC - управление фазой С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlPwrC'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlProg(self, ids: [None, list, str, int] = None,
                 time_start: [int, str, None] = None,
                 time_end: [int, str, None] = None,
                 tags: [None, list, str] = None
                 ):
        """
        Чтение из БД Журнала ElJrnlProg - программирование

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlProg'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlRelay(self, ids: [None, list, str, int] = None,
                  time_start: [int, str, None] = None,
                  time_end: [int, str, None] = None,
                  tags: [None, list, str] = None
                  ):
        """
        Чтение из БД Журнала ElJrnlRelay - управление реле

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimESumm(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimESumm - лимит суммарной энергии

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimESumm'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf(self, ids: [None, list, str, int] = None,
                    time_start: [int, str, None] = None,
                    time_end: [int, str, None] = None,
                    tags: [None, list, str] = None
                    ):
        """
        Чтение из БД Журнала ElJrnlLimETrf - потарифиный лимит энергии

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimETrf'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf1(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimETrf1 - лимит энергии тарифа 1

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .

        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimETrf1'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf2(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimETrf2 - лимит энергии тарифа 2

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimETrf2'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf3(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimETrf3 - лимит энергии тарифа 3

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimETrf3'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimETrf4(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimETrf4 - лимит энергии тарифа 4

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimETrf4'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimUAMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUAMax - ограничение максимального напряжения фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUAMin(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUAMin - ограничение минимального напряжения фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimUBMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUBMax - ограничение максимального напряжения фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBMin(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUBMin - ограничение минимального напряжения фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUBMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUCMax - ограничение максимального напряжения фазы С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCMin(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimUCMin - ограничение минимального напряжения фазы С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUABMax(self, ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUABMax - ограничение максимального расхождения напряжения фаз А и В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUABMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUABMin(self, ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUABMin - ограничение минимального расхождения напряжения фаз А и В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUABMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBCMax(self, ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUBCMax - ограничение максимального расхождения напряжения фаз В и С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUBCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBCMin(self, ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUBCMin - ограничение минимального расхождения напряжения фаз В и С

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUBCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCAMax(self, ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUCAMax - ограничение максимального расхождения напряжения фаз С и А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUCAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCAMin(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
                      tags: [None, list, str] = None
                      ):
        """
        Чтение из БД Журнала ElJrnlLimUCAMin - ограничение минимального расхождения напряжения фаз С и А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimUCAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimIAMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimIAMax - ограничение максимального тока фазы А

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimIAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimIBMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimIBMax - ограничение максимального тока фазы В

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimIBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimICMax(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimICMax - ограничение максимального тока фазы С
        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimICMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimFreqMax(self, ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
                       tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimFreqMax - ограничение максимальной частоты сети

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimFreqMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimFreqMin(self, ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
                       tags: [None, list, str] = None
                       ):
        """
        Чтение из БД Журнала ElJrnlLimFreqMin - ограничение минимальной частоты сети

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimFreqMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimPwr(self, ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
                   tags: [None, list, str] = None
                   ):
        """
        Чтение из БД Журнала ElJrnlLimPwr - ограничение мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrPP(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimPwrPP - ограничение прямой активной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimPwrPP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrPM(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimPwrPM - ограничение прямой реактивной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimPwrPM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrQP(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimPwrQP - ограничение обратной активной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimPwrQP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrQM(self, ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
                     tags: [None, list, str] = None
                     ):
        """
        Чтение из БД Журнала ElJrnlLimPwrQM - ограничение обратной реактивной мощности

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlLimPwrQM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlRvr(self, ids: [None, list, str, int] = None,
                time_start: [int, str, None] = None,
                time_end: [int, str, None] = None,
                tags: [None, list, str] = None
                ):
        """
        Чтение из БД Журнала ElJrnlReverce - реверс

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :param tags:- int/None - измерения что запрашиваем .
        :return:
        """

        measure = 'jrnlRvr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)
