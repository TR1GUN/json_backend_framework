# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки менеджера системы событий
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Settings


class TemplateEventManager(TemplateDeviceFunctions_Settings):
    """
    Настройки менеджера системы событий

    """
    # URL

    _path_url = url_path.get("Events_Manager")

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
