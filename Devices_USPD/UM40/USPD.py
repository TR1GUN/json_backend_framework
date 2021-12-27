# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# импортируем наши классы

from Service.TemplateUSPD import Template_USPD


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
class UM_40_SMART(Template_USPD):
    """
    Функционал УМ - 40 СМАРТ

    """
    # IP Адрес
    from Service.config import machine_ip
    ip_address = str(machine_ip)

    def __init__(self, ip_address=None):
        """
        Получаем функционал доступный в УМ-40 СМАРТ

        :param ip_address: IP адрес УСПД. Значение по умолчанию - None - Используется значение из файла settings.ini
        """
        # Устанавливаем IP адрес если его дали
        if ip_address is not None:
            self._ip_address = str(ip_address)
        # Иначе - Используем адрес из настроек
        else:
            self._ip_address = self._IP_address_from_config()

        # И обновляем функционал
        self._define_functionality()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Настройки
        self._Settings()

    def _Settings(self):
        """
        Получаем Класс который работает с настройками УСПД
        :return:
        """

        from Devices_USPD.UM40.Service.USPD_Settings import UM_40_SMART_Settings
        self.Settings = UM_40_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

        # self.USPD = UM_40_SMART_USPD(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
        # self.MeterDevices = UM_40_SMART_Meter(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)
