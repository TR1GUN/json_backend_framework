# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#               Здесь опишем наши классы для работы с разными конструкторами JSON для 40 SMART
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.FormJSON.UM40.Settings.Settings_UM40_Form_JSON import DeviceSettingsJSON, ServersJSON, \
    MeterJSON, ModemJSON


# -------------------------------------------------------------------------------------------------------------
#                                          Поле Settings
# -------------------------------------------------------------------------------------------------------------

class SettingsJSON:
    # Функционал
    # Таблица приборов учета , Настройки хранения архивных данных приборов учета
    Meter = None
    # Файловая система
    DeviceSettings = None

    # Система событий
    # EventSystem = None

    # Настройки модема
    Modem = None

    # Настройки Серверов
    Servers = None

    def __init__(self):
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Конструкторы
        self.Meter = self._JSON_Meter()
        self.Modem = self._JSON_Modem()
        self.Servers = self._JSON_Servers()
        # self.EventSystem = self._Settings_EventSystem()
        self.DeviceSettings = self._JSON_DeviceSettings()

    def _JSON_Meter(self):
        """
        Таблица приборов учета

        """
        # Определяем настройки
        Settings_Meter = MeterJSON()
        return Settings_Meter

    def _JSON_Modem(self):
        """
        Настройки Модема

        """

        # Определяем настройки
        Modem = ModemJSON()
        return Modem

    def _JSON_Servers(self):
        """

        Настройки Сервера

        :return:
        """
        # Определяем настройки
        Servers = ServersJSON()
        return Servers

    # def _Settings_EventSystem(self):
    #     """
    #
    #     Настройки Системы событий
    #
    #     :return:
    #     """

    def _JSON_DeviceSettings(self):
        """

        Настройки Самого прибора учета

        :return:
        """
        # Определяем настройки
        Device = DeviceSettingsJSON()
        return Device


# -------------------------------------------------------------------------------------------------------------
#                                          Поле Actions
# -------------------------------------------------------------------------------------------------------------

class ActionJSON:
    SetTime = None

    def __init__(self):
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Конструкторы
        self.SetTime = self._SetTime()

    # Установка Времени
    def _SetTime(self):
        from JSON_Backend_framework.FormJSON.UM40.Action.JSON_Construct_Actions_Set_Time import SettingsSetTime

        SetTime = SettingsSetTime()
        return SetTime


# -------------------------------------------------------------------------------------------------------------
#                                          Поле MeterDeviceManagement
# -------------------------------------------------------------------------------------------------------------

class MeterDeviceManagementJSON:
    SetRelay = None
    SyncTime = None

    def __init__(self):
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Конструкторы
        self.RelayControl = self._RelayControl()
        self.SyncTime = self._MeterTime()

    # Установка Времени
    def _MeterTime(self):
        from JSON_Backend_framework.FormJSON.UM40.MeterDeviceManagement.JSON_Construct_Management_MeterTime import \
            SettingsMeterTimeSync

        MeterTime = SettingsMeterTimeSync()
        return MeterTime

    # Установка Реле
    def _RelayControl(self):
        from JSON_Backend_framework.FormJSON.UM40.MeterDeviceManagement.JSON_Construct_Management_RelayControl import \
            SettingsRelay

        RelayControl = SettingsRelay()
        return RelayControl


# -------------------------------------------------------------------------------------------------------------
#                                          Поле MeterData
# -------------------------------------------------------------------------------------------------------------

class MeterDataJSON:
    MeterData = None

    def __init__(self):
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Конструкторы
        self.MeterData = self._MeterData()

    def _MeterData(self):
        from JSON_Backend_framework.FormJSON.UM40.MeterData.FormJSON_MeterData import FormJSON_MeterData

        MeterData = FormJSON_MeterData()
        return MeterData
