# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение Импульсных значений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data_Moment import \
    TemplateMeterDataMoment_Read_Measure


# -------------------------------------------------------------------------------------------------------------


class MeterDataMoment_Meter(TemplateMeterDataMoment_Read_Measure):
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
    def GetTime(self,
                ids: [None, list, int] = None,
                time_start: [int, None] = None,
                time_end: [int, None] = None,
                tags: [None, list, str] = None):
        """
        Чтение параметра GetTime - Текущее показание времени прибора учета	Любое время. Одно значение

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

        measure = 'GetTime'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def GetRelay(self, ids: [None, list, int] = None,
                 time_start: [int, None] = None,
                 time_end: [int, None] = None,
                 tags: [None, list, str] = None):
        """
        Чтение параметра GetRelay - Запрос состояний реле прибора учета

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

        measure = 'GetRelay'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def GetSerial(self, ids: [None, list, int] = None,
                  time_start: [int, None] = None,
                  time_end: [int, None] = None,
                  tags: [None, list, str] = None):
        """
        Чтение параметра GetSerial - Запрос серийного номера

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

        measure = 'GetSerial'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarNameActive(self, ids: [None, list, int] = None,
                             time_start: [int, None] = None,
                             time_end: [int, None] = None,
                             tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarNameActive - Тарифное расписание для счетчиков СПОДЭС - Имя календаря тарифного
        расписания - Активный

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

        measure = 'ElCalendarNameActive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarNamePassive(self, ids: [None, list, int] = None,
                              time_start: [int, None] = None,
                              time_end: [int, None] = None,
                              tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarNamePassive - Тарифное расписание для счетчиков СПОДЭС - Имя календаря тарифного
        расписания - Пассивный

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

        measure = 'ElCalendarNamePassive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarSeasonActive(self, ids: [None, list, int] = None,
                               time_start: [int, None] = None,
                               time_end: [int, None] = None,
                               tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarSeasonActive - Тарифное расписание для счетчиков СПОДЭС -  Сезонный профиль
        тарифного расписания -  Активный

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

        measure = 'ElCalendarSeasonActive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarSeasonPassive(self, ids: [None, list, int] = None,
                                time_start: [int, None] = None,
                                time_end: [int, None] = None,
                                tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarSeasonPassive - Тарифное расписание для счетчиков СПОДЭС - Сезонный профиль
        тарифного расписания -  Пассивный

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

        measure = 'ElCalendarSeasonPassive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarWeekActive(self, ids: [None, list, int] = None,
                             time_start: [int, None] = None,
                             time_end: [int, None] = None,
                             tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarWeekActive - Тарифное расписание для счетчиков СПОДЭС - Недельный профиль
        тарифного расписания - Активный

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

        measure = 'ElCalendarWeekActive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarWeekPassive(self, ids: [None, list, int] = None,
                              time_start: [int, None] = None,
                              time_end: [int, None] = None,
                              tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarWeekPassive - Тарифное расписание для счетчиков СПОДЭС - Недельный профиль
        тарифного расписания - Пассивный

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

        measure = 'ElCalendarWeekPassive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarDayActive(self, ids: [None, list, int] = None,
                            time_start: [int, None] = None,
                            time_end: [int, None] = None,
                            tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarDayActive - Тарифное расписание для счетчиков СПОДЭС - Суточный профиль тарифного
        расписания - Активный

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

        measure = 'ElCalendarDayActive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarDayPassive(self, ids: [None, list, int] = None,
                             time_start: [int, None] = None,
                             time_end: [int, None] = None,
                             tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarDayPassive - Тарифное расписание для счетчиков СПОДЭС - Суточный профиль тарифного
        расписания - Пассивный

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

        measure = 'ElCalendarDayPassive'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def ElCalendarActivateTime(self, ids: [None, list, int] = None,
                               time_start: [int, None] = None,
                               time_end: [int, None] = None,
                               tags: [None, list, str] = None):
        """
        Чтение параметра ElCalendarActivateTime - Тарифное расписание для счетчиков СПОДЭС - Дата активации тарифного
        расписания

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

        measure = 'ElCalendarActivateTime'
        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
