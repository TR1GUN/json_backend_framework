# Здесь расположим различные настройки

# ---------------------------------- Различные URL пути ----------------------------------
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

# ------------------------------------------------------------------------------------------------------