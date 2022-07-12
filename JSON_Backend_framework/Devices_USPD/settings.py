# Здесь расположим различные настройки

# ---------------------------------- Различные URL пути - Общие----------------------------------


url_path = {
    # //-------------------------------------------------------------------------------//
    #                                     Авторизация
    # //-------------------------------------------------------------------------------//
    # /auth	Авторизация
    "Authorization": '/auth',

    # /logoff	Отключение
    "Disconnection": '/logoff',

    # //-------------------------------------------------------------------------------//
    #                                     Настройки
    # //-------------------------------------------------------------------------------//

    # ================================ Настройки авторизации ==============================

    # Настройки http авторизации
    "Protocol_JSON_auth": '/settings/proto/json/auth',
    # Настройки авторизации текстового протокола
    "Protocol_TEXT_auth": '/settings/proto/text/auth',
    # Настройки авторизации протокола RTU-327
    "Protocol_RTU_auth": '/settings/proto/rtu/auth',
    # Настройки выдачи данных текстового протокола
    "Protocol_TEXT_data": '/settings/proto/text/data',
    # Настройка почтовых сообщений текстового протокола
    "Protocol_TEXT_mail": '/settings/proto/text/mail',

    # ================================ Настройки устройства ==============================

    # Настройки Ethernet
    "Settings_Ethernet": '/settings/ip',
    # Настройки последовательных интерфейсов(UART)
    "Settings_UART": '/settings/uart',
    # Настройки дискретных входов
    "Settings_Din": '/settings/din',
    # Настройки линий питания интерфейсов
    "Settings_Dout": '/settings/dout',
    # Настройки локального времени
    "Settings_TimeZone": '/settings/time/local',
    # Настройки доступа к файловой системе
    "Settings_FileSystem": '/settings/file_system/access',
    # Настройки модема
    "Settings_Modem": '/settings/modem',
    # Настройки APN(точки доступа)
    "Settings_APN": '/settings/modem/apn',
    # Настройки CSD(PPP-сервер)
    "Settings_CSD": '/settings/modem/csd',
    # Настройки SIM-карт (Pin, APN)
    "Settings_SIM": '/settings/modem/sim',

    # ================================Клиенты и серверы ==============================

    # Настройки TCP-серверов
    "Servers_TCP": '/settings/servers/tcp',
    # Настройки SMTP-серверов
    "Servers_SMTP": '/settings/servers/smtp',
    # Настройки SMTP-серверов
    "Servers_SNTP_settings": '/settings/smtp',
    # Настройки SNTP-серверов
    "Servers_SNTP": '/settings/servers/sntp',
    # Настройки MQTT-серверов
    "Servers_MQTT": '/settings/servers/mqtt',
    # Адресная книга
    "Settings_Address": '/settings/address',
    # Сообщения пользователя
    "Settings_MessagesCustom": '/settings/messages/custom',
    # Сообщения с данными приборов учета
    "Settings_MessagesMeter": '/settings/messages/meter',

    # ================================ Приборы учета ==============================

    # Настройки хранения архивных данных приборов учета
    "MeterArchInfo": '/settings/meter/arch',
    # Таблица приборов учета
    "MaterTable": '/settings/meter/table',
    # ================================ Система событий  ==============================

    # Настройки событий изменений дискретных входов
    "Events_Din": '/settings/events/din',
    # Настройки событий календаря
    "Events_Calendar": '/settings/events/calendar',
    # Настройки расписаний
    "Events_Schedule": '/settings/events/schdl',
    # Настройки менеджера системы событий
    "Events_Manager": '/settings/events/manager',
    # Настройки шаблонов приборов учета
    "Templates_Meter": '/settings/templates/meter',
    # Настройки шаблонов данных приборов учета
    "Templates_Meter_Data": '/settings/templates/arch',
    # Настройки шаблонов сообщений
    "Template_Messages": '/settings/templates/messages',
    # Шаблоны Email адресов
    "Template_Email": '/settings/templates/email',
    # Настройки регулярного опроса приборов учета
    "Actions_Meter_Poller": '/settings/actions/meter',
    # Настройки регулярной отправки почтовых сообщений
    "Actions_SMTP": '/settings/actions/smtp',
    # Настройки регулярной синхронизации времени
    "Actions_SNTP": '/settings/actions/sntp',
    # Настройки регулярной отправки sms сообщений
    "Actions_SMS": '/settings/actions/sms',
    # Настройки регулярной публикации mqtt сообщений
    "Actions_MQTT": '/settings/actions/mqtt',
    # Настройки имени устройства
    "Settings_Name": '/settings/name',

    # ================================ Протокол МЭК IEC60870 - 5–104 ==============================

    # Работа с таблицей MapIOA
    "MapIOA": '/settings/iec60870_5_104/mapioa',
    # Работа с таблицей ValueDescription
    "ValueDescription": '/settings/iec60870_5_104/value_description',
    # Работа с таблицей TemplateName
    "TemplateName": '/settings/iec60870_5_104/template_name',
    # Работа с таблицей COTTypes
    "COTTypes": '/settings/iec60870_5_104/cot_types',
    # Работа с таблицей TypeIDTypes
    "TypeIDTypes": '/settings/iec60870_5_104/type_id_types',
    # Работа с таблицей Settings
    "IEC60870Settings": '/settings/iec60870_5_104/iec60870_settings',
    # Работа с таблицей IEC60870Template
    "IEC60870Template": '/settings/iec60870_5_104/iec60870_template',
    # Работа с таблицей COTValues
    "COTValues": '/settings/iec60870_5_104/iec60870_cot_values',

    # //-------------------------------------------------------------------------------//
    #                            Опрос приборов учета
    # //-------------------------------------------------------------------------------//
    # 	Опрос приборов учета
    "MeterData": '/meter/data',
    # Опрос приборов учета – Архивные записи
    "MeterData_Arch": '/meter/data/arch',
    # Опрос приборов учета – Моментные показатели
    "MeterData_Moment": '/meter/data/moment',

    # //-------------------------------------------------------------------------------//
    #                                Управление приборами учета
    # //-------------------------------------------------------------------------------//

    # Установка времени – Системное время счетчика
    "Meter_Time": '/meter/settings/time',
    # Управление реле
    "Meter_Relay": '/meter/settings/relay',

    # //-------------------------------------------------------------------------------//
    #                                    Действия
    # //-------------------------------------------------------------------------------//

    # Синхронизация времени (SNTP)
    "Time_synchronization": '/action/time/sync',
    # Поверка внешних ЧРВ
    "Time_check": '/action/time/check',
    # Перезагрузка
    "Restart": '/action/restart',
    # Обновление загрузчика
    "Update_loader": '/action/update/loader',
    # Очистка логического диска
    "Disk_clear": '/action/disk/clear',
    # Установка времени – Системное время устройства
    "Set_time": '/action/time/set',
    # Синхронизация хранилища данных приборов учета
    "Storage_synchronization": '/action/storage/sync',

    # //-------------------------------------------------------------------------------//
    #                                 Журналы изделия
    # //-------------------------------------------------------------------------------//
    # Журнал системы событий
    "Journal_Action": '/jrnl/action',
    # Журнал изменения времени
    "Journal_Time": '/jrnl/time',
    # Журнал сетевых подключений
    "Journal_Server_connections": '/jrnl/srvconn',
    # Журнал подключений PPP клиента (GPRS)
    "Journal_PPP_Client_connections": '/jrnl/ppp/clconn',
    # Журнал поднятия PPP-сервера (CSD)
    "Journal_PPP_Server_connections": '/jrnl/ppp/srvconn',
    # Журнал входящих вызовов (CSD)
    "Journal_CSD_Call": '/jrnl/call',
    # Журнал изменения состояния дискретных входов
    "Journal_Sens": '/jrnl/din/sens',

    "Journal_PowerLine": '/jrnl/din/pwrline',

    "Journal_Power": '/jrnl/din/power',

    "Journal_Charge": '/jrnl/din/charge',

    "Journal_Din_Open": '/jrnl/din/open',
    # Журнал авторизации (HTTP-сервер)
    "Journal_Auth_JSON": '/jrnl/auth/json',
    # Журнал перезагрузок
    "Journal_reset": '/jrnl/reset',
    # Журнал хранилища почтовых сообщений
    "Journal_Mail_message": '/jrnl/mail/msg',
    # Журнал отправки почтовых сообщений
    "Journal_Mail_send": '/jrnl/mail/send',
    # Журнал изменения версии ВПО изделия
    "Journal_Update_version": '/jrnl/update/version',
    # Журнал обновления ВПО загрузчика изделия
    "Journal_Update_loader": '/jrnl/update/loader',
    # Журнал фиксации ответов приборов учета
    "Journal_Meter_answer": '/jrnl/meter/answ',
    # Журнал хранилища исходящих SMS сообщений
    "Journal_SMS_message": '/jrnl/sms/msg',
    # Журнал отправки SMS сообщений
    "Journal_SMS_send": '/jrnl/sms/send',
    # Журнал приема SMS сообщений
    "Journal_SMS_get": '/jrnl/sms/get',
    # Журнал установки связи с MQTT брокером
    "Journal_MQTT_connect": '/jrnl/mqtt/connect',
    # Журнал обмена сообщениями с MQTT брокером
    "Journal_MQTT_message": '/jrnl/mqtt/message',
    # //-------------------------------------------------------------------------------//
    #                     Информация о состоянии изделия
    # //-------------------------------------------------------------------------------//

    # Состояние линий питания интерфейсов
    "State_DOut": '/state/dout',
    # Состояние дискретных входов
    "State_DIn": '/state/din',
    # Состояние аналоговых входов
    "State_AIn": '/state/ain',
    # Ожидаемое время срабатывания расписаний
    "State_Scheduler": '/state/schdl',
    # Состояние последовательных интерфейсов
    "State_UART": '/state/uart',
    # Состояние сетевых подключений
    "State_Network": '/state/network',
    # Состояние сокетов
    "State_Socket": '/state/socket',
    # Состояние микросхем памяти
    "State_DataFlash": '/state/dataflash',
    # Состояние файловой системы
    "State_FileSystem": '/state/file_system',
    # Состояние модема
    "State_Modem": '/state/modem',
    # Состояние операционной системы
    "State_OS": '/state/os',
    # Состояние таблицы приборов учета
    "State_MeterTable": '/state/meter_table',
    # Текущее время
    "State_Time": '/state/time',
    # Информация о конфигурации системы
    "State_System": '/state/system',

    # //-------------------------------------------------------------------------------//
    #                                 Загрузка файлов
    # //-------------------------------------------------------------------------------//
    # Загрузка файлов обновления ВПО
    "Upload_firmware": '/upload/firmware',
    #       Загрузка файлов обновления ВПО
    "Upload_loader": '/upload/loader',

    # //-------------------------------------------------------------------------------//
    #                                     Зарядные станции
    # //-------------------------------------------------------------------------------//

    # -Таблица зарядных станций - Переписал
    'ChargeStationTable': '/settings/charge/table',
    # # - Состояние зарядных станций - Переписал
    'ChargeStationArchData': '/charge/data/arch',
    # //-------------------------------------------------------------------------------//
    #                                     Тарифное расписание
    # //-------------------------------------------------------------------------------//
    # // Активация тарифного расписания
    "Set_Calendar_Activate": '/meter/settings/calendar/activate',

    # // Имя календаря тарифного расписания
    "Set_Calendar_Name": '/meter/settings/calendar/name',

    # // Сезонный профиль тарифного расписания
    "Set_Calendar_Season": '/meter/settings/calendar/season',

    # // Недельный профиль тарифного расписания
    "Set_Calendar_Week": '/meter/settings/calendar/week',

    # // Суточный профиль тарифного расписания
    "Set_Calendar_Day": '/meter/settings/calendar/day',

    # // Дата активации тарифного расписания
    "Set_Calendar_Time": '/meter/settings/calendar/time',

}
