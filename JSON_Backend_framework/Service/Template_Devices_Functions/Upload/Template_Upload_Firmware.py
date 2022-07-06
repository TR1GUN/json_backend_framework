# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Загрузка файлов обновления ВПО
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_Upload


class TemplateUpLoadFirmware(TemplateDeviceFunctions_Upload):
    """
     Шаблон  - Загрузка файлов обновления ВПО

    """
    # URL

    _path_url = url_path.get("Upload_firmware")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

