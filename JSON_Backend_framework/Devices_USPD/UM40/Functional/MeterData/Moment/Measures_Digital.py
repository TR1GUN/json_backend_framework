# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Дискретных значений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_Moment import \
    TemplateMeterDataMoment_Read_Measure
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
    def DigJournalState(self,
                        ids: [None, list, str, int] = None,
                        time_start: [int, str, None] = None,
                        time_end: [int, str, None] = None,
                        tags: [None, list, str] = None):
        """
        Чтение параметра DigJournalState - Архивы показаний дискретных модулей ввода/вывода

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

    def DigConfig(self,
                  ids: [None, list, str, int] = None,
                  time_start: [int, str, None] = None,
                  time_end: [int, str, None] = None,
                  tags: [None, list, str] = None):
        """
        Чтение параметра DigConfig - Моментная энергия

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
    def DigMomentState(self,
                       ids: [None, list, str, int] = None,
                       time_start: [int, str, None] = None,
                       time_end: [int, str, None] = None,
                       tags: [None, list, str] = None):
        """
        Чтение параметра DigMomentState - Текущие показания дискретных модулей ввода/вывода

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
    def DigGetTime(self,
                   ids: [None, list, int] = None,
                   time_start: [int, None] = None,
                   time_end: [int, None] = None,
                   tags: [None, list, str] = None):
        """
        Чтение параметра DigGetTime - Текущее показание времени Дискретного прибора учета.	Любое время. Одно значение

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

        measure = 'DigGetTime'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def DigGetRelay(self,
                    ids: [None, list, int] = None,
                    time_start: [int, None] = None,
                    time_end: [int, None] = None,
                    tags: [None, list, str] = None):
        """
        Чтение параметра DigGetRelay - Запрос состояний реле Дискретного прибора учета

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

        measure = 'DigGetRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def DigSerial(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
                  tags: [None, list, str] = None):
        """
        Чтение параметра DigSerial - Запрос серийного номера Дискретного прибора учета

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

        measure = 'DigSerial'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
