# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     ШАБЛОН Настройки регулярной отправки почтовых сообщений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Settings


class TemplateActionsSMTP(TemplateDeviceFunctions_Settings):
    """
    ШАБЛОН Настройки регулярной отправки почтовых сообщений

    """
    # URL

    _path_url = url_path.get("Actions_SMTP")

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
