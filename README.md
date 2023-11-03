# Онлайн шахматы
Выполнили: Дунин Даниил, Чернов Никита

# Описание продукта
Данное приложение является реализацией настольной игры шахматы, в основе
которой лежит клиент-серверная архитектура. Приложение поддерживает
игру как со случайным соперником, так и с ботом разной сложности.

# Подробности реализации
Изначально запускается сервер в котором обрабатывается внутренняя логика
шахматной партии: от анализа возможных ходов, до взаимодействия между
клиентами. После подключаются либо игровые боты, либо игроки, каждого
из которых мы реализовали как клиента. Они отправляют запросы на сервер 
и в ответ получают соответствующую информацию: о местоположении фигур на
доске, о статусе партии, об отрисовки возможных ходов.

# Архитектура проекта
В папке Server хранятся скрипты с всей логикой сервера, для его запуска, понадобится конкретно mainServer(). Реализация клиентов как игроков находится в Client, а ботов - сильного и слабого - в EasyBot и HardBot, запускать также с помощью main скриптов. Также написано 49 тестов с итоговым покрытием 90%.

# Правила шахмат
Ознакомиться с ними можно перейдя по этой ссылке: https://www.chess.com/ru/kak-igrat-v-shakhmaty

Приятной игры!