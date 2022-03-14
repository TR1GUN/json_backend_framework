# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_moment import TemplateMeterDataMoment , TemplateMeterDataMoment_Read_Measure

from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData import FormJSON_MeterData


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Журналов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterDataMoment_Journal(TemplateMeterDataMoment_Read_Measure):
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
class MeterDataMoment_Pulse(TemplateMeterDataMoment_Read_Measure):
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
class MeterDataMoment_Digital(TemplateMeterDataMoment_Read_Measure):
    """
    Чтение Дискретных данных счетчиков
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
class MeterDataMoment_Electric(TemplateMeterDataMoment_Read_Measure):
    """
    Чтение значений Электросчетчиков
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
#                                         Чтение Данных счетчиков
#                                     Основной класс для взаимодействия
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class MeterDataMoment_MeasureRead:
    """
    Чтение Данных счетчиков

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _ip_address =None
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

        self.Journal = MeterDataMoment_Journal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Digital = MeterDataMoment_Digital(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Pulse = MeterDataMoment_Pulse(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.Electric = MeterDataMoment_Electric(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


# -------------------------------------------------------------------------------------------------------------
#                 Основной класс с конструктором JSON в зависимости от того что мы читаем
# -------------------------------------------------------------------------------------------------------------
class MeterDataMoment(TemplateMeterDataMoment):
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

        self.Measures = MeterDataMoment_MeasureRead(cookies=cookies, headers=headers, ip_address=ip_address)

        # Сбрасываем настройки JSON
        self._define_JSON()

    @staticmethod
    def get_measures():

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
