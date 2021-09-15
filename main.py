

print('lol')

# iec60870

# =====> ПЕРЕПИСАННОЕ
from SettingsUSPD.Meter_devices.MeterTable.MeterTable import settingsMeterTable
from SettingsUSPD.Digital_Interface_Settings.DigitalInterfaceSettings import settingsUart
from SettingsUSPD.Meter_devices.MeterDataTemplatesTable.MeterDataTemplatesTable import settingsMeterDataTemplates
from SettingsUSPD.Meter_devices.MeterTemplatesTable.MeterTemplatesTable import settingsMeterTemplates
from SettingsUSPD.Authorization_Settings.AuthorizationSettings import settingsAuthorization
from SettingsUSPD.Modem.Sim_Settings.SimSettings import settingsSIM
from SettingsUSPD.Network_connections.Ethernet_Settings.EthernetSettings import settingsEthernet
from SettingsUSPD.Network_connections.HTTP_Server_Settings.HTTPSettings import settingsTCPServer
from SettingsUSPD.Event_System_Settings.Event_Manager import settingsEventManager
from SettingsUSPD.Messages.Sending_Messages.MQTT.Broker_Settings_MQTT import settingsBrokerMQTT
from SettingsUSPD.PowerLines.Power_Line_Settings import settingsPowerLine
from SettingsUSPD.PowerLines.Power_Line_Status import settingsPowerLineStatus
from SettingsUSPD.Local_Time_Management_Settings.Time_Information import settingsTimeInformation
from SettingsUSPD.Local_Time_Management_Settings.Local_Time_Settings import settingsTimeLocal
from SettingsUSPD.Local_Time_Management_Settings.Scheduler import settingsScheduler
from SettingsUSPD.Local_Time_Management_Settings.Time_Synchronization_Servers import settingsNTPServer
from SettingsUSPD.Local_Time_Management_Settings.Time_Synchronization_Conditions import \
    settingsTimeSynchronizationConditions
from SettingsUSPD.Local_Time_Management_Settings.Journal_Set_Time import settingsJournalSetTime
from SettingsUSPD.Meter_devices.MeterResponseJournal.MeterResponseJournal import settingsMeterResponseJournal
from SettingsUSPD.Meter_devices.PollingMeteringDevicesByEvents.Poller import settingsPoller
from SettingsUSPD.Meter_devices.Meter_Data.Meter_Data_Moment import settingsMeterDataMoment
from SettingsUSPD.Meter_devices.Meter_Data.Meter_Data_Arch import settingsMeterDataArchive
from SettingsUSPD.Charge_Station.ChargeStationTable import settingsChargeStationTable
from SettingsUSPD.Charge_Station.ChargeStationArchData import settingsChargeStationArchData
from SettingsUSPD.Meter_devices.ManagementMeter.Time.SetTimeToMeter import settingsSetTimeToMeter
from SettingsUSPD.Meter_devices.ManagementMeter.Relay.SetMeterRelay import settingsSetMeterRelay
from SettingsUSPD.DeviceRestart.DeviceRestart import settingsDeviceRestart
from SettingsUSPD.NonFrontend.MeterMessagesTable import settingsMeterMessages
from SettingsUSPD.NonFrontend.MQTTMeterMessagesTable import settingsMQTTMeterMessages
from SettingsUSPD.NonFrontend.CalendarTable import settingsCalendar
from SettingsUSPD.NonFrontend.SMTPAccountTable import settingsAccountSMTP
from SettingsUSPD.NonFrontend.SMTPMeterMessagesTable import settingsSMTPMeterMessages
from SettingsUSPD.NonFrontend.EmailTable import settingsEmail
from SettingsUSPD.iec60870.MapIOATable import settingsMapIOA
from SettingsUSPD.iec60870.ValueDescriptionTable import settingsValueDescription
from SettingsUSPD.iec60870.TemplateNameTable import settingsTemplateName
from SettingsUSPD.iec60870.COTTypesTable import settingsCOTTypes
from SettingsUSPD.iec60870.TypeIDTypesTable import settingsTypeIDTypes
from SettingsUSPD.iec60870.IEC60870SettingsTable import settingsIEC60870Settings
from SettingsUSPD.iec60870.IEC60870TemplateTable import settingsIEC60870Template
from SettingsUSPD.iec60870.IEC60870COTValuesTable import settingsIEC60870COTValues


# TODO this is HTTP stuff
def auth(env):
    return '200 OK', ""


# ///
#     По УРЛ определяем наш запрос - Это важно

handlers = {
        '/auth': auth,

        # // Авторизация - Не дописано !!!!!
        '/settings/proto/json/auth' : settingsAuthorization,

        # // Переписал - Таблица Счетчиков - переделал
        '/settings/meter/table': settingsMeterTable,

        # // переписал - Настройки СИМ Карты - переделал
        '/settings/modem/sim': settingsSIM,

        # // Настройки линий питания - Переделал
        '/settings/dout': settingsPowerLine,

        # // Состояние линий питания - Добивил !!!!
        '/state/dout': settingsPowerLineStatus,

        # // переписал Настройки ethernet
        '/settings/ip': settingsEthernet,
        # // Настройки локального времени - Переписал
        '/settings/time/local': settingsTimeLocal,

        # // Сервера синхронизации времени - Переписал
        '/settings/servers/sntp': settingsNTPServer,
        # /////////////////////ДОБАВИЛ///////////////////////////

        # // Условия синхронизации времени - - Не дописмал
        '/settings/actions/sntp': settingsTimeSynchronizationConditions,

        # // Журнал установки времени - - Не дописмал
        '/jrnl/time': settingsJournalSetTime,

        # ///////////////////////////////////////////////////////
        # // Настройки расписаний - Переделал
        '/settings/events/schdl': settingsScheduler,

        # // Опрос приборов учета по событиям - Переделал
        '/settings/actions/meter': settingsPoller,

        # // - Настройки - Настройка системы событий - Переписал
        '/settings/events/manager' : settingsEventManager,

        # // - Настройки HTTP сервера - переписал
        '/settings/servers/tcp': settingsTCPServer,

        # // Задание времени - Переделал
        '/meter/settings/time': settingsSetTimeToMeter,

        # // Задание положения реле - Переписал
        '/meter/settings/relay': settingsSetMeterRelay,

        # // Считывание - Архивные показатели - Переписал
        '/meter/data/arch': settingsMeterDataArchive,

        # // Считывание - Текущие показатели - Переписал
        '/meter/data/moment': settingsMeterDataMoment,

        # // Шаблоны приборов учета - Переписал
        '/settings/templates/meter': settingsMeterTemplates,

        # //Шаблоны данных приборов учета - Переписал
        '/settings/templates/arch': settingsMeterDataTemplates,

        # /////////////////////ДОБАВИЛ///////////////////////////

        # //Журнал ответов приборов учета - - Не дописмал
        '/jrnl/meter/answ': settingsMeterResponseJournal,

        # ///////////////////////////////////////////////////////
        # информации о времени - ОБЬЕДЕНИЛ В ОДИН КЛАСС
        # // Настройки информации о времени - получение - Переписал
        '/state/time': settingsTimeInformation,
        # //  информации о времени - перезапись - Переписал
        '/action/time/set': settingsTimeInformation,

        # // - Перезагрузка устройства - переписал
        '/action/restart' : settingsDeviceRestart,

        # // Настройки MQTT брокера - Переделал
        '/settings/servers/mqtt': settingsBrokerMQTT,

        # ///////////////////////////Зарядные станции//////////////////////////////////

        # -Таблица зарядных станций - Переписал
        '/settings/charge/table': settingsChargeStationTable,

        # # - Состояние зарядных станций - Переписал
        '/charge/data/arch': settingsChargeStationArchData,

        # ///////////////////////////////////////////////////////

        # /////////////////////ДОБАВИЛ///////////////////////////
        # Настройки Настройки цифровых интерфейсов - Не дописмал
        '/settings/uart': settingsUart,

        # ///////////////////////////////////////////////////////
        # Пока не завезено во фронтенд

        # // - таблица MeterMessages в БД системы событий - Переписал
        '/settings/templates/messages': settingsMeterMessages,

        # // - таблица MQTTMeterMessages в БД системы событий - Переписал
        '/settings/action/mqtt': settingsMQTTMeterMessages,

        # // - таблица Calendar в БД системы событий - Переписал
        '/settings/events/calendar': settingsCalendar,

        # // - Таблица аккаунтов SMTP - Переписал
        '/settings/smtp': settingsAccountSMTP,
        # // -  таблица SMTPMeterMessages в БД системы событий - Переписал
        '/settings/action/smtp': settingsSMTPMeterMessages,

        # // -  таблица Email в БД системы событий - Переписал
        '/settings/email': settingsEmail,

        # ///////////////////// iec60870 ///////////////////////////

        # // - iec60870 - Работа с таблицей MapIOA - Переписал
        '/settings/iec60870/mapioa': settingsMapIOA,

        # // - iec60870 - работа с таблицей ValueDescription - переписал
        '/settings/iec60870/value_description': settingsValueDescription,
        # // - iec60870 - работа с таблицей TemplateName - переписал
        '/settings/iec60870/template_name': settingsTemplateName,
        # // - iec60870 - работа с таблицей COTTypes - переписал
        '/settings/iec60870/cot_types': settingsCOTTypes,
        # // - iec60870 - работа с таблицей TypeIDTypes - переписал
        '/settings/iec60870/type_id_types': settingsTypeIDTypes,

        # // - iec60870 - работа с таблицей Settings - Переписал
        '/settings/iec60870/iec60870_settings' : settingsIEC60870Settings,

        # // - iec60870 - работа с таблицей IEC60870Template - Переписал
        '/settings/iec60870/iec60870_template': settingsIEC60870Template ,

        # // - iec60870 - работа с таблицей IEC60870Template - Переписал
        '/settings/iec60870/iec60870_cot_values' :settingsIEC60870COTValues,
            }

# /// СТАРОЕ
#
# handlers = [
#     ('POST', '/auth', auth),
#
#     # // Авторизация - Не дописано !!!!!
#     ('GET', '/settings/proto/json/auth', settingsAuthorization),
#     ('PUT', '/settings/proto/json/auth', settingsAuthorization),
#     ('POST', '/settings/proto/json/auth', settingsAuthorization),
#     ('DELETE', '/settings/proto/json/auth', settingsAuthorization),
#
#     # // Переписал - Таблица Счетчиков - переделал
#     ('GET', '/settings/meter/table', settingsMeterTable),
#     ('PUT', '/settings/meter/table', settingsMeterTable),
#     ('POST', '/settings/meter/table', settingsMeterTable),
#     ('DELETE', '/settings/meter/table', settingsMeterTable),
#
#     # // переписал - Настройки СИМ Карты - переделал
#     ('GET', '/settings/modem/sim', settingsSIM),
#     ('PUT', '/settings/modem/sim', settingsSIM),
#     ('POST', '/settings/modem/sim', settingsSIM),
#
#     # // Настройки линий питания - Переделал
#     ('GET', '/settings/dout', settingsPowerLine),
#     ('PUT', '/settings/dout', settingsPowerLine),
#     ('POST', '/settings/dout', settingsPowerLine),
#     ('DELETE', '/settings/dout', settingsPowerLine),
#
#     # // Состояние линий питания - Добивил !!!!
#     ('GET', '/state/dout', settingsPowerLineStatus),
#
#     # // переписал Настройки ethernet
#     ('GET', '/settings/ip', settingsEthernet),
#     ('PUT', '/settings/ip', settingsEthernet),
#     ('POST', '/settings/ip', settingsEthernet),
#
#     # // Настройки локального времени - Переписал
#     ('GET', '/settings/time/local', settingsTimeLocal),
#     ('PUT', '/settings/time/local', settingsTimeLocal),
#     ('POST', '/settings/time/local', settingsTimeLocal),
#
#     # // Сервера синхронизации времени - Переписал
#     ('GET', '/settings/servers/sntp', settingsNTPServer),
#     ('PUT', '/settings/servers/sntp', settingsNTPServer),
#     ('POST', '/settings/servers/sntp', settingsNTPServer),
#     ('DELETE', '/settings/servers/sntp', settingsNTPServer),
#     # /////////////////////ДОБАВИЛ///////////////////////////
#
#     # // Условия синхронизации времени - - Не дописмал
#     ('GET', '/settings/actions/sntp', settingsTimeSynchronizationConditions),
#     ('PUT', '/settings/actions/sntp', settingsTimeSynchronizationConditions),
#     ('POST', '/settings/actions/sntp', settingsTimeSynchronizationConditions),
#     ('DELETE', '/settings/actions/sntp', settingsTimeSynchronizationConditions),
#
#     # // Журнал установки времени - - Не дописмал
#     ('GET', '/jrnl/time', settingsJournalSetTime),
#     ('PUT', '/jrnl/time', settingsJournalSetTime),
#     ('POST', '/jrnl/time', settingsJournalSetTime),
#     ('DELETE', '/jrnl/time', settingsJournalSetTime),
#
#     # ///////////////////////////////////////////////////////
#     # // Настройки расписаний - Переделал
#     ('GET', '/settings/events/schdl', settingsScheduler),
#     ('PUT', '/settings/events/schdl', settingsScheduler),
#     ('POST', '/settings/events/schdl', settingsScheduler),
#     ('DELETE', '/settings/events/schdl', settingsScheduler),
#
#     # // Опрос приборов учета по событиям - Переделал
#     ('GET', '/settings/actions/meter', settingsPoller),
#     ('PUT', '/settings/actions/meter', settingsPoller),
#     ('POST', '/settings/actions/meter', settingsPoller),
#     ('DELETE', '/settings/actions/meter', settingsPoller),
#
#     # // - Настройки - Настройка системы событий - Переписал
#     ('GET', '/settings/events/manager', settingsEventManager),
#     ('PUT', '/settings/events/manager', settingsEventManager),
#     ('POST', '/settings/events/manager', settingsEventManager),
#     ('DELETE', '/settings/events/manager', settingsEventManager),
#
#     # // - Настройки HTTP сервера - переписал
#     ('GET', '/settings/servers/tcp', settingsTCPServer),
#     ('PUT', '/settings/servers/tcp', settingsTCPServer),
#     ('POST', '/settings/servers/tcp', settingsTCPServer),
#
#     # // Задание времени - Переделал
#     ('PUT', '/meter/settings/time', settingsSetTimeToMeter),
#
#     # // Задание положения реле - Переписал
#     ('PUT', '/meter/settings/relay', settingsSetMeterRelay),
#
#     # // Считывание - Архивные показатели - Переписал
#     ('POST', '/meter/data/arch', settingsMeterDataArchive),
#
#     # // Считывание - Текущие показатели - Переписал
#     ('POST', '/meter/data/moment', settingsMeterDataMoment),
#
#     # // Шаблоны приборов учета - Переписал
#     ('GET', '/settings/templates/meter', settingsMeterTemplates),
#     ('PUT', '/settings/templates/meter', settingsMeterTemplates),
#     ('POST', '/settings/templates/meter', settingsMeterTemplates),
#     ('DELETE', '/settings/templates/meter', settingsMeterTemplates),
#
#     # //Шаблоны данных приборов учета - Переписал
#     ('GET', '/settings/templates/arch', settingsMeterDataTemplates),
#     ('PUT', '/settings/templates/arch', settingsMeterDataTemplates),
#     ('POST', '/settings/templates/arch', settingsMeterDataTemplates),
#     ('DELETE', '/settings/templates/arch', settingsMeterDataTemplates),
#
#     # /////////////////////ДОБАВИЛ///////////////////////////
#
#     # //Журнал ответов приборов учета - - Не дописмал
#     ('GET', '/jrnl/meter/answ', settingsMeterResponseJournal),
#     ('PUT', '/jrnl/meter/answ', settingsMeterResponseJournal),
#     ('POST', '/jrnl/meter/answ', settingsMeterResponseJournal),
#     ('DELETE', '/jrnl/meter/answ', settingsMeterResponseJournal),
#
#     # ///////////////////////////////////////////////////////
#     # информации о времени - ОБЬЕДЕНИЛ В ОДИН КЛАСС
#     # // Настройки информации о времени - получение - Переписал
#     ('GET', '/state/time', settingsTimeInformation),
#     # //  информации о времени - перезапись - Переписал
#     ('PUT', '/action/time/set', settingsTimeInformation),
#
#     # // - Перезагрузка устройства - переписал
#     ('PUT', '/action/restart', settingsDeviceRestart),
#
#     # // Настройки MQTT брокера - Переделал
#     ('GET', '/settings/servers/mqtt', settingsBrokerMQTT),
#     ('PUT', '/settings/servers/mqtt', settingsBrokerMQTT),
#     ('POST', '/settings/servers/mqtt', settingsBrokerMQTT),
#     ('DELETE', '/settings/servers/mqtt', settingsBrokerMQTT),
#
#     # ///////////////////////////Зарядные станции//////////////////////////////////
#
#     # -Таблица зарядных станций - Переписал
#     ('GET', '/settings/charge/table', settingsChargeStationTable),
#     ('PUT', '/settings/charge/table', settingsChargeStationTable),
#     ('POST', '/settings/charge/table', settingsChargeStationTable),
#     ('DELETE', '/settings/charge/table', settingsChargeStationTable),
#
#     # # - Состояние зарядных станций - Переписал
#     ('POST', '/charge/data/arch', settingsChargeStationArchData),
#
#     # ///////////////////////////////////////////////////////
#
#     # /////////////////////ДОБАВИЛ///////////////////////////
#     # Настройки Настройки цифровых интерфейсов - Не дописмал
#     ('GET', '/settings/uart', settingsUart),
#     ('PUT', '/settings/uart', settingsUart),
#     ('POST', '/settings/uart', settingsUart),
#
#     # ///////////////////////////////////////////////////////
#     # Пока не завезено во фронтенд
#
#     # // - таблица MeterMessages в БД системы событий - Переписал
#     ('GET', '/settings/templates/messages', settingsMeterMessages),
#     ('PUT', '/settings/templates/messages', settingsMeterMessages),
#     ('POST', '/settings/templates/messages', settingsMeterMessages),
#     ('DELETE', '/settings/templates/messages', settingsMeterMessages),
#
#     # // - таблица MQTTMeterMessages в БД системы событий - Переписал
#     ('GET', '/settings/action/mqtt', settingsMQTTMeterMessages),
#     ('PUT', '/settings/action/mqtt', settingsMQTTMeterMessages),
#     ('POST', '/settings/action/mqtt', settingsMQTTMeterMessages),
#     ('DELETE', '/settings/action/mqtt', settingsMQTTMeterMessages),
#
#     # // - таблица Calendar в БД системы событий - Переписал
#     ('GET', '/settings/events/calendar', settingsCalendar),
#     ('PUT', '/settings/events/calendar', settingsCalendar),
#     ('POST', '/settings/events/calendar', settingsCalendar),
#     ('DELETE', '/settings/events/calendar', settingsCalendar),
#
#     # // - Таблица аккаунтов SMTP - Переписал
#     ('GET', '/settings/smtp', settingsAccountSMTP),
#     ('PUT', '/settings/smtp', settingsAccountSMTP),
#     ('POST', '/settings/smtp', settingsAccountSMTP),
#     ('DELETE', '/settings/smtp', settingsAccountSMTP),
#
#     # // -  таблица SMTPMeterMessages в БД системы событий - Переписал
#     ('GET', '/settings/action/smtp', settingsSMTPMeterMessages),
#     ('PUT', '/settings/action/smtp', settingsSMTPMeterMessages),
#     ('POST', '/settings/action/smtp', settingsSMTPMeterMessages),
#     ('DELETE', '/settings/action/smtp', settingsSMTPMeterMessages),
#
#     # // -  таблица Email в БД системы событий - Переписал
#     ('GET', '/settings/email', settingsEmail),
#     ('PUT', '/settings/email', settingsEmail),
#     ('POST', '/settings/email', settingsEmail),
#     ('DELETE', '/settings/email', settingsEmail),
#
#     # ///////////////////// iec60870 ///////////////////////////
#
#     # // - iec60870 - Работа с таблицей MapIOA - Переписал
#     ('GET', '/settings/iec60870/mapioa', settingsMapIOA),
#     ('PUT', '/settings/iec60870/mapioa', settingsMapIOA),
#     ('POST', '/settings/iec60870/mapioa', settingsMapIOA),
#     ('DELETE', '/settings/iec60870/mapioa', settingsMapIOA),
#
#     # // - iec60870 - работа с таблицей ValueDescription - переписал
#     ('GET', '/settings/iec60870/value_description', settingsValueDescription),
#     # // - iec60870 - работа с таблицей TemplateName - переписал
#     ('GET', '/settings/iec60870/template_name', settingsTemplateName),
#     # // - iec60870 - работа с таблицей COTTypes - переписал
#     ('GET', '/settings/iec60870/cot_types', settingsCOTTypes),
#     # // - iec60870 - работа с таблицей TypeIDTypes - переписал
#     ('GET', '/settings/iec60870/type_id_types', settingsTypeIDTypes),
#
#     # // - iec60870 - работа с таблицей Settings - Переписал
#     ('GET', '/settings/iec60870/iec60870_settings', settingsIEC60870Settings),
#     ('POST', '/settings/iec60870/iec60870_settings', settingsIEC60870Settings),
#     ('PUT', '/settings/iec60870/iec60870_settings', settingsIEC60870Settings),
#
#     # // - iec60870 - работа с таблицей IEC60870Template - Переписал
#     ('GET', '/settings/iec60870/iec60870_template', settingsIEC60870Template),
#     ('PUT', '/settings/iec60870/iec60870_template', settingsIEC60870Template),
#     ('POST', '/settings/iec60870/iec60870_template', settingsIEC60870Template),
#     ('DELETE', '/settings/iec60870/iec60870_template', settingsIEC60870Template),
#
#     # // - iec60870 - работа с таблицей IEC60870Template - Переписал
#     ('GET', '/settings/iec60870/iec60870_cot_values', settingsIEC60870COTValues),
#     ('PUT', '/settings/iec60870/iec60870_cot_values', settingsIEC60870COTValues),
#     ('POST', '/settings/iec60870/iec60870_cot_values', settingsIEC60870COTValues),
#     ('DELETE', '/settings/iec60870/iec60870_cot_values', settingsIEC60870COTValues),
#
# ]
