# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнала изменения времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Journal


class TemplateJournalTime(TemplateDeviceFunctions_Journal):
    """
    Шаблон Журнала изменения времени

    """
    # URL

    _path_url = url_path.get("Journal_time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию
