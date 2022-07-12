# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Состояние модема
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_InfoState


class TemplateStateModem(TemplateDeviceFunctions_InfoState):
    """
     Шаблон  - Состояние модема

    """
    # URL
    _path_url = url_path.get("State_Modem")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------