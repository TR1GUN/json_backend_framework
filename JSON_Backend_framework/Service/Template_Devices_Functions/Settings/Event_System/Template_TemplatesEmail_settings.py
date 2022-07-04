# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     Шаблоны Email адресов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Settings


class TemplateTemplatesEmail(TemplateDeviceFunctions_Settings):
    """
    Шаблоны Email адресов

    """
    # URL

    _path_url = url_path.get("Template_Email")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Имя поля настроек
    _Settings_name = 'Settings'

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
