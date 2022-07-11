# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Чтение значений Электросчетчиков - Текущие
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.MeterData.Template_Meter_Data import \
    TemplateMeterData_Read_Measure


# -------------------------------------------------------------------------------------------------------------
class MeterData_Moment(TemplateMeterData_Read_Measure):
    """
    Чтение значений Счетчиков - Текущие
    """

    # Поскольку мы наследуемся, то делаем конструктор
    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Чтение значений Счетчиков - Текущие

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
    def mRelay(self, ids: [None, list, str, int] = None,
               # time_start: [int, str, None] = None,
               # time_end: [int, str, None] = None,
               # tags: [None, list, str] = None
               ):
        """
        Чтение из БД параметра mRelay - Текущее показание реле

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве. - Вырезано

        :param time_end: - int/None - Время конца считывания .
        Если None - и задано время старта - то ставиться текущая дата  + 1000.
        Если время старта не задано то поле time не формируется - Вырезано
        :param time_start:- int/None - Время старта считывания .
        Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется - Вырезано
        :return:
        """

        measure = 'mRelay'
        time_start = None
        time_end = None
        tags = None

        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------
    def mTime(self, ids: [None, list, str, int] = None,
              # time_start: [int, str, None] = None,
              # time_end: [int, str, None] = None,
              # tags: [None, list, str] = None
              ):
        """
        Чтение из БД параметра mTime - Текущее показание времени приьоров учета

        :param ids: - int/list/None - ID станций - Если None, то не формируется поле ids
        :param tags: - None/list/str - Тэги что запрашиваем - Если None, то тэг не ставиться,
                                        если строка - то тэг что указан в строке,
                                        если список , то список тэгов что указан в массиве. - Вырезано

        :param time_end: - int/None - Время конца считывания . Если None - и задано время старта - то ставиться
        текущая дата  + 1000. Если время старта не задано то поле time не формируется - Вырезано :param time_start:-
        int/None - Время старта считывания . Если None - и задано время конца - то ставиться 0. Если время конца не
        задано то поле time не формируется - Вырезано
         :return:
        """

        measure = 'mTime'
        time_start = None
        time_end = None
        tags = None

        return self._read_settings(measure=measure, ids=ids, time_start=time_start, time_end=time_end, tags=tags)

    # -------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------
    def mQual(self, ids: [None, list, str, int] = None,
              time_start: [int, str, None] = None,
              time_end: [int, str, None] = None,
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
    def mEng(self, ids: [None, list, str, int] = None,
             time_start: [int, str, None] = None,
             time_end: [int, str, None] = None,
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
