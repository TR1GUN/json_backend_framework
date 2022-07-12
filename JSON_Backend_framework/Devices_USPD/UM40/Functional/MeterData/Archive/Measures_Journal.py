# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Журналов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_Arch import \
    TemplateMeterDataArch_Read_Measure


# -------------------------------------------------------------------------------------------------------------


class MeterDataArch_Journal(TemplateMeterDataArch_Read_Measure):
    """
    Чтение Журналов
    """

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
    def ElJrnlPwr(self,
                  ids: [None, list, str, int] = None,
                  time_start: [int, str, None] = None,
                  time_end: [int, str, None] = None,
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
    def ElJrnlTimeCorr(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def PlsJrnlTimeCorr(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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

    def ElJrnlReset(self,
                    ids: [None, list, str, int] = None,
                    time_start: [int, str, None] = None,
                    time_end: [int, str, None] = None,
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

    def ElJrnlC1Init(self,
                     ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
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
    def ElJrnlC2Init(self,
                     ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
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
    def ElJrnlTrfCorr(self,
                      ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
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
    def ElJrnlOpen(self,
                   ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
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

    def ElJrnlUnAyth(self,
                     ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
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
    def ElJrnlPwrA(self,
                   ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
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
    def ElJrnlPwrB(self,
                   ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
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
    def ElJrnlPwrC(self,
                   ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
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
    def ElJrnlProg(self,
                   ids: [None, list, str, int] = None,
                   time_start: [int, str, None] = None,
                   time_end: [int, str, None] = None,
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
    def ElJrnlRelay(self,
                    ids: [None, list, str, int] = None,
                    time_start: [int, str, None] = None,
                    time_end: [int, str, None] = None,
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
    def ElJrnlLimESumm(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimETrf(self,
                      ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
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
    def ElJrnlLimETrf1(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimETrf2(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimETrf3(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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

    def ElJrnlLimETrf4(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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

    def ElJrnlLimUAMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimUAMin(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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

    def ElJrnlLimUBMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimUBMin(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimUCMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimUCMin(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimUABMax(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimUABMin(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimUBCMax(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimUBCMin(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimUCAMax(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimUCAMin(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
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
    def ElJrnlLimIAMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimIBMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimICMax(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimFreqMax(self,
                         ids: [None, list, str, int] = None,
                         time_start: [int, str, None] = None,
                         time_end: [int, str, None] = None,
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
    def ElJrnlLimFreqMin(self,
                         ids: [None, list, str, int] = None,
                         time_start: [int, str, None] = None,
                         time_end: [int, str, None] = None,
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

    def ElJrnlLimPwr(self,
                     ids: [None, list, str, int] = None,
                     time_start: [int, str, None] = None,
                     time_end: [int, str, None] = None,
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
    def ElJrnlLimPwrPP(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimPwrPM(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimPwrQP(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlLimPwrQM(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
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
    def ElJrnlReverce(self,
                      ids: [None, list, str, int] = None,
                      time_start: [int, str, None] = None,
                      time_end: [int, str, None] = None,
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
