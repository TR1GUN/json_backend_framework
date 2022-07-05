# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнал отправки почтовых сообщений
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Journal


class TemplateJournalMailSend(TemplateDeviceFunctions_Journal):
    """
    Шаблон Журнала отправки почтовых сообщений
    """
    # URL
    _path_url = url_path.get("Journal_Mail_send")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию
