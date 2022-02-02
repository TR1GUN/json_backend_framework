# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон состояния линий питания интерфейсов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.TemplateDeviceFunctions import TemplateDeviceFunctions_InfoState

class TemplateStateDOut(TemplateDeviceFunctions_InfoState):
    """
    Шаблон состояния линий питания интерфейсов

    """
    # URL

    _path_url = url_path.get("State_Dout")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

    # def _read_settings(self):
    #     """
    #     Читаем данные - GET
    #     :return:
    #     """
    #     # делаем запрос - получаем ответ
    #     response = self._request_GET()
    #
    #     return response