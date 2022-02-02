# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Управления реле
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterManagement

class TemplateRelayControl(TemplateDeviceFunctions_MeterManagement):
    """
    Шаблон Управления реле

    """
    # URL

    _path_url = url_path.get("Meter_Relay")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


