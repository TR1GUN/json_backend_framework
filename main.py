
# iec60870

# TODO this is HTTP stuff
def auth(env):
    return '200 OK', ""


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

from Service.Request_GET import GET

# print(len(handlers))
# i = 0
# for url in handlers:
#
#         result = GET(url=url).Result()
#         if result.get("code") != 200:
#
#                 print(url, result)
#                 i = i + 1
#
#         else:
#                 print("Успешно", url)
#
# print(i)

 # /settings/servers/sntp -  Не существует /etc/chrony/uspd.conf
# /settings/actions/sntp - Надо дописать

url = "/settings/ip"
result = GET(url=url).Result()
print(result)


# from genson import SchemaBuilder
# import json
#
# builder = SchemaBuilder()
#
# # datastore = {"lol":"lol"}
# # datastore = json.dumps(datastore)
#
# datastore = {"settings":[{"id":1,"name":"_name_"},{"id":2,"name":"_name_"}],"table":"COTTypes", "res":0}
# datastore = json.dumps(datastore)
#
# builder.add_object(datastore)
# #
# # builder.to_schema()
#
# empty_schema = builder.to_schema()
# print(json.dumps(empty_schema))

# from jschon import JSONSchema
# empty_schema = JSONSchema({"lol":"lol"})
# print(empty_schema)