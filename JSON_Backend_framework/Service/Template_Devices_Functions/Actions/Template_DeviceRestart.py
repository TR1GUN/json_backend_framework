# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                        Шаблон для перезагрузки
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path


class TemplateDeviceRestart(TemplateFunctional):
    """

    Шаблон для перезагрузки

    """
    # URL

    _path_url = url_path.get("Restart")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    def Restart(self):
        """
        Берем и перезагружаем устройство
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


