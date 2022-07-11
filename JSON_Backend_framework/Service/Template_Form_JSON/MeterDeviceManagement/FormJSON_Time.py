# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                           Установка времени на Счетчике
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------

class TemplateFormJSON_MeterTimeSync:
    """
    Установка времени на Счетчике
    """
    # Готовый запрос
    _Setting_MeterTimeSync = None

    # ID счетчика
    _MeterId = None

    # Добавляем
    def add_Value(self, MeterIdx: int):
        """
        Установка прибора учета для синхронизации времени на нем

        """
        try:
            self._MeterId = int(MeterIdx)
        except Exception as e:
            error = "Error value Meter Id: " + str(MeterIdx) + ".\n Error Exception : " + str(e)
            print(error)
            self._MeterId = 0

    # Удаляем
    def remove_Value(self):
        """
        Удаление записанного прибора учета
        """
        self._MeterId = None

    def get_JSON(self):
        """
        Получаем наши данные что составили
        """
        self._Setting_MeterTimeSync = \
            {
                "id": int(self._MeterId)
            }

        return self._Setting_MeterTimeSync
