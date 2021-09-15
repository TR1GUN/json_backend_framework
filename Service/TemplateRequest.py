# Здесь опишем главный класс запроса от которого будем наследоваться

# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон основных данных по которым отправляется запрос
# //////////////////////////////////////////////////////////////////////////////////////////
class TemplateRequest:
    # Наш заголовок
    http = 'http://'
    _result = {}

    # Наш айпишник
    from Service.config import machine_ip
    ip_port = machine_ip

    def Result(self):
        """
        Возвращаем  общий словарь результатов
        :return:
        """
        return self._result

    def GET_data(self):
        """
        Возвращаем поле дата
        :return:
        """
        return self._result.get("data")

    def GET_result_code(self):
        """
        Возвращаем результат работы
        :return:
        """
        return self._result.get("code")

