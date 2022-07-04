#
import JSON_Backend_framework

# //-------------------------------------------------------------------
ip_smart_31 = '192.168.205.22'
ip_smart_40 = '192.168.203.54'

# ip_smart_40 = '85.115.238.210'
# ip_smart_31 = '85.115.238.210'

# САМ СМАРТ
SMART40 = JSON_Backend_framework.USPD.UM_40_Smart(ip_address=ip_smart_40)
#

# SMART31 = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password='admin',ip_address=ip_smart_40)

# //-------------------------------------------------------------------
#                         Протокол 40/31 Смарта
# //-------------------------------------------------------------------

# СЧЕТЧИКИ

UM_40_Meters_json = {"Meters": [{'addr': '88', 'id': 4, 'ifaceCfg': '', 'ifaceName': 'Hub', 'index': 4, 'pId': 5, 'passRd': '32323232323232323232323232323232', 'passWr': '32323232323232323232323232323232', 'rtuFider': 0, 'rtuObjNum': 0, 'rtuObjType': 0, 'type': 36, 'typeName': 'SPODES_M2XX'}, {'addr': '192.168.205.22:5555', 'id': 5, 'ifaceCfg': '', 'ifaceName': 'Ethernet', 'index': 5, 'pId': 0, 'passRd': '', 'passWr': '', 'rtuFider': 0, 'rtuObjNum': 0, 'rtuObjType': 0, 'type': 94, 'typeName': 'MILUR IC'}, {'addr': '192.168.202.241:5555', 'id': 6, 'ifaceCfg': '', 'ifaceName': 'Ethernet', 'index': 6, 'pId': 0, 'passRd': '', 'passWr': '', 'rtuFider': 0, 'rtuObjNum': 0, 'rtuObjType': 0, 'type': 94, 'typeName': 'MILUR IC'}, {'addr': '141227285', 'id': 7, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Hub', 'index': 7, 'pId': 6, 'passRd': '373737373737', 'passWr': '373737373737', 'rtuFider': 0, 'rtuObjNum': 0, 'rtuObjType': 0, 'type': 5, 'typeName': 'SE303'}, {'addr': 'ТЕСТ', 'id': 100, 'ifaceCfg': '9600,8n1', 'ifaceName': 'Iface4', 'index': 8, 'pId': 0, 'passRd': '373737373737', 'passWr': '373737373737', 'rtuFider': 1, 'rtuObjNum': 1, 'rtuObjType': 1, 'type': 5, 'typeName': 'SE303'}]}
UM_40_Meters_json = {
    "Meters": [
        {
            "addr": "88",
            "id": 1,
            "ifaceCfg": "",
            "ifaceName": "Iface1",
            "index": 1,
            "pId": 0,
            "passRd": "32323232323232323232323232323232",
            "passWr": "32323232323232323232323232323232",
            "rtuFider": 0,
            "rtuObjNum": 0,
            "rtuObjType": 0,
            "type": 36,
            "typeName": "SPODES_M2XX"
        },
        {
            "addr": "141227285",
            "id": 2,
            "ifaceCfg": "",
            "ifaceName": "Hub",
            "index": 2,
            "pId": 3,
            "passRd": "373737373737",
            "passWr": "373737373737",
            "rtuFider": 0,
            "rtuObjNum": 0,
            "rtuObjType": 0,
            "type": 5,
            "typeName": "SE303"
        },
        {
            "addr": "192.168.202.241:5555",
            "id": 3,
            "ifaceCfg": "",
            "ifaceName": "Ethernet",
            "index": 3,
            "pId": 0,
            "passRd": "373737373737",
            "passWr": "373737373737",
            "rtuFider": 1,
            "rtuObjNum": 1,
            "rtuObjType": 1,
            "type": 94,
            "typeName": "MILUR IC"
        },
        {
            "addr": "192.168.205.22:5555",
            "id": 4,
            "ifaceCfg": "",
            "ifaceName": "Ethernet",
            "index": 4,
            "pId": 0,
            "passRd": "",
            "passWr": "",
            "rtuFider": 0,
            "rtuObjNum": 0,
            "rtuObjType": 0,
            "type": 94,
            "typeName": "MILUR IC"
        },
        {
            "addr": "1101",
            "id": 5,
            "ifaceCfg": "",
            "ifaceName": "Hub",
            "index": 5,
            "pId": 4,
            "passRd": "32323232323232323232323232323232",
            "passWr": "32323232323232323232323232323232",
            "rtuFider": 0,
            "rtuObjNum": 0,
            "rtuObjType": 0,
            "type": 36,
            "typeName": "SPODES_M2XX"
        },
        {
            "addr": "ТЕСТ",
            "id": 6,
            "ifaceCfg": "9600,8n1",
            "ifaceName": "Iface1",
            "index": 6,
            "pId": 0,
            "passRd": "373737373737",
            "passWr": "373737373737",
            "rtuFider": 1,
            "rtuObjNum": 1,
            "rtuObjType": 1,
            "type": 5,
            "typeName": "SE303"
        }
    ]
}
#
# lol = SMART31.Settings.Meter.Table.Read_Settings()
#
# print(lol)


# lol = SMART40.Settings.Meter.Table.Rewrite_Settings(data=UM_40_Meters_json)
# print(lol)

lol = SMART40.Settings.Meter.Table.Read_Settings()

print(lol)
# //-------------------------------------------------------------------
#                         Тарифное расписание
# //-------------------------------------------------------------------
# Данные что запускаем
# data = {
#   "ids": [1],
#   "tags": [],
#   "measures": [
#     "ElMomentEnergy"
#   ]
# }
# Имя календаря тарифного расписания
# data = {
#   "ids": [1],
#   "tags": [],
#   "measures": [
#     "ElCalendarNameActive"
#   ]
# }

# data = {
#   "ids": [1],
#   "tags": [],
#   "measures": [
#     "ElCalendarNamePassive"
#   ]
# }
# Сезонный профиль тарифного расписания
# data = {
#   "ids": [1],
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
#   "ids": [1],
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

data = {
  "ids": [3],
  "tags": [],
  "measures": [
    "ElCalendarDayPassive"
  ]
}

# # Дата активации тарифного расписания
# data = {
#   "ids": [3],
#   "tags": [],
#   "measures": [
#     "ElCalendarActivateTime"
#   ]
# }

data_Day = {"id": 3, "type": "Passive",
            "settings": [{"dayId": 2, "ScriptName": "00000A0064FF", "ScriptSelector": 2, "hour": 14, "minute": 42,
                          "second": 57}]}

# data_Day =  {"id":3, "type": "Active",
# "settings":[{"dayId":1, "ScriptName":"00000A0064FF", "ScriptSelector":2, "hour":14, "minute":42, "second":57}]}


data_Week = {"id": 3, "type": "Active",
             "settings": [{"WeekName": "44656661756C74",
                           "monday": 1, "tuesday": 1, "wednesday": 1, "thursday": 1, "friday": 1, "saturday": 1,
                           "sunday": 1}]}

data_Week = {"id": 3, "type": "Passive",
             "settings": [{"WeekName": "44656661756C74",
                           "monday": 1, "tuesday": 1, "wednesday": 1, "thursday": 1, "friday": 1, "saturday": 1,
                           "sunday": 1}]}

data_Season = {"id": 3, "type": "Active",
               "settings": [
                   {"SeasonName": "44656661756C74", "WeekName": "44656661756C74", "SeasonStart": 2065875840000}]}

data_Season = {"id": 3, "type": "Passive",
               "settings": [
                   {"SeasonName": "44656661756C74", "WeekName": "44656661756C74", "SeasonStart": 2065875840000}]}

data_Name = {"id": 3, "type": "Active", "settings": [{"CalendarName": "44656661756C74"}]}
# data_Name = {"id":3, "type": "Passive", "settings":[{"CalendarName":"44656661756C74"}]}

data_Time = {"id": 3, "settings": [{"ActivateTime": 1649082459}]}

data_Activate = {"id": 3}
# //-------------------------------------------------------------------
# САМ СМАРТ
# SMART40 = JSON_Backend_framework.USPD.UM_40_Smart(ip_address=ip_smart_40)
# SMART31 = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password='admin',ip_address=ip_smart_40)
# lol = SMART40.Settings.DeviceSettings.Interface_Ethernet.Read_Settings()
#
# print(lol)

# Читаем текущие показания
# MeterData = SMART31.MeterData.MeterData.Read_MeterData(data=data)
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

# //-------------------------------------------------------------------
# Здесь расположим временные тестовые прогоны
# //-------------------------------------------------------------------
# //-------------------------------------------------------------------
#                           Настройки
# //-------------------------------------------------------------------
# //---------------------- Общие настройки ----------------------------
# DeviceSettings = SMART.Settings.DeviceSettings
# Настройки Ethernet
# print('read...')
# request = DeviceSettings.Interface_Ethernet.read_settings()
# print(request)
# print('write...')
# request = DeviceSettings.Interface_Ethernet.write_settings()
# print(request)
# print('rewrite...')
# request = DeviceSettings.Interface_Ethernet.rewrite_settings()
# print(request)
# print('delete...')
# request = DeviceSettings.Interface_Ethernet.delete_settings()
# print(request)

# Настройки последовательных интерфейсов(UART)
# print('read...')
# request = DeviceSettings.Interface_UART.read_settings()
# print(request)
# print('write...')
# request = DeviceSettings.Interface_UART.write_settings()
# print(request)
# print('rewrite...')
# request = DeviceSettings.Interface_UART.rewrite_settings()
# print(request)
# print('delete...')
# request = DeviceSettings.Interface_UART.delete_settings()
# print(request)

# Настройки линий питания интерфейсов
# print('read...')
# request = DeviceSettings.Interface_DOut.read_settings()
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


# Настройки локального времени - Часовые пояса
# print('read...')
# request = DeviceSettings.Time_Local.read_settings()
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

# //----------------    Настройки модема     ------------------------
# Modem = SMART.Settings.Modem

# СИМ карты
# print('read...')
# request = Modem.SIM.read_settings()
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

# //----------------    Настройки серверов     ------------------------


# TCP Сервера

# print('read...')
# request = ServerTCP().read_settings()
# print(request)
# print('write...')
# request = ServerTCP().write_settings()
# print(request)
# print('rewrete...')
# request = ServerTCP().rewrite_settings()
# print(request)


# //-------------------------------------------------------------------
#                   Опрос приборов учета
# //-------------------------------------------------------------------
# Опрос приборов учета

# Опрос приборов учета – Архивные записи

# Опрос приборов учета – Моментные показатели

# //-------------------------------------------------------------------
#                   Управление приборами учета
# //-------------------------------------------------------------------
# Установка времени – Системное время счетчика

# Управление реле

# //-------------------------------------------------------------------
#                           Действия
# //-------------------------------------------------------------------
# Перезагрузка


# Установка времени – Системное время устройства

# //-------------------------------------------------------------------
# Журналы изделия
# //-------------------------------------------------------------------
# Журнал изменения времени
# result = SMART.Journal.Time.read_Journal()
# print(result)

# Журнал фиксации ответов приборов учета
# result = SMART.Journal.Meter_answer.read_Journal()
# print(result)

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
