# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                       Поле Settings - Собираем
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
#                                     Поле - DeviceSettings
# -------------------------------------------------------------------------------------------------------------

class DeviceSettingsJSON :
    # Настройки Ethernet
    Interface_Ethernet = None
    # Настройки последовательных интерфейсов(UART)
    Interface_UART = None
    # Настройки дискретных входов

    # Настройки линий питания интерфейсов
    Interface_DOut = None
    # Настройки локального времени
    Time_Local = None
    # Настройки доступа к файловой системе

    def __init__(self):

        self.Interface_Ethernet = self._JSON_Ethernet()
        self.Interface_UART = self._JSON_UART()
        self.Interface_DOut = self._JSON_DOut()
        self.Time_Local = self._JSON_Time_Local()

    # ГЕНЕРИРУЕМ Настройки Ethernet
    def _JSON_Ethernet(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_Ethernet import SettingsEthernet
        Ethernet = SettingsEthernet()
        return Ethernet

    # ГЕНЕРИРУЕМ Настройки последовательных интерфейсов(UART)
    def _JSON_UART(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_UART import SettingsUART

        UART = SettingsUART()

        return UART

    # ГЕНЕРИРУЕМ Настройки Питания линий интерфейсов
    def _JSON_DOut(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_DOut import SettingsDOut

        PowerLine = SettingsDOut()

        return PowerLine

    # ГЕНЕРИРУЕМ Настройки часового пояса
    def _JSON_Time_Local(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Local_Time import SettingsTimeZone

        LocalTime = SettingsTimeZone()

        return LocalTime


# -------------------------------------------------------------------------------------------------------------
#                                     Поле - Servers
# -------------------------------------------------------------------------------------------------------------
class ServersJSON:

    # Настройки TCP-серверов
    TCP = None
    # # Настройки SMTP-серверов
    # SMTP = None
    # # Настройки SТTP-серверов
    # SNTP = None
    # # Настройки MQTT-серверов
    # MQTT = None

    def __init__(self):


        self.TCP = self._JSON_TCP()
        # self.SMTP = self._JSON_SMTP()
        # self.SNTP = self._JSON_SNTP()
        # self.MQTT = self._JSON_MQTT()

    # Здесь генерируем сам функционал :

    # Настройки TCP-серверов
    def _JSON_TCP(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.Servers.JSON_Construct_Settings_Server_TCP import SettingsServer
        TCP = SettingsServer()
        return TCP


# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Modem
# -------------------------------------------------------------------------------------------------------------

class ModemJSON:

    # Настройки SIM-карт (Pin, APN)
    SIM = None
    # # Настройки CSD(PPP-сервер)
    # CSD = None
    # # Настройки APN(точки доступа)
    # APN = None

    def __init__(self):

        self.SIM = self._JSON_SIM_card()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _JSON_SIM_card(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.Modem.JSON_Construct_Settings_SIM import SettingsSim
        SIM_card = SettingsSim()
        return SIM_card

# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Meter
# -------------------------------------------------------------------------------------------------------------

class MeterJSON:

    # Таблица приборов учета
    Table = None
    # Настройки хранения архивных данных приборов учета
    # ArchInfo = None

    def __init__(self):

        self.Table = self._JSON_Table()
        # self.ArchInfo = self._JSON_Arch()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _JSON_Table(self):
        from JSON_Backend_framework.FormJSON.UM40.Settings.Meter.JSON_Construct_Settings_MeterTable import SettingsMeterTable
        Table = SettingsMeterTable()
        return Table

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _JSON_Arch(self):


        ArchInfo = None
        return ArchInfo