# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнала фиксации ответов приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Journal


class TemplateJournalMeterAnswer(TemplateDeviceFunctions_Journal):
    """
    Шаблон Журнала фиксации ответов приборов учета

    """
    # URL

    _path_url = url_path.get("Journal_Meter_ANSW")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Настройки по умолчанию
    # Переопределяем чтоб можно было достать
    path_url = _path_url
