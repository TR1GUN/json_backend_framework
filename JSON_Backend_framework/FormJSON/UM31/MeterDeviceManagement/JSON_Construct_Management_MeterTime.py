# -------------------------------------------------------------------------------------------------------------
#                                        Класс для Формирования Правильного JSON
#                                                   Протокол УМ-31 СМАРТ
#                                               Установка времени на Счетчике
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Form_JSON.MeterDeviceManagement.FormJSON_Time import TemplateFormJSON_MeterTimeSync

# -------------------------------------------------------------------------------------------------------------


class FormJSON_MeterTimeSync(TemplateFormJSON_MeterTimeSync):
    """
    Сборка JSON - Установка времени на Счетчике
    """
    # Готовый запрос
    _Setting_MeterTimeSync = None

    # ID счетчика
    _MeterId = None

    def __init__(self):
        """
        Сборка JSON - Управление реле
        """
        self._Setting_MeterTimeSync = None

