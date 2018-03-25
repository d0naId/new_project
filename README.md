# Flask
здесь на простом примере показано, как работает  flask, на примере модели оценки отзыва к фильму.

Основной код лежит в файле demo.py его и следует запускать в командной строке командой:

*python demo.py*

терминал сообщит вам о том, что был запущен процесс:

*Preparing classifier  
Classifier is ready  
0.3418259620666504 seconds  
 \* Running on http://IP:5000/*  
 Переходим по указанному адресу (вместо букв IP будет непосредственно IP)
 
 Перед Вами открывается окно, в котором предлагается вставить текст отзыва и оценить позитивный или негативный этот отзыв
 
 ![Пустое поле](https://img-fotki.yandex.ru/get/479032/26569126.0/0_18dd15_eebc2419_orig.png)
 
 ![Негативный отзыв](https://img-fotki.yandex.ru/get/1022004/26569126.0/0_18dd16_74587e45_orig.png)
 
 ![Позитивный отзыв](https://img-fotki.yandex.ru/get/1025205/26569126.0/0_18dd18_85590b05_orig.png)

# Модель
Здесь как раз минимум сложностей
в файле pipeline_log.pkl упакован pickle файл с sklern-овским pipelin-ом, в котором последовательно векторизатор и логистическая регрессия.
Для удобства работы создан файл sentiment_classifier.py, в котором написан класс SentimentClassifier для упрощения использования модели.
Проект сделан в рамках прохождения курса [Анализ данных: финальный проект](https://www.coursera.org/learn/data-analysis-project/home/welcome) by Moscow Institute of Physics and Technology & Yandex
