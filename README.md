## Контекст задачи
Когда ваш бизнес предполагает анализ статистических данных, поступающих из разных источников, вам требуется эти данные собирать, хранить, индексировать, трансформировать в другие данные, анализировать и т.д.

Часто бывает так, что масштаб проекта ещё недостаточно велик для внедрения крупных программных платформ наподобие Hadoop, и в этом случае вам помогут универсальные варианты на базе стандартных NoSQL-решений, которые позволят справиться с накоплением и обработкой данных среднего объёма.

К таким решениям, исходя из нашей практики, относится [Elasticsearch](https://www.elastic.co/products/elasticsearch).
## Что такое Elasticsearch
[Elasticsearch](https://www.elastic.co/products/elasticsearch) — это представитель кластерных NoSQL с JSON REST API. Elasticsearch — это нечто большее, чем просто поисковая система, она поддерживает сложные агрегации, геофильтры и список продолжается. И самое прекрасное это скорость получение запросов. 
Мы можем считать его и не реляционным хранилищем документов в формате JSON, и поисковой системой на базе полнотекстового поиска [Lucene](https://ru.wikipedia.org/wiki/Lucene).

Аппаратная платформа — Java Virtual Machine.

Официальные клиенты доступны на Java, NET (C#), Python, Groovy, JavaScript, PHP, Perl, Ruby.

Elasticsearch разрабатывается компанией Elastic вместе со связанными проектами, называемыми Elastic Stack, — [Elasticsearch](https://www.elastic.co/products/elasticsearch), [Logstash](https://www.elastic.co/products/logstash), [Beats](https://www.elastic.co/products/beats) и [Kibana](https://www.elastic.co/products/kibana).

Beats — легковесные агенты и отправители данных с различных устройств. Logstash собирает и обрабатывает данные зарегистрированных событий. За хранение и поиск данных отвечает Elasticsearch. Kibana визуализирует данные через web-интерфейс.

Сегодня Elastic Stack с успехом используется сервисами eBay, Adobe, Uber, Nvidia, Blizzard, Citibank, Volkswagen, Microsoft, SoundCloud, GitHub, Netflix, Amazon.
## Основные понятия Elasticsearch
| **SQL**         | **Elasticsearch** |
| -------------   | ----------------  |
| База данных     | Индекс            | 
| Таблица         | Тип               |
| Ряд             | Документ          |
| Колонка         | Поле              |
### Индекс
Индекс похож на базу данных. Термин индекс не следует путать с индексом базы данных, как можно предложить если вы знакомы с реляционными базами данных. Индекс подразумевает логическую группировку Типов (таблиц). Имя индекса должно быть уникальным и состоять из строчных букв.
### Тип
Тип похож на таблицу базы данных, индекс может иметь один или несколько типов. Тип — это логическое разделение различных видов данных. Например, если вы создаете приложение для блога, можно предложить создать тип для статей и комментариев.
### Документ
В Elasticsearch данные хранятся в виде документов JSON (Javascript Object Notation). Большинство хранилищ данных NoSQL используют JSON для хранения своих данных, поскольку формат JSON очень лаконичный, гибкий и понятный людям. Документ в Elasticsearch очень похож на строку по сравнению с реляционной базой данных.
### Кластер и узел
В традиционных базах данных обычно у нас есть только один сервер, обслуживающий все запросы. Elasticsearch — это распределенная система, что означает она состоит из одного или нескольких узлов, которые действуют как одно целое, что позволяет масштабировать и обрабатывать нагрузку, превышающую то, что может обработать один сервер. Каждый узел (сервер) имеет часть данных. Вы можете запустить Elasticsearch только с одним узлом, а затем добавить больше узлов или другими словами, масштабировать кластер, когда количество данных превышает возможности одного сервер. 

![image](https://user-images.githubusercontent.com/18426280/62547495-f6054f80-b86d-11e9-95e8-b2f1bd4b7a43.png)

На рисунке выше кластер имеет три узла с именами elasticsearch1, elasticsearch2, elasticsearch3. Эти три узла работают вместе, чтобы обрабатывать все запросы индексирования и извлечения данных. В зависимости от потребностей вашего приложения вы можете добавлять и удалять узлы (серверы) «на лету».
### Shard (осколок или шард)
Индекс представляет собой набор из одного или нескольких шардов. За счет чего Elasticsearch может хранить информацию объем которой превышает возможности одного сервера. Elasticsearch использует Apach Lucene для индексирования и обработки запросов. Шард — это не что иное, как экземпляр Apache Lucene.
## Взаимодействие с Elasticsearch
Основной способ взаимодействия с Elasticsearch — REST API. По умолчанию API — интерфейс Elasticsearch работает на порту 9200. Api можно классифицировать на следующие виды:

- API документов: CRUD (Create Retrieve Update Delete) операции с документами
- API поиска: поиск чего бы то ни было
- API Индексов: управление индексами (создание, удаление …)
- API Cat: вместо JSON данных возвращаются в табличном виде
- API кластера: для управления кластером
## Установка Elasticsearch
Для этого нам сначала потребуется [Java](https://www.oracle.com/technetwork/java/javase/downloads/index.html). 

```commandline
java --version
```

**Result:**

![image](https://user-images.githubusercontent.com/18426280/62542096-ca7d6780-b863-11e9-93d1-4c28a0d314b6.png)

Дистрибутив Elasticsearch доступен [на сайте разработчика](https://www.elastic.co/downloads/elasticsearch).
Для запуска **elasticsearch**, из папки с дистрибутивом нужно выполнить команду 
 
```commandline
bin/elasticsearch
```

**Result:**

![image](https://user-images.githubusercontent.com/18426280/62542264-20eaa600-b864-11e9-8040-7ba3cd6d5987.png)

После этого нужно перейти на `http://localhost:9200/`, чтобы убедиться, что **elasticsearch** запущен и мы всё сделали правильно. Если вы сделали всё верно, вы должны будете увидеть что-то такое:
```json
{
    "name": "GtVTB1T",
    "cluster_name": "elasticsearch",
    "cluster_uuid": "wRWP1A4ZRfiqcKnq94NHOQ",
    "version": {
        "number": "6.4.0",
        "build_flavor": "default",
        "build_type": "tar",
        "build_hash": "595516e",
        "build_date": "2018-08-17T23:18:47.308994Z",
        "build_snapshot": false,
        "lucene_version": "7.4.0",
        "minimum_wire_compatibility_version": "5.6.0",
        "minimum_index_compatibility_version": "5.0.0"
    },
    "tagline": "You Know, for Search"
}
```
### Проверка здоровья кластера
Elasticsearch предоставляет различные API для оперативного управления кластерами и узлами. Например мы можем проверить работоспособность кластера следующим запросом: `http://localhost:9200/_cluster/health?pretty`
```json
{
    "cluster_name": "elasticsearch",
    "status": "green",
    "timed_out": false,
    "number_of_nodes": 1,
    "number_of_data_nodes": 1,
    "active_primary_shards": 0,
    "active_shards": 0,
    "relocating_shards": 0,
    "initializing_shards": 0,
    "unassigned_shards": 0,
    "delayed_unassigned_shards": 0,
    "number_of_pending_tasks": 0,
    "number_of_in_flight_fetch": 0,
    "task_max_waiting_in_queue_millis": 0,
    "active_shards_percent_as_number": 100
}
```
Как видно из ответа статус зеленый (статус кластера может быть зеленым, желтым или красным). Состояние кластера — это, в основном, индикация правильного распределения осколков в кластере.

В следующей таблице описано, что означает каждый статус:

![image](https://user-images.githubusercontent.com/18426280/62626205-85bf0280-b92f-11e9-8dfd-7f0a600bb4a0.png)                                                                                                                                                                                                                                                                                         |
                                                                                                                                                                                                                                                                                                     |
### Основные типы данных
- Text (Если вы хотите выполнить полнотекстовый поиск, вы должны использовать тип text)
- Keyword (Тип keyword должен использоваться, если вы хотите получить точное совпадение)
- Date (Тип данных date используется для представления полей даты в Elasticsearch)
- Numeric (Числовые типы поддерживаемые Elasticsearch)
- Boolean (Булевский тип данных используется для представления логических полей true или false)
- Binary (Бинарный тип данных используется для хранения закодированной в `Base64` строки)
- Array (Используется как и обычный массив из json)
- Object (Поле в документе может быть как просто числом, так и целым объектом)
- Nested (Когда вы используете вложенный тип данных, каждый объект в массиве индексируется как новый  вложенный документ)

####  Разница между Object и Nested
Документы Elasticsearch являются объектами JSON. Поле в документе может быть как просто числом, так и целым объектом. Например, документ пользователя, как показано ниже, содержит имя, которое представляет собой простое текстовое поле и адрес, который является объектом. А адрес также может иметь внутренние объекты. Объект пользователя:
```json
{
   "id": 1,
   "name": "Петр",
   "address": {
     "street": "Ленина 19б",
     "city": "Москва"
   }
 }
```

В отличие от простых типов данных, когда объект сохраняется в инвертированном индексе, он разбивается на пары «ключ-значение». Документ пользователя хранится, как показано ниже:
```json
{
   "id": 1,
   "name": "User1",
   "address.street": "Ленина 19б",
   "address.city": "Москва"
 }
```
Поскольку объект хранится в виде пар ключ-значение, он становится сложным, когда у вас есть массив объектов. Посмотрим, что произойдет, если у пользователя несколько адресов. Например:
```json
{
 "id": 1,
 "name": "User1",
  "address": [
    {
      "street": "Сивкова 12",
      "city": "Васьково"
    },
    {
      "street" : "Русталова 2",
      "city": "Москва"
    }
  ]
}
```
Храниться он будет следующим образом:
```json
{
  "id" : 1,
  "name" : "User1",
  "address.street" : ["Сивкова 12", "Русталова 2"],
  "address.city" : ["Васьково", "Москва"]
}
```
Когда объекты адреса хранятся в инвертированном индексе, связь между частями одного и того же адреса теряется. Например, если вы запрашиваете все документы, содержащие улицу, Сивкова 12 и Москва, глядя на исходный документ, результатов не должно быть. Но учитывая способ хранения документ все же вернется.
Когда у нас есть массив объектов, массив сглаживается, из-за чего отношения между полями объектов ломаются. Чтобы решить эту проблему, Elasticsearch предоставляет вложенный тип данных. Когда вы используете вложенный тип данных, каждый объект в массиве индексируется как новый  вложенный документ. Поскольку объекты обрабатываются внутри как отдельные документы, вам нужно использовать специальный тип запроса для запроса вложенных документов.
```json
{
   "properties": {
     "id": {
       "type": "integer"
     },
     "name": {
       "type": "keyword"
     },
     "address_nested": {
       "type": "nested",
       "properties": {
         "street": {
           "type": "keyword"
         },
         "city": {
           "type": "keyword"
         }
       }
     }
   }
 }
```
### Типы запросов
Запросы Elasticsearch выполняются с помощью **Search API**. Как и все остальное в Elasticsearch, запрос и ответ представлены в виде JSON.
Запросы в Elasticsearch делятся следующим образом:
- Структурированные запросы : структурированные запросы используются для запроса чисел, дат, статусов и т. д. Они похожи на запросы, поддерживаемые базой данных SQL. Например, может ли число или дата попадать в диапазон или найти всех сотрудников с определенным именем и так далее
- Полнотекстовые поисковые запросы . Полнотекстовые поисковые запросы используются для поиска в текстовых полях. Когда вы отправляете полнотекстовый запрос в Elasticsearch, он сначала находит все документы, соответствующие запросу, а затем документы оцениваются на основе того, насколько релевантен каждый документ для запроса.
## Elasticsearch + Django
Для работы с Elasticsearch в Django нужно использовать пакет [django-elasticsearch-dsl](https://github.com/sabricot/django-elasticsearch-dsl).  При его установке так же установятся [elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py) и [elasticsearch-py](https://github.com/elastic/elasticsearch-py) пакеты. **Важно, чтобы версии elasticsearch-py и elasticsearch-dsl-py совпадали с версией Elasticsearch, который вы установили до этого!**

После установки мы должны добавить `django_elasticsearch_dsl` в секцию `INSTALLED_APPS` в settings.py. Так же мы должны добавить секцию `ELASTICSEARCH_DSL`.
```python
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
```

После этого необходимо создать файл `documents.py`, в котором нужно описать надстройку над нашими моделями:

**models.py:**
```python
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Car(models.Model):
    brand = models.CharField(max_length=120)
    color = models.CharField(max_length=120)

    def __str__(self):
        return self.brand


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    posts = models.ManyToManyField(Post)
    car = models.ForeignKey(Car, related_name='authors', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
```

**documents.py:**
```python
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from forum.models import Post


@registry.register_document
class PostDocument(Document):
    title = fields.TextField()
    content = fields.TextField()
    timestamp = fields.DateField()
    category = fields.NestedField(
        properties={
            'name': fields.TextField(),
            'slug': fields.TextField()
        }
    )

    class Index:
        name = 'posts'

    class Django:
        model = Post
```

Чтобы только что созданный document проиндексировался необходимо выполнить команду
```commandline
python manage.py search_index --rebuild
```
Для того, чтобы убедиться, что наши posts были успешно проиндексированы, нужно отправить _GET_ запрос через Search API `http://localhost:9200/_search`
```json
{
    "took": 2,
    "timed_out": false,
    "_shards": {
        "total": 5,
        "successful": 5,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": 9,
        "max_score": 1,
        "hits": [
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "5",
                "_score": 1,
                "_source": {
                    "title": "Iron Age Celtic Woman Wearing Fancy Clothes Buried in This 'Tree Coffin' in Switzerland",
                    "content": "During the late Iron Age ...",
                    "timestamp": "2019-07-31T13:37:37.203637+00:00",
                    "category": {
                        "name": "business",
                        "slug": "business"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "8",
                "_score": 1,
                "_source": {
                    "title": "Shin Ok-ju: S Korean doomsday cult leader jailed for six years",
                    "content": "The leader of a South Korean ...",
                    "timestamp": "2019-07-31T13:37:37.205086+00:00",
                    "category": {
                        "name": "news",
                        "slug": "news"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "9",
                "_score": 1,
                "_source": {
                    "title": "Hong Kong protests: 'I'm in Australia but I feel censored by Chinese students'",
                    "content": "Hong Kong is now in its ...",
                    "timestamp": "2019-07-31T13:37:37.205602+00:00",
                    "category": {
                        "name": "business",
                        "slug": "business"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "2",
                "_score": 1,
                "_source": {
                    "title": "Democratic debates: Five things to look out for",
                    "content": "It's time for Round Two in ...",
                    "timestamp": "2019-07-31T13:37:37.202019+00:00",
                    "category": {
                        "name": "sport",
                        "slug": "sport"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "4",
                "_score": 1,
                "_source": {
                    "title": "Andy Murray says he is closer than he thought to making singles return",
                    "content": "The former world No 1 ...",
                    "timestamp": "2019-07-31T13:37:37.203169+00:00",
                    "category": {
                        "name": "news",
                        "slug": "news"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "6",
                "_score": 1,
                "_source": {
                    "title": "Divers Find Temples and Treasures in Sunken Ancient Egyptian City",
                    "content": "Divers Find Temples and Treasures ...",
                    "timestamp": "2019-07-31T13:37:37.204103+00:00",
                    "category": {
                        "name": "business",
                        "slug": "business"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "1",
                "_score": 1,
                "_source": {
                    "title": "Princess Haya: Dubai ruler and wife begin London court battle",
                    "content": "The ruler of Dubai ...",
                    "timestamp": "2019-07-31T13:37:37.201303+00:00",
                    "category": {
                        "name": "sport",
                        "slug": "sport"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "7",
                "_score": 1,
                "_source": {
                    "title": "Democratic debates: Who won and lost in round one?",
                    "content": "The Democrats competing ...",
                    "timestamp": "2019-07-31T13:37:37.204588+00:00",
                    "category": {
                        "name": "sport",
                        "slug": "sport"
                    }
                }
            },
            {
                "_index": "posts",
                "_type": "doc",
                "_id": "3",
                "_score": 1,
                "_source": {
                    "title": "Premier League 2019‑20 preview No 4: Brighton",
                    "content": "Guardian writers predicted ...",
                    "timestamp": "2019-07-31T13:37:37.202635+00:00",
                    "category": {
                        "name": "news",
                        "slug": "news"
                    }
                }
            }
        ]
    }
}
```
Для того, чтобы удалить все данные о всех индексах из elasticsearch API, нужно отправить _DELETE_ запрос через Search API `http://localhost:9200/_all`
```json
{
    "acknowledged": true
}
```

Создадим два разных `view`, чтобы проверить работу приложения. Одно представление для работы с данными через DjangoORM и другое для работы через elasticsearch API:

**views.py**
```python
from django.db.models import Q as django_Q
from django.shortcuts import render
from django.views import View
from elasticsearch_dsl import Q as elastic_Q

from forum.documents import PostDocument
from forum.models import Post
from forum.utils import timeit

TEMPLATE_NAME = 'search.html'


class ElasticSearchView(View):
    @timeit(search_name='elastic')
    def get(self, request):
        query = request.GET.get('q')

        search_result = PostDocument.search().query(elastic_Q('fuzzy', content=query) |
                                                    elastic_Q('fuzzy', title=query) |
                                                    elastic_Q('nested',
                                                              path='category',
                                                              query=elastic_Q('fuzzy', category__name=query) |
                                                                    elastic_Q('fuzzy', category__slug=query)))
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})


class SimpleSearchView(View):
    @timeit(search_name='simple')
    def get(self, request):
        query = request.GET.get('q')

        search_result = Post.objects.all().filter(django_Q(content__contains=query) |
                                                  django_Q(title__contains=query) |
                                                  django_Q(category__name__contains=query) |
                                                  django_Q(category__slug__contains=query))
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})
```

Поисковое API для текста в Django ORM по умолчанию имеет два режима: на полное совпадение и на включение (`contains`). Elasticsearch API предоставляет намного больше возможностей для [поиска](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

**Demo:**

![Aug-07-2019 16-12-01 gif sb-d29131d9-wPY4jf](https://user-images.githubusercontent.com/18426280/62625605-3926f780-b92e-11e9-8303-6b91115b006e.gif)


## Это интересно
Как я говорил выше, из коробки Django поддерживает лишь стандартные операции с поиском по тексту:
```python
>>> Author.objects.filter(name__contains='Terry')
[<Author: Terry Gilliam>, <Author: Terry Jones>]
```
-----------------------------------
```python
>>> Author.objects.filter(name__icontains='Terry')
[<Author: Terry Gilliam>, <Author: Terry Jones>, <Author: terry brooks>]
```

Но, например, база `PostgreSQL` имеет много специфических [полей поиска](https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/lookups/), а также свой движок для [полнотекстового поиска](https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/search/).

Хорошая [статья](https://medium.com/@pauloxnet/full-text-search-in-django-with-postgresql-4e3584dee4ae) для примера.
