# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Установки времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_MeterManagement

class TemplateTimeMeterSetting(TemplateDeviceFunctions_MeterManagement):
    """
    Шаблон Установки времени

    """
    # URL

    _path_url = url_path.get("Meter_Time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    def _getting_settings(self):
        """
        Проверяем значение реле
        """
        return {}

    def Sync(self, data=None):
        """
        Синхронизация времени на счетчике по его MeterIdx

        """
        if data is None:
            data = self._getting_settings()

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------