# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Дата активации тарифного расписания
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterManagement


class TemplateCalendarTime(TemplateDeviceFunctions_MeterManagement):
    """
    Шаблон Дата активации тарифного расписания

    """
    # URL

    _path_url = url_path.get("Set_Calendar_Time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
