# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Поверка внешних ЧРВ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Actions_Set


class TemplateActionTimeCheck(TemplateDeviceFunctions_Actions_Set):
    """
     Шаблон  - Поверка внешних ЧРВ

    """
    # URL
    _path_url = url_path.get("Time_check")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------