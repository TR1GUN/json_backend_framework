# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки последовательных интерфейсов(UART)
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Interface_UART_settings import \
    TemplateInterface_UART
from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Interface_UART import SettingsUART
# -------------------------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------------------------


class Interface_UART(TemplateInterface_UART):
    """
    Настройки последовательных интерфейсов(UART)

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = SettingsUART()

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки последовательных интерфейсов(UART)

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    def _getting_settings(self):

        """

        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса

        """
        # Читаем что задали
        SettingsUART_JSON = self.Settings.get_settings()
        UART = SettingsUART_JSON.get(self._Settings_name)

        if UART is not None:
            # Если НИЧЕГО НЕ ДОБАВЛЯЛИ , используем из GET запроса
            if len(UART) > 0:
                data = UART
            else:
                data = self._request_setting()
        else:
            data = self._request_setting()
        return data




# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------------------------
