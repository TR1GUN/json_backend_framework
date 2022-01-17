# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон состояния линий питания интерфейсов
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional


class TemplateStateDOut(TemplateFunctional):
    """
    Шаблон состояния линий питания интерфейсов

    """
    # URL
    from JSON_Backend_framework.Devices_USPD.settings import url_path
    _path_url = url_path.get("State_Dout")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Настройки по умолчанию

    def _read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response