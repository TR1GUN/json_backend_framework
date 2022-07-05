# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнал поднятия PPP-сервера (CSD)
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Journal


class TemplateJournalPPPServerConnect(TemplateDeviceFunctions_Journal):
    """
    Шаблон Журнала поднятия PPP-сервера (CSD)
    """
    # URL
    _path_url = url_path.get("Journal_PPP_Server_connections")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию
