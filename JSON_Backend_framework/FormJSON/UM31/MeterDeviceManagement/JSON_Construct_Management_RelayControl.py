# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                   Протокол УМ-31 СМАРТ
#                                                      Управление реле
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Form_JSON.MeterDeviceManagement.FormJSON_Relay import TemplateFormJSON_Relay

# -------------------------------------------------------------------------------------------------------------


class FormJSON_Relay(TemplateFormJSON_Relay):
    """
    Сборка JSON - Управление реле
    """
    # Готовый запрос
    _Setting_Relay = None

    # ID счетчика
    _MeterId = None
    # ID реле
    _RelayId = None
    # Положение реле
    _RelayState = None

    def __init__(self):
        """
        Сборка JSON - Управление реле
        """
        self._Setting_Relay = None
