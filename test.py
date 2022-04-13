#
import JSON_Backend_framework

# //-------------------------------------------------------------------
ip_smart_31 = '192.168.205.22'
ip_smart_40 = '192.168.202.176'
SMART = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password="admin", ip_address=ip_smart_31)
lol = SMART.Settings.Meter.Table.Read_Settings()
print(lol)

SMART = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password="admin", ip_address=ip_smart_40)
lol = SMART.Settings.Meter.Table.Read_Settings()
print(lol)

SMART = JSON_Backend_framework.USPD.UM_31_Smart(Login='admin', Password="admin", ip_address=ip_smart_40)
lol = SMART.MeterData.MeterData.Read_MeterData(data={"ids":[100],"tags":[],"time":[],"measures":["aCfg"]})
print(lol)
#
# print(lol)
#
# lol = SMART.Settings.Meter.Table.Read_Settings()
# print(lol)
#
#
# SMART = JSON_Backend_framework.USPD.UM_40_Smart(ip_address='192.168.202.176')
# lol = SMART.Settings.Meter.Table.Read_Settings()
# print(lol)


# lol = SMART.Settings.Meter.ArchInfo.read_settings()
# print(lol)
#
# lol = SMART.Settings.Modem.SIM.SettingsSim.settings_Sim2()
#
# print(lol)
#
# USPD = JSON_Backend_framework.USPD.UM_40_Smart(ip_address='192.168.202.143')
#
#
# print(USPD.StateInfo.Time.url_path)
# print(USPD.StateInfo.Time.Time_USPD_Read())
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
