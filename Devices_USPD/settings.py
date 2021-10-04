# Здесь расположим различные настройки

# ---------------------------------- Различные URL пути - Общие----------------------------------
url_path = {
                                    # Авторизация

           "Authorization": '/auth'	,

                                    # Настройки

                        # Настройки устройства

            # Настройки Ethernet
            "Ethernet_settings": '/settings/ip',
            # Настройки линий питания интерфейсов
            "Interface_power_line_settings": '/settings/dout',
            # Настройки локального времени
            "Local_time_settings": '/settings/time/local',
            # Настройки SIM-карт (Pin, APN)
            "SIM_card_settings": '/settings/modem/sim',

                        # Клиенты и серверы
            # Настройки TCP-серверов
            "TCP_server_settings": '/settings/servers/tcp',
            # Настройки SNTP-серверов
            "SNTP_server_settings": '/settings/servers/sntp',

                        # Приборы учета
            # Таблица приборов учета
            "Metering_device_table": '/settings/meter/table',

                        # Система событий
            # Настройки менеджера системы событий
            "Event_Manager_Settings": '/settings/events/manager',
            # Настройки шаблонов приборов учета
            "Metering_device_templates_settings": '/settings/templates/meter',
            # Настройки шаблонов данных приборов учета
            "Settings_for_metering_devices_data_templates": '/settings/templates/arch',
            # Настройки расписаний
            "Schedule_settings": '/settings/events/schdl',
            # Настройки регулярного опроса приборов учета
            "Settings_for_regular_polling_of_metering_devices": '/settings/actions/meter',

                                    # Опрос приборов учета

            # Опрос приборов учета
            "Meter_Data_arch": '/meter/data/arch',

            "Meter_Data_moment": '/meter/data/moment',


                                    # Управление приборами учета

            # Установка времени
            "Time_setting": '/meter/settings/time',
            # Управление реле
            "Relay_control": '/meter/settings/relay',

                                    # Действия
            # Установка времени
            "Set_Time_setting": '/action/time/set',

                                    # Информация о состоянии изделия
            # Текущее время
            "Current_time": '/state/time',

}


            # ///////////////////////////////////////////////////////////
            #                Добавлено  в 40 СМАРТ
            # ///////////////////////////////////////////////////////////
url_path_smart40 = {


        # // Авторизация - Не дописано !!!!!
        'settingsAuthorization': '/settings/proto/json/auth',

        # -----------------> ЕСть в 30 смарте , но по дургому реализованно в 40
        # // Состояние линий питания - Добивил !!!!
        # Настройки линий питания интерфейсов
        "Interface_power_line_settings": '/state/dout',


        # // Условия синхронизации времени -
        # Настройки SNTP-серверов
        "SNTP_server_settings": '/settings/actions/sntp',
        # ----------------->

        # // Журнал установки времени - - Не дописмал
        'JournalSetTime':'/jrnl/time',









        # /////////////////////ДОБАВИЛ///////////////////////////

        # //Журнал ответов приборов учета - - Не дописмал
        'MeterResponseJournal': '/jrnl/meter/answ',

        # ///////////////////////////////////////////////////////
        # информации о времени - ОБЬЕДЕНИЛ В ОДИН КЛАСС


        # // - Перезагрузка устройства - переписал
        'DeviceRestart' : '/action/restart' ,

        # // Настройки MQTT брокера - Переделал
        'BrokerMQTT':  '/settings/servers/mqtt',

        # ///////////////////////////Зарядные станции//////////////////////////////////

        # -Таблица зарядных станций - Переписал
        'ChargeStationTable' : '/settings/charge/table',

        # # - Состояние зарядных станций - Переписал
        'ChargeStationArchData' : '/charge/data/arch',

        # ///////////////////////////////////////////////////////

        # /////////////////////ДОБАВИЛ///////////////////////////
        # Настройки Настройки цифровых интерфейсов - Не дописмал
        'settingsUart' : '/settings/uart',

        # ///////////////////////////////////////////////////////
        # Пока не завезено во фронтенд

        # // - таблица MeterMessages в БД системы событий - Переписал
        'MeterMessages' : '/settings/templates/messages',

        # // - таблица MQTTMeterMessages в БД системы событий - Переписал
        'MQTTMeterMessages' : '/settings/action/mqtt',

        # // - таблица Calendar в БД системы событий - Переписал
        'Calendar' : '/settings/events/calendar' ,

        # // - Таблица аккаунтов SMTP - Переписал
        'AccountSMTP' : '/settings/smtp',
        # // -  таблица SMTPMeterMessages в БД системы событий - Переписал
        'SMTPMeterMessages' : '/settings/action/smtp' ,

        # // -  таблица Email в БД системы событий - Переписал
        'settingsEmail' : '/settings/email',

        # ///////////////////// iec60870 ///////////////////////////

        # // - iec60870 - Работа с таблицей MapIOA - Переписал
         "MapIOA": '/settings/iec60870/mapioa',

        # // - iec60870 - работа с таблицей ValueDescription - переписал
        "ValueDescription": '/settings/iec60870/value_description',
        # // - iec60870 - работа с таблицей TemplateName - переписал
               "TemplateName"  : '/settings/iec60870/template_name',
        # // - iec60870 - работа с таблицей COTTypes - переписал
        'COTTypes'   : '/settings/iec60870/cot_types',
        # // - iec60870 - работа с таблицей TypeIDTypes - переписал
        'TypeIDTypes' : '/settings/iec60870/type_id_types',

        # // - iec60870 - работа с таблицей Settings - Переписал
        'IEC60870Settings'   : '/settings/iec60870/iec60870_settings',

        # // - iec60870 - работа с таблицей IEC60870Template - Переписал
         'IEC60870Template': '/settings/iec60870/iec60870_template',

        # // - iec60870 - работа с таблицей IEC60870Template - Переписал
        'IEC60870COTValues' : '/settings/iec60870/iec60870_cot_values',
           }

# ------------------------------------------------------------------------------------------------------
