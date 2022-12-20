### Приложение для аннотирования текстов на русском языке на основе [модели](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) Ильи Гусева.

#### 1. Основные используемые библиотеки
- [FastAPI](https://www.google.com)
- [Huggingface](https://huggingface.co/)
- [Pytorch](https://pytorch.org/)

#### 2. Развернутое приложение в Яндекс.Облако

##### Пример GET запроса:

```
http://158.160.22.185:8000?q=Актуальность проблемы. Электронная информация играет все большую роль во всех сферах жизни современного общества. В последние годы объем научно-технической текстовой информации в электронном виде возрос настолько, что возникает угроза обесценивания этой информации в связи с трудностями поиска необходимых сведений среди множества доступных текстов. Развитие информационных ресурсов Интернет многократно усугубило проблему информационной перегрузки. В этой ситуации особенно актуальными становятся методы автоматизации реферирования текстовой информации, то есть методы получения сжатого представления текстовых документов–рефератов (аннотаций). Постановка проблемы автоматического реферирования текста и соответственно попытки ее решения с использованием различных подходов предпринимались многими исследователями.
```

##### Пример POST запроса в postman
![Пример запроса в postman](./img/img_1.png)

##### Пример POST запроса в curl
```
curl -X 'POST' \
  'http://158.160.22.185:8000/summarize/' \
  -H 'Content-Type: application/json' \
  -d '{ "text": "I hate machine learning engineering!" }'
```