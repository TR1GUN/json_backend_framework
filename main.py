
# # ///
# #     По УРЛ определяем наш запрос - Это важно
#
# handlers = {
#         '/auth': auth,
#         # // Авторизация - Не дописано !!!!!
#         '/settings/proto/json/auth' : settingsAuthorization,
#
#         # // Переписал - Таблица Счетчиков - переделал
#         '/settings/meter/table': settingsMeterTable,
#
#         # // переписал - Настройки СИМ Карты - переделал
#         '/settings/modem/sim': settingsSIM,
#
#         # // Настройки линий питания - Переделал
#         '/settings/dout': settingsPowerLine,
#
#         # // Состояние линий питания - Добивил !!!!
#         '/state/dout': settingsPowerLineStatus,
#
#         # // переписал Настройки ethernet
#         '/settings/ip': settingsEthernet,
#         # // Настройки локального времени - Переписал
#         '/settings/time/local': settingsTimeLocal,
#
#         # // Сервера синхронизации времени - Переписал
#         '/settings/servers/sntp': settingsNTPServer,
#         # /////////////////////ДОБАВИЛ///////////////////////////
#
#         # // Условия синхронизации времени - - Не дописмал
#         '/settings/actions/sntp': settingsTimeSynchronizationConditions,
#
#         # // Журнал установки времени - - Не дописмал
#         '/jrnl/time': settingsJournalSetTime,
#
#         # ///////////////////////////////////////////////////////
#         # // Настройки расписаний - Переделал
#         '/settings/events/schdl': settingsScheduler,
#
#         # // Опрос приборов учета по событиям - Переделал
#         '/settings/actions/meter': settingsPoller,
#
#         # // - Настройки - Настройка системы событий - Переписал
#         '/settings/events/manager' : settingsEventManager,
#
#         # // - Настройки HTTP сервера - переписал
#         '/settings/servers/tcp': settingsTCPServer,
#
#         # // Задание времени - Переделал
#         '/meter/settings/time': settingsSetTimeToMeter,
#
#         # // Задание положения реле - Переписал
#         '/meter/settings/relay': settingsSetMeterRelay,
#
#         # // Считывание - Архивные показатели - Переписал
#         '/meter/data/arch': settingsMeterDataArchive,
#
#         # // Считывание - Текущие показатели - Переписал
#         '/meter/data/moment': settingsMeterDataMoment,
#
#         # // Шаблоны приборов учета - Переписал
#         '/settings/templates/meter': settingsMeterTemplates,
#
#         # //Шаблоны данных приборов учета - Переписал
#         '/settings/templates/arch': settingsMeterDataTemplates,
#
#         # /////////////////////ДОБАВИЛ///////////////////////////
#
#         # //Журнал ответов приборов учета - - Не дописмал
#         '/jrnl/meter/answ': settingsMeterResponseJournal,
#
#         # ///////////////////////////////////////////////////////
#         # информации о времени - ОБЬЕДЕНИЛ В ОДИН КЛАСС
#         # // Настройки информации о времени - получение - Переписал
#         '/state/time': settingsTimeInformation,
#         # //  информации о времени - перезапись - Переписал
#         '/action/time/set': settingsTimeInformation,
#
#         # // - Перезагрузка устройства - переписал
#         '/action/restart' : settingsDeviceRestart,
#
#         # // Настройки MQTT брокера - Переделал
#         '/settings/servers/mqtt': settingsBrokerMQTT,
#
#         # ///////////////////////////Зарядные станции//////////////////////////////////
#
#         # -Таблица зарядных станций - Переписал
#         '/settings/charge/table': settingsChargeStationTable,
#
#         # # - Состояние зарядных станций - Переписал
#         '/charge/data/arch': settingsChargeStationArchData,
#
#         # ///////////////////////////////////////////////////////
#
#         # /////////////////////ДОБАВИЛ///////////////////////////
#         # Настройки Настройки цифровых интерфейсов - Не дописмал
#         '/settings/uart': settingsUart,
#
#         # ///////////////////////////////////////////////////////
#         # Пока не завезено во фронтенд
#
#         # // - таблица MeterMessages в БД системы событий - Переписал
#         '/settings/templates/messages': settingsMeterMessages,
#
#         # // - таблица MQTTMeterMessages в БД системы событий - Переписал
#         '/settings/action/mqtt': settingsMQTTMeterMessages,
#
#         # // - таблица Calendar в БД системы событий - Переписал
#         '/settings/events/calendar': settingsCalendar,
#
#         # // - Таблица аккаунтов SMTP - Переписал
#         '/settings/smtp': settingsAccountSMTP,
#         # // -  таблица SMTPMeterMessages в БД системы событий - Переписал
#         '/settings/action/smtp': settingsSMTPMeterMessages,
#
#         # // -  таблица Email в БД системы событий - Переписал
#         '/settings/email': settingsEmail,
#
#         # ///////////////////// iec60870 ///////////////////////////
#
#         # // - iec60870 - Работа с таблицей MapIOA - Переписал
#         '/settings/iec60870/mapioa': settingsMapIOA,
#
#         # // - iec60870 - работа с таблицей ValueDescription - переписал
#         '/settings/iec60870/value_description': settingsValueDescription,
#         # // - iec60870 - работа с таблицей TemplateName - переписал
#         '/settings/iec60870/template_name': settingsTemplateName,
#         # // - iec60870 - работа с таблицей COTTypes - переписал
#         '/settings/iec60870/cot_types': settingsCOTTypes,
#         # // - iec60870 - работа с таблицей TypeIDTypes - переписал
#         '/settings/iec60870/type_id_types': settingsTypeIDTypes,
#
#         # // - iec60870 - работа с таблицей Settings - Переписал
#         '/settings/iec60870/iec60870_settings' : settingsIEC60870Settings,
#
#         # // - iec60870 - работа с таблицей IEC60870Template - Переписал
#         '/settings/iec60870/iec60870_template': settingsIEC60870Template ,
#
#         # // - iec60870 - работа с таблицей IEC60870Template - Переписал
#         '/settings/iec60870/iec60870_cot_values' :settingsIEC60870COTValues,
#             }

# --


handlers = [
        '/auth',
        # // Авторизация - Не дописано !!!!! +
        '/settings/proto/json/auth' ,

        # // Переписал - Таблица Счетчиков - переделал +
        '/settings/meter/table',

        # // переписал - Настройки СИМ Карты - переделал +
        '/settings/modem/sim',

        # // Настройки линий питания - Переделал +
        '/settings/dout',

        # // Состояние линий питания - Добивил !!!! +
        '/state/dout',

        # // переписал Настройки ethernet +
        '/settings/ip',
        # // Настройки локального времени - Переписал +
        '/settings/time/local',

        # // Сервера синхронизации времени - Переписал
        '/settings/servers/sntp',
        # /////////////////////ДОБАВИЛ///////////////////////////

        # // Условия синхронизации времени - - Не дописмал
        '/settings/actions/sntp',

        # // Журнал установки времени - - Не дописмал
        '/jrnl/time',

        # ///////////////////////////////////////////////////////
        # // Настройки расписаний - Переделал +
        '/settings/events/schdl',

        # // Опрос приборов учета по событиям - Переделал +
        '/settings/actions/meter',

        # // - Настройки - Настройка системы событий - Переписал +
        '/settings/events/manager' ,

        # // - Настройки HTTP сервера - переписал +
        '/settings/servers/tcp',

        # // Задание времени - Переделал
        '/meter/settings/time',

        # // Задание положения реле - Переписал
        '/meter/settings/relay',

        # // Считывание - Архивные показатели - Переписал
        '/meter/data/arch',
        '/meter/data/moment',
        '/settings/templates/meter',
        '/settings/templates/arch',
        '/jrnl/meter/answ',
        '/state/time',
        '/action/time/set',
        # '/action/restart' ,
        '/settings/servers/mqtt',
        '/settings/charge/table',
        '/charge/data/arch',
        '/settings/uart',
        '/settings/templates/messages',
        '/settings/action/mqtt',
        '/settings/events/calendar',
        '/settings/smtp',
        '/settings/action/smtp',
        '/settings/email',
        '/settings/iec60870/mapioa',
        '/settings/iec60870/value_description',
        '/settings/iec60870/template_name',
        '/settings/iec60870/cot_types',
        '/settings/iec60870/type_id_types',
        '/settings/iec60870/iec60870_settings',
        '/settings/iec60870/iec60870_template',
        '/settings/iec60870/iec60870_cot_values',
            ]
# --


# from USPD import USPD
#
# # Smart = USPD.UM_31_Smart(ip_address='192.168.0.1/')
#
# Smart = USPD.UM_40_Smart()
#
#
# lol = Smart.Settings.Ethernet.read_settings()
#
# print(lol)
# lol = Smart.Settings.TCP_server.rewrite_settings()
# print(lol)
#

# lol = Smart.Settings.Schedule_settings.read_settings()
#
# print(lol)
#
# lol = Smart.Settings.SNTP_server.read_settings()
#
# print(lol)
#
# lol = Smart.Settings.TCP_server.read_settings()
#
# print(lol)










# Smart40 = USPD.UM_40_Smart()
#
# lol = Smart40.Settings.Ethernet.read_settings()
#
# print(lol)
# #
# lol = Smart40.Settings.Ethernet.read_settings()
#
# print(lol)
#
# lol = Smart40.Settings.Ethernet.read_settings()
#
# print(lol)
#
# lol = Smart40.Settings.Ethernet.read_settings()
#
# print(lol)

from Service.Template_Functional import TemplateFunctional


class Test(TemplateFunctional):
    """
    Настройки расписаний

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = '/settings/actions/meter'

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None, path = ''):
        """
        Настройки расписаний

        :param cookies:
        :param headers:
        """
        self._path_url = path

        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response



test = Test(path ='/settings/meter/table')


a = test.read_settings()
print("GET\n", a)
#
# a = test.write_settings(data={'Settings': []})
# print("POST\n",a)
#
# a = test.rewrite_settings(data={'Settings': []})
# print("PUT\n",a)

# a = test.delete_settings(data={'Settings': []})
# a = test.delete_settings()
# print("DELETE\n",a)


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# for url in handlers :
#
#     lol = Test(path=url).read_settings()
#     if (lol.get('code') != 200):
#
#     # if lol.get('code') == 423 :
#         print('--------')
#         print(lol.get('code'))
#         print(url)


# '/settings/action/smtp'
# '/settings/email'
# lol = Test(path='/settings/servers/mqtt').read_settings()
# print(lol)