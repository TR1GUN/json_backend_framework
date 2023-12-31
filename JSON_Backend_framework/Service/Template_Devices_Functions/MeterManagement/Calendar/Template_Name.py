# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Имя календаря тарифного расписания
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterManagement


class TemplateCalendarName(TemplateDeviceFunctions_MeterManagement):
    """
    Шаблон Имя календаря тарифного расписания

    """
    # URL

    _path_url = url_path.get("Set_Calendar_Name")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
