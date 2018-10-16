#!usr/bin/env python
#-*-encoding:UTF-8-*-

#==================<Имортирование необходимых модулей>==================
import urllib2
#Модуль для работы с протоколом HTTP, высокоуровневый
import urllib
#Модуль для работы с протоколом HTTP, более низкоуровневый чем urllib2, 
#фактически из него необходима одна функция - urllib.urlquote
import Queue
#Модуль, который представляет собой "Pool", фактически это список, в 
#котором на нужных местах вставлены замки таким образом, чтобы к нему 
#одновременно мог обращаться только один поток
import threading
#Модуль для работы с потоками, из него понадобится только 
#threading.active_count, threading.Thread, threading.Thread.start, 
#threading.Rlock
import re
#Модуль для работы с регулярными выражениями, его использование выходит
#за пределы статьи
import time 
#Модуль для работы со временем, из него нужна только функция sleep
queue = Queue.Queue()
#Обязательное присваивание, нужно делать именно так (т.е. импортировать
#класс Queue из модуля Queue и инициализировать его)
#==================</Имортирование необходимых модулей>=================

#==============================<Настройки>==============================
PROXY = "10.10.31.103:3128"
#Во время написания статьи сижу за прокси-сервером, поэтому в статье 
#затрагивается и этот вопрос, этой строкой обьявляется глобальная
#переменная PROXY, в которой находится адрес прокси-сервера. Для работы 
#напрямую необходимо указать значение None
HEADERS = {"User-Agent" : "Opera/9.64 (Windows NT 5.1; U; en) Presto/2.1.1",
           "Accept" : "text/html, application/xml;q=0.9, application/xhtml+xml, image/ png, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",
           "Accept-Language" : "ru,uk-UA;q=0.9,uk;q=0.8,en;q=0.7",
           "Accept-Charset" : "iso-8859-1, utf-8, utf-16, *;q=0.1",
           "Accept-Encoding" : "identity, *;q=0",
           "Connection" : "Keep-Alive"}
#Для того чтобы получить страницу с www.google.com НЕОБХОДИМО использовать
#заголовки браузера, они представлены выше в ассоциативном массиве HEADERS, 
#соответствуют реальным заголовкам браузера Opera с маленько модификацией, эти 
#заголовки означают что клиент не может принимать zlib compressed data, т.е. 
#сжатые данные - не хотел я заморачиваться еще и с разархивироанием страниц, тем 
#более что не все сайты их сжимают...
THREADS_COUNT = 10
#В принципе это все настройки приложения, это-количество потоков
DEEP = 30
#Это - значение, которое отвечает за глубину страниц поиска, которые 
#нужно просматривать, фактически же определяет собой количество ссылок, 
#которые будут собраны сборщиком.
ENCODING = "UTF-8"
#Кодировка ваших файлов (для загрузки данных из файла с запросами и 
#последующего их перевода в юникод)
#==============================</Настройки>===================================

LOCK = threading.RLock()
# Вот тут то впервые и затрагивается модуль threading
#создается обьект LOCK, который представляет собой класс threading.RLock из
#модуля threading, это -простейший замок, который запрещает исполнение 
#несколькими потоками участка кода который идет после вызова его метода 
#acquire() Основным отличием threading.RLock от threading.Lock (тоже класс из 
#модуля threading) является то, что каждый поток может обращаться к обьекту 
#threading.RLock неограниченное количество раз, обьект threading.Lock может 
#вызываться каждым потоком только единожды.
#///////////////////////////////////////////////////////////////////////
def worker():
# Обьявление функции worker, входных аргументов нет
    global queue
    #Здесь и далее я буду обьявлять функции из глобального пространства 
    #имен в локальном для лучшей читабельности кода, хотя в написании
    #софта такое делать строго не рекомендую (!)
    while True:
    #Запуск бесконечного цикла, в котором будет происходить работа
        try:
        #Обработка ошибок, блок try/except, когда обработается
        #ошибка Queue.Empty это значит, что список задач пуст, и поток 
        #должен завершить свою работу
        	target_link =  queue.get_nowait() 
            #Эта строчка олицетворяет собой получение задачи потоком из
            #списка задач queue
        except Queue.Empty, error:
        #сам перехват ошибки
            return
            #Завершение работы функции
        parsed_data = get_and_parse_page(target_link)
        #Позже будет реализована функция, которая будет получать 
        #страницу и доставать из нее необходимые значения
        if parsed_data != "ERROR":
        #Проверка на то, была ли получена страница
            write_to_file(parsed_data)
            #Также будет реализована функция для записи собранных данных в файл
        else:
            queue.put(target_link)
            #Если страница не была получена, то забрасываем ее обратно в queue
#///////////////////////////////////////////////////////////////////////
def write_to_file(parsed_data):
#Обявление функции write_to_file, аргумент –массив данных для записи
    global LOCK
    global ENCODING
    LOCK.acquire()
    #"Накидывание замка", следующий далее участок кода может выполнятся
    #только одним потоком в один и тот же момент времени
    with open("parsed_data.txt", "a") as out:
    #Используется with statement, открывается файл parsed_data.txt с
    #правами "a", что означает дозапись в конец файла, и присваиваевается
    #хэндлеру на файл имя out (я так привык)
        for site in parsed_data:
        #Проход циклом по всем элементам parsed data, имя активного в 
        #данный момент элемента будет site
            link, title = site[0], site[1]
            #Присваивание переменным link и title значений из кортежа site
            title = title.replace("<em>", "").replace("</em>", "").replace("<b>", "").replace("</b>", "")
            #.replace -это замена HTML-тэгов, которые проскакивают в title и совершено не нужны
            out.write(u"{link}|{title}\n".format(link=link, title=title).encode("cp1251"))
            #Производится сама запись в файл, используется оператор форматирования 
            #строк .format, в отличие от % он поддерживает именованные аргументы, чем я и не 
            #преминул воспользоваться, таким образом в файл пишется строка вида:
            #ссылка на сайт | title страницы\n -символ переноса строки(все это переводится
            #из юникода в cp1251)
    LOCK.release()
    #"Отпирание"  замка, в противном случае ни один из следующих 
    #потоков не сможет работать с этим участком кода. По-хорошему, тут тоже нужно 
    #сделать обработку ошибок, но это учебный пример, да и ошибка там может 
    #возникнуть (после добавки замка в этот участок кода) только если во время
    #работы приложения выставить атрибут “только чтение” для данного пользователя
    #относительно файла parsed_data.txt
#///////////////////////////////////////////////////////////////////////
def get_and_parse_page(target_link):
#Обьявление функции, аргумент – ссылка на страницу
    global PROXY
    #Указывает на то, что в данной функции используется переменная PROXY
    #из глобального пространства имен
    global HEADERS
    #То же и для переменной Headers
    if PROXY is not None:
    #Если значение PROXY не равно None
        proxy_handler = urllib2.ProxyHandler( { "http": "http://"+PROXY+"/" } )
        #Создается Прокси-Хэндлер с указанным прокси
        opener = urllib2.build_opener(proxy_handler)
        #Далее создается opener c созданным ранее Прокси-Хэндлером
        urllib2.install_opener(opener)
        #И наконец-то он устанавливается, теперь нет необходимости в 
        #шаманствах, все запросы в которых будет использоваться urllib2 
        #(в пределах этой функции будут направляться через указанный ранее 
        #PROXY)
    page_request = urllib2.Request(url=target_link, headers=HEADERS)
    #Создается обьект Request, который олицетворяет собой Request instance,
    #фактически это GET запрос к серверу с указанными параметрами, мне 
    #же необходимо использовать заголовки...
    try:
    #Обработка всех возможных ошибок, возникающих во время получения
    #страницы, это нехорошо, но лучше чем полное отсутствие обработки
        page = urllib2.urlopen(url=page_request).read().decode("UTF-8", "replace")
        #Переменной page присваиваем прочитанное значение страницы запроса, переведенное 
        #в unicode из кодировки UTF-8 (кодировка, используемая на www.google.com) (в 
        #Python 2.6 unicode -это отдельный тип данных(!))
    except Exception ,error:
    #Сам перехват ошибки и сохранение ее значения в переменную error
        print str(error)
        #Вывод ошибки в консоль, прведварительно переведя ее в строку 
        #(просто на всякий случай)
        return "ERROR"
        #Возврат из функции в том случае, если во время работы возникла ошибка
    harvested_data = re.findall(r'''\<li\ class\=g\>\<h3\ class\=r\>\<a\ href\=\"(.*?)".*?>(.*?)\<\/a\>\<\/h3\>''', page)
    #Сбор со страницы поиска ссылок и title найденных страниц
    #Очистка данных от результатов поиска по блогам, картинкам и др. сервисам гугла
    for data in harvested_data:
    #Для каждого элемента массива harvested_data присвоить ему имя data
        if data[0].startswith("/"):
        #Если нулевой элемент массива data(ссылка) начинается с символа /
            harvested_data.remove(data)
            #Удаляем его из массива harvested_data
        if ".google.com" in data[0]:
        #Если нулевой элемент массива data(ссылка) имеет в себе .google.com
            harvested_data.remove(data)
            #Также удаляем его из массива harvested_data
    return harvested_data
    #Возвращаем собранные значения из функции
#///////////////////////////////////////////////////////////////////////
def main():
#Обявление функции, входных аргментов нет
    print "STARTED"
    #Вывод в консоль о начале процесса
    global THREADS_COUNT
    global DEEP
    global ENCODING
    #Обьявляние о том что эти переменные будут использоваться
    #из глобального пространства имен
    with open("requests.txt") as requests:
    #Открываем файл requests в котором находятся запросы к поисковику
         for request in requests:
         #На данном файлхэндлере доступен итератор, поэтому можно 
         #пройтись по файлу циклом, без загрузки файл в оперативку, но это 
         #тоже не важно, я все равно его туда загружу:)
                request = request.translate(None, "\r\n").decode(ENCODING, "replace")
                #Очистка запроса от символов конца строки а также их 
                #перевод в юникод (с заменой конфликтных символов)
                empty_link = "http://www.google.com/search?hl=ru&client=opera&rls=ru&hs=67v&q={request}&start={N}&sa=N"
                #Это пустой адрес страницы поиска, отформатирован
                for i in xrange(0, DEEP, 10):
                #Проход итератором по диапазону #чисел от 0 до DEEP, 
                #который представляет собой максимальную глубину поиска с 
                #шагом в 10, т.е. получаем из этого диапазона только 
                #числа десятков, т.е. 10, 20, 30 (как идет поиск у гугла)
                     queue.put(empty_link.format(request=request.encode("UTF-8"), N=i))
                     #Добавление в очередь каждой сгенерированной ссылки
                     #и перевод её в кодировку UTF-8 (для гугла)
    for _ in xrange(THREADS_COUNT):
    #Проход циклом по диапазону чисел количества потоков
        thread_ = threading.Thread(target=worker)
        #Создается поток, target-имя функции, которая являет собой 
        #участок кода, выполняемый многопоточно
        thread_.start()
        #Вызывается метод start() , таким образом поток запускается
    while threading.active_count() >1:
    #До тех пор, пока количество активных потоков больше 1 (значит, 
    #запущенные потоки продолжают работу)
        time.sleep(1)
        #Основной поток засыпает на 1 секунду
    print "FINISHED"
    #Вывод в консоль о завершении работы приложения
#///////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    main()
    