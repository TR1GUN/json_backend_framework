# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#               Здесь опишем наши классы для работы с разными конструкторами JSON для 40 SMART
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.FormJSON.UM40.UM40_FormJSON import ActionJSON , MeterDeviceManagementJSON , MeterDataJSON , SettingsJSON
# -------------------------------------------------------------------------------------------------------------
#                                          Протокол УМ - 40 СМАРТ
# -------------------------------------------------------------------------------------------------------------


class UM40FormJSON:
    # Поля Необходимые для доступа
    # Настройки
    Settings = None
    # Действия
    Action = None
    # Управление приборами учетa
    MeterDeviceManagement = None
    # Опрос приборов учета - данные приборов учета
    MeterData = None

    def __init__(self):
        """
        Протокол УМ - 40 СМАРТ - Конструктор
        """
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Настройки
        self._Settings()

        self._Actions()
        self._MeterDeviceManagement()
        self._MeterData()

    # Настройки
    def _Settings(self):

        self.Settings = SettingsJSON()

    # Действия
    def _Actions(self):

        self.Action = ActionJSON()

    # Управление приборами учетa
    def _MeterDeviceManagement(self):
        self.MeterDeviceManagement = MeterDeviceManagementJSON()

    # Опрос приборов учета - данные приборов учета
    def _MeterData(self):
        self.MeterData = MeterDataJSON()