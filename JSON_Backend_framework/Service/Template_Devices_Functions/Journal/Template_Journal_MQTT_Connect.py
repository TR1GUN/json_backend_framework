# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнал установки связи с MQTT брокером
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Journal


class TemplateJournalMQTTConnect(TemplateDeviceFunctions_Journal):
    """
    Шаблон Журнала установки связи с MQTT брокером
    """
    # URL
    _path_url = url_path.get("Journal_MQTT_connect")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию
