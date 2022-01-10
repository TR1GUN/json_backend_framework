# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон  - Текущее время
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from Service.Template_Functional import TemplateFunctional


class TemplateStateTime(TemplateFunctional):
    """
     Шаблон  - Текущее время

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("State_Time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Настройки по умолчанию

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response