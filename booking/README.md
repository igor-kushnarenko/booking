# Структура БД составленной по дизайну
Дизайн: https://www.figma.com/file/h7DVtchQ84o9fK4CXKANHK/%D0%9F%D0%B0%D1%80%D0%BA-%D0%9B%D0%B0%D1%81%D0%BA%D0%B8%D0%BD%D0%BE?node-id=0%3A1

# ER-диаграмма
https://drawsql.app/pa_group/diagrams/booking#

# API
1. pip install requirements.txt
2. install postgreSQL
4. http://127.0.0.1:8000/api/

# Краткое описание БД - из каких таблиц и представлений состоит.
1. visit

id - PK

user_id - идентификатор пользователя

date_visit - дата визита

time_id - временной период

servise_id - вид услуги


2. user

id - PK

first_name - имя пользователя

last_name - фамилия пользователя

birthday - дата рождения



3. auth

id - PK

user_id - идентификатор пользователя

login - логин

password - пароль



4. auth

id - PK

user_id - идентификатор пользователя

login - логин

password - пароль


5. service

id - PK

name - наименование услуги


6. vault

id - PK

service_id - идентификатор услуги

vault_number - номер сейфа



7. seats

id - PK

service_id - идентификатор услуги

seat_number - номер шезлонга

fare_conditions - условия использования



8. ticket

id - PK

visit_id - идентификатор визита

reservation_id - идентификатор резервирования

ticket_number - номер билета

number_persons - количество персон

rate_id - идентификатор тарифа


9. reservation

id - PK

reservation_date - дата резервации

time_reservation - время резервации


10. rate

id - PK

name - наименование тарифа

price - стоимость тарифа


11. bill

id - PK

ticket_id - идентификатор билета

user_id - идентификатор пользователя

rate_it - идентификатор тарифа


12. bill

id - PK

ticket_id - идентификатор билета

user_id - идентификатор пользователя

rate_it - идентификатор тарифа



13. time

id - PK

name - наивенование временного промежутка
