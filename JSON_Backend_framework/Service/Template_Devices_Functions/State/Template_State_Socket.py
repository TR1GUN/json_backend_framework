# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Состояние сокетов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_InfoState


class TemplateStateSocket(TemplateDeviceFunctions_InfoState):
    """
     Шаблон  - Состояние сокетов

    """
    # URL
    _path_url = url_path.get("State_Socket")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------