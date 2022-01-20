# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Текущее время
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.settings import url_path
from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional


class TemplateStateTime(TemplateFunctional):
    """
     Шаблон  - Текущее время

    """
    # URL
    _path_url = url_path.get("State_Time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Настройки по умолчанию

    def _read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response