# JSON-Backend-Tests

Здесь расположим тесты для JSON-Backend



-----------
### ChargeStationTable

Таблица зарядных станций

- `read_settings()` - Читаем данные - GET
- `write_settings()` - Добавляем на запись данные - POST    
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `rewrite_settings()` - Перезаписываем данные - PUT      
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `delete_settings()` - Удаляем данные - DELETE     
   - `data`: Данные в Формате JSON - Если None - то используем добавленные данные - Если их нет, то никакой idx не будет задан
    
Пример JSON который можно отправлять на запись\перезапись
```json
{
  settings: {
                'addr': IP_address,
                'id': Device_idx,
                'mqttId': ID_MQTT,
                'port': IP_port,
                'type': type
            }
}
```
Пример JSON который можно отправлять на удаление
```json
{
  settings : {
                'id': []
             }
}
```

Добавление своих элементов массива по-одному     
В классе есть поле `Data_Settings` через который можно добавлять свои настройки для использования в основном классе.   
Это поле является объектом класса со своими методами.   
Методы Класса:
- `add_settings()` - Добавление настроек для записи :   
  - `Device_idx` - int - ID станции - поле  id
  - `IP_address` - str - IP адрес станции  - поле  addr
  - `IP_port` - int - IP порт станции  - поле  port
  - `ID_MQTT` - int - ID MQTT брокера - поле  mqttId
  - `type` -  str - Тип станции - По умолчанию заполняется значением ZSE-500T (Единственное поддерживаемое значение) - поле type
  

- `remove_settings()` -  Удаление добавленной записи settings для записи по ID    
  - `idx` - list or int
  
- `get_settings()` - Получаем добавленные settings

- `add_ids()` - Добавляем Device_id для запроса данных или удаления
  - `ids` - Сам Id

- `remove_ids()` - Удаление добавленной записи ids для получения/удаления записей
  - `param ids` - list or int
  
- `get_ids` - Получаем добавленные settings

-----------









#Примеры JSON :

-----------
## :floppy_disk: Для таблицы chargeStations

### POST
Запрос
```json
{"method": "post", "data": [{"table": "chargeStations", "values": [{"id": 1, "type": "ZSE-500T", "addr": "2322", "port": 1231, "mqttId": 2321}]}]}
```
Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
### GET
Запрос
```json
{"method": "get", "data": [{"table": "chargeStations"}]}
```
Варианты ответа:
```json
{"data" :[{"table" : "chargeStations","values" :[{"addr" : "2322", "id" : 2, "mqttId" : 0, "port" : 1231, "type" : "ZSE-500T"}]}],"res" : 0.0 }
```
### PUT
Запрос
```json
 {"method": "put", "data": [{"table": "chargeStations", "values": [
 {"id": 1, "type": "ZSE-500T", "addr": "2322", "port": 1231, "mqttId": 2321}]}]}
```

Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
### DELETE
Запрос
```json
{"method": "delete", "data": [{"table": "chargeStations","ids":[1]}]}
```
```json
{"method": "delete", "data": [{"table": "chargeStations"}]}
```

Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
-----------