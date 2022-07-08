# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                        Шаблон установки времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Actions_Set


class TemplateActionTimeSet(TemplateDeviceFunctions_Actions_Set):
    """
    Шаблон Установки времени

    """
    # URL

    _path_url = url_path.get("Set_time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    _Time_Set_dict = {}

    # def _date_time_now(self):
    #     """
    #     Вспомогательный метод Получающий сегодняшние время сейчас
    #     и заполняет правильно им Time_Set_dict
    #     :return:
    #     """
    #     # Вспомомгательный метод Получающий сегоднянее время сейчас
    #
    #     import datetime
    #     # Year Month Day Hour Minute Second Time_Zone
    #     self._Time_Set_dict = {}
    #
    #     date_now = datetime.datetime.now(datetime.timezone.utc).astimezone().replace(microsecond=0)
    #     self._Time_Set_dict['Year'] = str(date_now.year)
    #     self._Time_Set_dict['Month'] = str(date_now.month)
    #     self._Time_Set_dict['Day'] = str(date_now.day)
    #     self._Time_Set_dict['Hour'] = str(date_now.hour)
    #     self._Time_Set_dict['Minute'] = str(date_now.minute)
    #     self._Time_Set_dict['Second'] = str(date_now.second)
    #     # self._Time_Set_dict['Time_Zone'] = str(date_now.timetz())
    #     Time_Zone = date_now.strftime('%z')
    #     # Если наша строка не пустая - разделяем точкой
    #     if len(Time_Zone) > 0:
    #         Time_Zone = Time_Zone[:3] + ':' + Time_Zone[3:]
    #     self._Time_Set_dict['Time_Zone'] = str(Time_Zone)

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
                    data = answer_setting

        except Exception as e:

            print("При считывании параметров возникла ошибка - Используем время системы " + str(e))

        return data

    def _read_Time_to_Device(self):

        """
        Запрашиваем данные для чтения времени - Это важно

        """

        # Поскольку это шаблон - ставим заглушку - Возвращаем пустоту

        return {}

    # def _SystemTime(self):
    #     """
    #     Смотрим чис
    #     """
    #     # Первое что делаем - ПОлучаем ТЕКУЩЕЕ ВРЕМЯ
    #     self._date_time_now()
    #     # И формируем из этого поле data
    #
    #     data = self._Create_JSON_data()
    #
    #     return data

    # def _Create_JSON_data(self):
    #
    #     Year = self._Time_Set_dict['Year']
    #     Month = self._Time_Set_dict['Month']
    #     Day = self._Time_Set_dict['Day']
    #     Hour = self._Time_Set_dict['Hour']
    #     Minute = self._Time_Set_dict['Minute']
    #     Second = self._Time_Set_dict['Second']
    #     Time_Zone = self._Time_Set_dict['Time_Zone']
    #     # Теперь собираем в единую стрингу
    #     Time_string = Year + '-' + Month + '-' + Day + 'T' + Hour + ':' + Minute + ':' + Second + Time_Zone
    #
    #     data = {"time": Time_string}

        # return data

    # ОСНОВНОЙ МЕТОД КОТОРЫЙ ТОРЧИТ СНАРУЖИ
    def Set(self, data=None):
        """
        Перезаписываем данные - PUT

        Формат JSON
        {"time": "2007-10-15T01:33:25+10:00"}

        :param data: JSON На запись , который игнорирует

        """
        # Если мы дали пустоту , то определяем значения что заданы
        if data is None:
            data = self._define_data_set()
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def _define_data_set(self):
        """
        В этом методе определяем данные что будем отправлять
        """

        # Поскольку здесь нельзя задать никакие данные , вставляем данные что будем считывать
        data = self._request_setting()

        return data

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
