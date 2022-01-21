# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# импортируем наши классы

from JSON_Backend_framework.Service.TemplateUSPD import Template_USPD


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class UM_40_SMART(Template_USPD):
    """
    Функционал УМ - 40 СМАРТ

    """

    _ip_address = ''

    def __init__(self, ip_address=None):
        """
        Получаем функционал доступный в УМ-40 СМАРТ

        """
        # Устанавливаем IP адрес

        self._ip_address = str(ip_address)

        # Логин
        self._Login = ''
        # Пароль
        self._Password = ''

        # И обновляем функционал
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Настройки
        self._Settings()
        self._StateInfo()
        self._Journal()
        self._Actions()
        self._MeterDeviceManagement()
        self._MeterData()

    def _Settings(self):
        """
        Получаем Класс который работает с настройками УСПД
        :return:
        """

        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Settings import UM_40_SMART_Settings
        self.Settings = UM_40_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Состояние Изделия
    def _StateInfo(self):
        """
        Получаем Класс который работает с Информация о состоянии УСПД
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_StateInfo import UM_40_SMART_StateInfo
        self.StateInfo = UM_40_SMART_StateInfo(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # ЖУРАНЛЫ
    def _Journal(self):

        """
        Получаем класс который работает с Журналами УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Journal import UM_40_SMART_Journal

        self.Journal = UM_40_SMART_Journal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Действия
    def _Actions(self):

        """
        Получаем класс который работает с Действия УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Actions import UM_40_SMART_Actions

        self.Action = UM_40_SMART_Actions(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Управление Приборами учета
    def _MeterDeviceManagement(self):

        """
        Получаем класс который работает с Действия УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_MeterDeviceManagement import UM_40_SMART_MeterDeviceManagement

        self.MeterDeviceManagement = UM_40_SMART_MeterDeviceManagement(
                                                                        cookies=self._cookies,
                                                                        headers=self._headers,
                                                                        ip_address=self._ip_address
                                                                       )
    # Опрос Приборов Учета - Данные приборов учета
    def _MeterData(self):

        """

        Получаем класс который работает с Действия УСПД

        """
        from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_MeterData import UM_40_SMART_MeterData

        self.MeterData = UM_40_SMART_MeterData(cookies=self._cookies, headers=self._headers,ip_address=self._ip_address)
