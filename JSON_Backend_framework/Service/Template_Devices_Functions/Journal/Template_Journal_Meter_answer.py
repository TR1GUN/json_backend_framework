# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Журнала фиксации ответов приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path


class TemplateJournalMeterAnswer(TemplateFunctional):
    """
    Шаблон Журнала фиксации ответов приборов учета

    """
    # URL

    _path_url = url_path.get("Journal_Meter_ANSW")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Настройки по умолчанию
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    def Read_Journal(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response
