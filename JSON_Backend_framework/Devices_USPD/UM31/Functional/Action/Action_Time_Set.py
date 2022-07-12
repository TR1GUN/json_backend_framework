# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия
from JSON_Backend_framework.Service.Template_Devices_Functions.Actions.Template_Action_Time_set import \
    TemplateActionTimeSet
# -------------------------------------------------------------------------------------------------------------


class ActionTimeSet(TemplateActionTimeSet):
    """
    Установка времени

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # _Time_Set_dict = {}
    #
    # Year = None
    # Month = None
    # Day = None
    #
    # Hour = None
    # Minute = None
    # Second = None
    #
    # TimeZone = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Установка времени

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    # Запрос времени - делаем из состояния времени
    def _read_Time_to_Device(self):
        """
        Запрашиваем данные для чтения времени - Это важно
        """

        # Поскольку это шаблон - ставим заглушку - Возвращаем пустоту
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Time import StateTime

        ReadTime = StateTime(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

        USPD_Time = ReadTime.Read()

        return USPD_Time

    # Запрос настроек
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки
        """
        data = {}
        try:
            # делаем запрос - получаем ответ
            response = self._read_Time_to_Device()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    data = answer_setting.get('time', "")

        except Exception as e:

            print("При считывании параметров возникла ошибка - Используем время системы " + str(e))

        return data

    def _define_data_set(self):
        """
        В этом методе определяем данные что будем отправлять
        """

        # Поскольку здесь нельзя задать никакие данные , вставляем данные что будем считывать
        data = self._request_setting()
        # Поскольку из всех полей нам необходимо только одно - вытаскиваем его
        return data

    # def _Create_JSON_data(self, data_read):
    #     """
    #     Здесь мы собираем наш JSON что должны отправить.
    #     """

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# data =  {"time": "2007-10-15T01:33:25+10:00"}
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
