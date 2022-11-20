### Приложение для аннотирования текстов на русском языке на основе [модели](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) Ильи Гусева.

#### 1. Основные используемые библиотеки:
- [FastAPI](https://www.google.com)
- [Huggingface](https://huggingface.co/)
- [Pytorch](https://pytorch.org/)

#### 2. Запуск на локальном компьютере
 - создаем и активируем локальное окружение (автор использует [conda](https://docs.conda.io/en/latest/));
 - устанавливаем необходимые пакеты (environment.yml или requirements.txt);
 - запускаем веб-сервер командой ```python -m uvicorn app:app --reload ```.

#### 3. Запуск в [docker](https://www.docker.com/).

Создаем контейнер
```
docker build . -t fastapiapp  --progress=plain
```

Запускаем контейнер
```
docker run -p 8000:8000 fastapiapp
```

#### 4. Пример запроса:
```
curl -X 'POST' \
  'http://localhost:8000/summarize/' \
  -H 'Content-Type: application/json' \
  -d '{ "text": "I hate machine learning engineering!" }'
```