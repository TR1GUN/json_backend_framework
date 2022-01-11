# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнала изменения времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class TemplateJournalTime(TemplateFunctional):
    """
    Шаблон Журнала изменения времени

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Journal_time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Настройки по умолчанию

    def read_Journal(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response
