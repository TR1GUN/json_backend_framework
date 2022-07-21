#
# import JSON_Backend_framework
#
# # # //-------------------------------------------------------------------
# ip_smart_31 = '192.168.205.22'
# ip_smart_40 = '192.168.202.197'
# SMART = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password="admin", ip_address=ip_smart_31)
# SMART = JSON_Backend_framework.USPD.UM_40_Smart(ip_address=ip_smart_40)

# lol = SMART.Settings.Proto.Text_Auth.Read_Settings()
#
# print(lol)
# lol2 = SMART.Settings.Proto.Text_Auth.Delete_Settings()
#
# print(lol2)
#
# lol2 = SMART.Settings.Proto.Text_Auth.Read_Settings()
#
# print(lol2)
#
# # Мои счетчики
# {'Meters': [{'id': 1, 'pId': 0, 'archId': 1, 'type': 5, 'addr': '1', 'passRd': '373737373737', 'passWr': '373737373737', 'line': 0, 'iface': 0, 'br': 0}, {'id': 2, 'pId': 0, 'archId': 1, 'type': 32, 'addr': '1', 'passRd': '', 'passWr': '', 'line': 0, 'iface': 0, 'br': 0}, {'id': 3, 'pId': 0, 'archId': 1, 'type': 3, 'addr': '1', 'passRd': '010101010101', 'passWr': '020202020202', 'line': 0, 'iface': 0, 'br': 0}, {'id': 4, 'pId': 0, 'archId': 1, 'type': 10, 'addr': '1', 'passRd': '303030303030', 'passWr': '303030303030', 'line': 0, 'iface': 0, 'br': 0}]}}


# SMART = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password="admin", ip_address=ip_smart_40)
# lol = SMART.Settings.Meter.Table.Read_Settings()
# print(lol)

# //-------------------------------------------------------------------
#                         Тарифное расписание
# //-------------------------------------------------------------------
# Данные что запускаем
# data = {
#     "ids": [3],
#     "tags": [],
#     "measures": [
#         "ElMomentEnergy"
#     ]
# }
# # Имя календаря тарифного расписания
# data = {
#     "ids": [3],
#     "tags": [],
#     "measures": [
#         "ElCalendarNameActive"
#     ]
# }

# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarNamePassive"
#   ]
# }
# # Сезонный профиль тарифного расписания
# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarSeasonActive"
#   ]
# }

# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarSeasonPassive"
#   ]
# }
# # Недельный профиль тарифного расписания
# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarWeekActive"
#   ]
# }

# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarWeekPassive"
#   ]
# }
# Суточный профиль тарифного расписания
# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarDayActive"
#   ]
# }

# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarDayPassive"
#   ]
# }

# # Дата активации тарифного расписания
# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarActivateTime"
#   ]
# }
#
# data_Day = {"id": 3, "type": "Passive",
#             "settings": [{"dayId": 2, "ScriptName": "00000A0064FF", "ScriptSelector": 2, "hour": 14, "minute": 42,
#                           "second": 57}]}

# data_Day =  {"id":3, "type": "Active",
# "settings":[{"dayId":1, "ScriptName":"00000A0064FF", "ScriptSelector":2, "hour":14, "minute":42, "second":57}]}

#
# data_Week = {"id": 3, "type": "Active",
#              "settings": [{"WeekName": "44656661756C74",
#                            "monday": 1, "tuesday": 1, "wednesday": 1, "thursday": 1, "friday": 1, "saturday": 1,
#                            "sunday": 1}]}
#
# data_Week = {"id": 3, "type": "Passive",
#              "settings": [{"WeekName": "44656661756C74",
#                            "monday": 1, "tuesday": 1, "wednesday": 1, "thursday": 1, "friday": 1, "saturday": 1,
#                            "sunday": 1}]}
#
# data_Season = {"id": 3, "type": "Active",
#                "settings": [
#                    {"SeasonName": "44656661756C74", "WeekName": "44656661756C74", "SeasonStart": 2065875840000}]}
# data_Season = {"id": 3, "type": "Passive",
#                "settings": [
#                    {"SeasonName": "44656661756C74", "WeekName": "44656661756C74", "SeasonStart": 2065875840000}]}
#
# data_Name = {"id": 3, "type": "Active", "settings": [{"CalendarName": "44656661756C74"}]}
# # data_Name = {"id":3, "type": "Passive", "settings":[{"CalendarName":"44656661756C74"}]}
#
# data_Time = {"id": 3, "settings": [{"ActivateTime": 1649082459}]}
#
# data_Activate = {"id": 3}
# //-------------------------------------------------------------------
# САМ СМАРТ
# SMART40 = JSON_Backend_framework.USPD.UM_40_Smart(ip_address=ip_smart_40)
#
# lol = SMART40.Settings.DeviceSettings.Interface_Ethernet.Read_Settings()
# print(lol)


# Читаем текущие показания
# MeterData = SMART40.MeterData.MeterData_Moment.Read_MeterData(data=data)
# print(MeterData)

# Задаем показания

# Day = SMART40.MeterDeviceManagement.Calendar.Day.Set_Calendar(data=data_Day)
# print(Day)
# Week = SMART40.MeterDeviceManagement.Calendar.Week.Set_Calendar(data=data_Week)
# print(Week)
# Season = SMART40.MeterDeviceManagement.Calendar.Season.Set_Calendar(data=data_Season)
# print(Season)
# Name = SMART40.MeterDeviceManagement.Calendar.Name.Set_Calendar(data=data_Name)
# print(Name)
# Time = SMART40.MeterDeviceManagement.Calendar.Time.Set_Calendar(data=data_Time)
# print(Time)
# Activate = SMART40.MeterDeviceManagement.Calendar.Activate.Set_Calendar(data=data_Activate)
# print(Activate)

# # //-------------------------------------------------------------------
# # Здесь расположим временные тестовые прогоны
# # //-------------------------------------------------------------------
# SMART = JSON_Backend_framework.USPD.UM_40_Smart(ip_address=ip_smart_40)
#
# # //-------------------------------------------------------------------
# #                           Настройки
# # //-------------------------------------------------------------------
# # //---------------------- Общие настройки ----------------------------
# DeviceSettings = SMART.Settings.DeviceSettings
# # Настройки Ethernet
# print('Ethernet read...')
# request = DeviceSettings.Interface_Ethernet.Read_Settings()
# print(request)
# print('Ethernet write...')
# request = DeviceSettings.Interface_Ethernet.write_settings()
# print(request)
# print('Ethernet rewrite...')
# request = DeviceSettings.Interface_Ethernet.rewrite_settings()
# print(request)
# print('Ethernet delete...')
# request = DeviceSettings.Interface_Ethernet.delete_settings()
# print(request)
#
# # Настройки последовательных интерфейсов(UART)
# print('Interface_UART read...')
# request = DeviceSettings.Interface_UART.Read_Settings()
# print(request)
# print('Interface_UART write...')
# request = DeviceSettings.Interface_UART.write_settings()
# print(request)
# print('Interface_UART rewrite...')
# request = DeviceSettings.Interface_UART.rewrite_settings()
# print(request)
# print('Interface_UART delete...')
# request = DeviceSettings.Interface_UART.delete_settings()
# print(request)
#
# # Настройки линий питания интерфейсов
# print('Interface_DOut read...')
# request = DeviceSettings.Interface_DOut.Read_Settings()
# print(request)
# print('write...')
# request = DeviceSettings.Interface_DOut.write_settings()
# print(request)
# print('rewrite...')
# request = DeviceSettings.Interface_DOut.rewrite_settings()
# print(request)
# print('delete...')
# request = DeviceSettings.Interface_DOut.delete_settings()
# print(request)
#
#
# # Настройки локального времени - Часовые пояса
# print('Time_Local read...')
# request = DeviceSettings.Time_Local.Read_Settings()
# print(request)
# print('write...')
# request = DeviceSettings.Time_Local.write_settings()
# print(request)
# print('rewrite...')
# request = DeviceSettings.Time_Local.rewrite_settings()
# print(request)
# print('delete...')
# request = DeviceSettings.Time_Local.delete_settings()
# print(request)
#
# # //----------------    Настройки модема     ------------------------
# # Modem = SMART.Settings.Modem
#
# # СИМ карты
# print('read...')
# request = Modem.SIM.Read_Settings()
# print(request)
# print('write...')
# request = Modem.SIM.write_settings()
# print(request)
# print('rewrite...')
# request = Modem.SIM.rewrite_settings()
# print(request)
# print('delete...')
# request = Modem.SIM.delete_settings()
# print(request)
#
# # //----------------    Настройки серверов     ------------------------
#
# Server = SMART.Settings.Servers
# # TCP Сервер
# print('TCP read...')
# request = Server.TCP.Read_Settings()
# print(request)
# print('write...')
# request = Server.TCP.write_settings()
# print(request)
# print('rewrete...')
# request = Server.TCP.rewrite_settings()
# print(request)
# print('delete...')
# request = Server.TCP.delete_settings()
# print(request)
#
#
# # SMTP Сервера
#
# print('SMTP read...')
# request = Server.SMTP.Read_Settings()
# print(request)
# print('write...')
# request = Server.SMTP.write_settings()
# print(request)
# print('rewrete...')
# request = Server.SMTP.rewrite_settings()
# print(request)
# print('delete...')
# request = Server.SMTP.delete_settings()
# print(request)
#
# # SNTP Сервера
#
# print('SNTP read...')
# request = Server.SNTP.Read_Settings()
# print(request)
# print('write...')
# request = Server.SNTP.write_settings()
# print(request)
# print('rewrete...')
# request = Server.SNTP.rewrite_settings()
# print(request)
# print('delete...')
# request = Server.SNTP.delete_settings()
# print(request)
#
#
# # MQTT Сервера
#
# print('MQTT read...')
# request = Server.MQTT.Read_Settings()
# print(request)
# print('write...')
# request = Server.MQTT.write_settings()
# print(request)
# print('rewrete...')
# request = Server.MQTT.rewrite_settings()
# print(request)
# print('delete...')
# request = Server.MQTT.delete_settings()
# print(request)
# //-------------------------------------------------------------------
#                   Опрос приборов учета
# //-------------------------------------------------------------------
# Опрос приборов учета
#
# Опрос приборов учета – Архивные записи
#
# Опрос приборов учета – Моментные показатели
#
# //-------------------------------------------------------------------
#                   Управление приборами учета
# //-------------------------------------------------------------------
# Установка времени – Системное время счетчика
#
# Управление реле
#
# //-------------------------------------------------------------------
#                           Действия
# //-------------------------------------------------------------------
# Перезагрузка
#
#
# Установка времени – Системное время устройства
#
# //-------------------------------------------------------------------
# Журналы изделия
# //-------------------------------------------------------------------
# Журнал изменения времени
# result = SMART.Journal.Time.read_Journal()
# print(result)
#
# Журнал фиксации ответов приборов учета
# result = SMART.Journal.Meter_answer.read_Journal()
# print(result)
#
# //-------------------------------------------------------------------
# Информация о состоянии изделия
# //-------------------------------------------------------------------
# Текущее время
# result = SMART.StateInfo.Time.Time_USPD_Read()
# print(result)
# # Состояние линий питания интерфейсов
# result = SMART.StateInfo.DOut.State_read()
# print(result)
# //-------------------------------------------------------------------
