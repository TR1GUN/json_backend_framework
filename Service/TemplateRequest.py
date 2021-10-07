# Здесь опишем главный класс запроса от которого будем наследоваться

# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон основных данных по которым отправляется запрос
# //////////////////////////////////////////////////////////////////////////////////////////
class TemplateRequest:
    # Наш заголовок
    _http = 'http://'
    _result = {}
    _response = None

    _debug = False

    # Наш айпишник
    from Service.config import machine_ip
    ip_port = str(machine_ip)

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

    def _url_collector(self, url):
        """
        В этом методе собираем наш URL

        НУжен дял сборки валидного УРЛ , чтоб не выстреливать себе в ногу из-за слэшей и прочего
        :param url: сюда пихаем наш путь url
        :return: Возвращаем корректно собранный URL
        """

        # Первое что делаем - определяемся из каких частей состоит наш урл

        # UPD :
        # если у нас путь ровняется пустоте - выбрасываем на глагне
        if url is None:
            url = '/login'

        # Закрытое поле - не нужно выставлять
        http = self._http

        # Айпишник
        ip_port = self.ip_port

        # А тут погналась свистопляска :
        # МЫ спустили url без начинающего первого слэша
        if url[0] != '/':
            # Собирать ничего не надо
            if 'http://' in url:
                url = url
            else:
                # Проверяем - есть ли у нас айпишник уже в записи
                if url[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    # Добавляем http заголовок и все
                    url = http + url
                # иначе - думаем что ссылка прсото без слэша и проверяем уже правильно ли задан айпишник
                else:
                    # Вариант 1 - задан с http заголовком
                    if 'http://' in ip_port:
                        # Вариант 1.1 -  со слэшем в конце
                        if ip_port[-1] == '/':
                            url = ip_port + url

                        # Вариант 1.2 -  без слэша в конце
                        else:
                            url = ip_port + '/' + url
                    # Вариант 2 - задан без http заголовка
                    else:
                        # Вариант 2.1 -  со слэшем в конце
                        if ip_port[-1] == '/':
                            url = http + ip_port + url

                        # Вариант 2.2 -  без слэша в конце
                        else:
                            url = http + ip_port + '/' + url

        # Если вставили URL без слэша - Проверяем что есть в этом url
        else:
            # Проверяем - есть ли у нас айпишник уже в записи
            if url[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                url = http[:-1] + url

            # Иначе считаем что с url все хорошо
            else:
                # Теперь проверяем айпишник

                # Вариант 1 - задан с http заголовком
                if 'http://' in ip_port:
                    # Вариант 1.1 -  со слэшем в конце
                    if ip_port[-1] == '/':
                        url = ip_port[:-1] + url

                    # Вариант 1.2 -  без слэша в конце
                    else:
                        url = ip_port + url

                # Вариант 2 - задан без http заголовка
                else:
                    # Вариант 2.1 -  со слэшем в конце
                    if ip_port[-1] == '/':
                        url = http + ip_port[:-1] + url

                    # Вариант 2.2 -  без слэша в конце
                    else:
                        url = http + ip_port + url

        return url

    def get_cookies(self):
        """
        Возвращаем куки операции

        :return:
        """
        if self._response is not None:
            cookies = self._response.cookies
        else:
            cookies = None
        return cookies

    def get_headers(self):
        """
        Возвращаем headers операции

        :return:
        """
        if self._response is not None:
            headers = self._response.headers
        else:
            headers = None
        return headers

    def get_response(self):
        """
        Возвращаем класс ответа - необходимо может быть для отдали
        :return:
        """

        return self._response
