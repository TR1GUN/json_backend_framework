# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Шаблон Установки времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from Service.Template_Functional import TemplateFunctional


class TemplateTimeMeterSetting(TemplateFunctional):
    """
    Шаблон Установки времени

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Meter_Time")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def _request_set_id(self, data):
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