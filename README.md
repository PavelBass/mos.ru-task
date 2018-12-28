# some_company Job challenge

## Задание

Реализовать асинхронный HTTP-сервер, обрабатывающий поисковые запросы пользователей.

Работа сервиса описывается так:

1. Сервис принимает текстовый запрос пользователя.
2. Определяет, к какой теме или темам может принадлежать запрос (подробности см. ниже).
3. Выдает результат в формате json, в котором указан список соответствущих запросу тем.

Каждая тема определяется набором фраз, например:

- новости: "деревья на Садовом кольце", "добрый автобус", "выставка IT-технологий";
- кухня: "рецепт борща", "яблочный пирог", "тайская кухня";
- товары: "Дети капитана Гранта", "зимние шины", "Тайская кухня";

или любые другие, на ваше усмотрение. Важно, чтобы какая-то из фраз встретилась в нескольких наборах индексов, как "тайская кухня" в примере.
Предполагается, что наборы фраз все умещаются в оперативной памяти, но при этом могут быть достаточно большими.

Правило принадлежности запроса теме:

1. Если набор слов из запроса содержит в себе все слова какой-либо из фраз, то запрос считается соответствующим теме. Иначе - не соответствующим.
2. Порядок слов в запросе и во фразах не учитывается.

Примеры:

Запрос "где купить зимние шины" соответствует теме "товары", т.к. содержит в себе все слова из фразы "зимние шины".
Запрос "борща любимого рецепт" соответствует теме "кухня", т.к. содержит в себе все слова из фразы "рецепт борща".
Запрос "тайская кухня" соответствует двум темам: "кухня" и "товары".
Запрос "кухня" не соответствует ни одной теме, т.к. не включает в себя целиком слова ни одной из фраз.