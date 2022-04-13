# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_arch import \
    TemplateMeterDataArch, TemplateMeterDataArch_Read_Measure
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data import TemplateMeterData, TemplateMeterData_Read_Measure

from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData import FormJSON_MeterData


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Журналов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterData_Journal(TemplateMeterDataArch_Read_Measure):
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
    def jrnlPwr(self, ids: [None, list, int] = None,
                time_start: [int, None] = None,
                time_end: [int, None] = None,
                tags: [None, list, str] = None
                ):
        """
        Чтение из БД Журнала jrnlPwr - управление питанием

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется
        :return:
        """

        measure = 'jrnlPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlTimeCorr(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlTimeCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlReset(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlReset'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlC1Init(self, ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlC1Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlC2Init(self, ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlC2Init'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlTrfCorr(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlTrfCorr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlOpen(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlOpen'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlUnAyth(self, ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlUnAyth'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrA(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlPwrA'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrB(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlPwrB'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlPwrC(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlPwrC'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlProg(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlProg'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlRelay(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimESumm(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimESumm'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf(self, ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimETrf'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf1(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimETrf1'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf2(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimETrf2'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimETrf3(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimETrf3'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimETrf4(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimETrf4'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimUAMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUAMin(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimUBMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBMin(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUBMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCMin(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUABMax(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUABMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUABMin(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUABMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBCMax(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUBCMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUBCMin(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUBCMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimUCAMax(self, ids: [None, list, int] = None,
                      time_start: [int, None] = None,
                      time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimUCAMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimIAMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimIAMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimIBMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimIBMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimICMax(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimICMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimFreqMax(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimFreqMax'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimFreqMin(self, ids: [None, list, int] = None,
                       time_start: [int, None] = None,
                       time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimFreqMin'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    def jrnlLimPwr(self, ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimPwr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrPP(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimPwrPP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrPM(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimPwrPM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrQP(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimPwrQP'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlLimPwrQM(self, ids: [None, list, int] = None,
                     time_start: [int, None] = None,
                     time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlLimPwrQM'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def jrnlRvr(self, ids: [None, list, int] = None,
                time_start: [int, None] = None,
                time_end: [int, None] = None,
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
        :return:
        """

        measure = 'jrnlRvr'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение значений Электросчетчиков - Текущие
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterData_Moment(TemplateMeterDataArch_Read_Measure):
    """
    Чтение значений Электросчетчиков - Текущие
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
    def mRelay(self, ids: [None, list, int] = None,
               time_start: [int, None] = None,
               time_end: [int, None] = None,
               tags: [None, list, str] = None):
        """
        Чтение из БД параметра mRelay - Текущее показание реле

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

        measure = 'mRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def mQual(self, ids: [None, list, int] = None,
              time_start: [int, None] = None,
              time_end: [int, None] = None,
              tags: [None, list, str] = None):
        """
        Чтение из БД параметра mQual - текущие ПКЭ

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

        measure = 'mQual'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def mEng(self, ids: [None, list, int] = None,
             time_start: [int, None] = None,
             time_end: [int, None] = None,
             tags: [None, list, str] = None):
        """
        Чтение из БД параметра mEng - текущие показания энергии

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

        measure = 'mEng'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение значений Электросчетчиков - Архивные
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class MeterData_Arch(TemplateMeterDataArch_Read_Measure):
    """
    Чтение значений Электросчетчиков - Архивные
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
    def aEng(self, ids: [None, list, int] = None,
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

        measure = 'aEng'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aDay(self, ids: [None, list, int] = None,
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

        measure = 'aDay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aMonth(self, ids: [None, list, int] = None,
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

        measure = 'aMonth'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aDayCons(self, ids: [None, list, int] = None,
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

        measure = 'aDayCons'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aMonthCons(self, ids: [None, list, int] = None,
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

        measure = 'aMonthCons'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aQual(self, ids: [None, list, int] = None,
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

        measure = 'aQual'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aCons(self, ids: [None, list, int] = None,
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

        measure = 'aCons'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aCfg(self, ids: [None, list, int] = None,
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

        measure = 'aCfg'

        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def aHour(self, ids: [None, list, int] = None,
              time_start: [int, None] = None,
              time_end: [int, None] = None,
              tags: [None, list, str] = None):
        """
        Чтение из БД параметра aHour - Показания на начало часа

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

        measure = 'aHour'

        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
#                                     Основной класс для взаимодействия
# -------------------------------------------------------------------------------------------------------------
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

        self.Journal = MeterData_Journal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        self.MeterData_Moment = MeterData_Moment(cookies=self._cookies, headers=self._headers,
                                                 ip_address=self._ip_address)
        self.MeterData_Arch = MeterData_Arch(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)


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
