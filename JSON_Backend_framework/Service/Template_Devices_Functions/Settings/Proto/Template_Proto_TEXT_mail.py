# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон настроек почтовых сообщений текстового протокола
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Settings


class TemplateProtoTextMail(TemplateDeviceFunctions_Settings):
    """
    Шаблон Настройки почтовых сообщений текстового протокола

    """
    # URL
    _path_url = url_path.get("Protocol_TEXT_mail")

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
