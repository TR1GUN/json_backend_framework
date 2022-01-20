# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path

class TemplateMeterDataMoment(TemplateFunctional):
    """
    Шаблон Опроса приборов учета

    """
    # URL

    _path_url = url_path.get("Meter_Data_moment")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    def request_settings(self, data):
        """
        Запросить данные - POST

        :param data:
        :return:
        """

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

