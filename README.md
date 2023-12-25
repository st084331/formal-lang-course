[![Check code style](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/actions/workflows/code_style.yml/badge.svg)](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/actions/workflows/code_style.yml)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
---
# Formal Language Course

Курс по формальным языкам: шаблон структуры репозитория для выполнения домашних работ,
а также материалы курса и другая сопутствующая информация.

Актуальное:
- [Таблица с текущими результатами](https://docs.google.com/spreadsheets/d/1-vx82auNr0PQDQ3SwA7IYewZyOC9iHIaoX1w1qRUZ3I/edit?usp=sharing)
- [Список задач](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/tree/main/tasks)
- [Стиль кода как референс](https://www.python.org/dev/peps/pep-0008/)
- [Материалы по курсу](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/blob/main/docs/lecture_notes/Formal_language_course.pdf)
- [О достижимости с ограничениями в терминах формальных языков](https://github.com/FormalLanguageConstrainedPathQuerying/FormalLanguageConstrainedReachability-LectureNotes)
- Классика по алгоритмам синтаксического анализа: [Dick Grune, Ceriel J. H. Jacobs, "Parsing Techniques A Practical Guide"](https://link.springer.com/book/10.1007/978-0-387-68954-8#bibliographic-information)
- Классика по теории формальных языков: [M. A. Harrison. 1978. "Introduction to Formal Language Theory"](https://dl.acm.org/doi/book/10.5555/578595)
- Свежее по теории автоматов и их применению в различных областях: [Editors: Jean-Éric Pin. 2021. "Handbook of Automata Theory"](https://ems.press/books/standalone/172)

Технологии:
- Python 3.8+
- Pytest для unit тестирования
- GitHub Actions для CI
- Google Colab для постановки и оформления экспериментов
- Сторонние пакеты из `requirements.txt` файла
- Английский язык для документации или самодокументирующийся код

## Работа с проектом

- Для выполнения домашних практических работ необходимо сделать `fork` этого репозитория к себе в `GitHub`.
- Рекомендуется установить [`pre-commit`](https://pre-commit.com/#install) для поддержания проекта в адекватном состоянии.
  - Установить `pre-commit` можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit install
    ```
  - Отформатировать код в соответствии с принятым стилем можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit run --all-files
    ```
- Ссылка на свой `fork` репозитория размещается в [таблице](https://docs.google.com/spreadsheets/d/1-vx82auNr0PQDQ3SwA7IYewZyOC9iHIaoX1w1qRUZ3I/edit?usp=sharing) курса с результатами.
- В свой репозиторий необходимо добавить проверяющих с `admin` правами на чтение, редактирование и проверку `pull-request`'ов.

## Домашние практические работы

### Дедлайны

- **мягкий**: TODO 23:59
- **жёсткий**: TODO 23:59

### Выполнение домашнего задания

- Каждое домашнее задание выполняется в отдельной ветке. Ветка должна иметь осмысленное консистентное название.
- При выполнении домашнего задания в новой ветке необходимо открыть соответствующий `pull-request` в `main` вашего `fork`.
- `Pull-request` снабдить понятным названием и описанием с соответствующими пунктами прогресса.
- Проверка заданий осуществляется посредством `review` вашего `pull-request`.
- Как только вы считаете, что задание выполнено, вы можете запросить `review` у проверяющего.
  - Если `review` запрошено **до мягкого дедлайна**, то вам гарантированна дополнительная проверка (до жёсткого дедлайна), позволяющая исправить замечания до наступления жёсткого дедлайна.
  - Если `review` запрошено **после мягкого дедлайна**, но **до жесткого дедлайна**, задание будет проверено, но нет гарантий, что вы успеете его исправить.
- Когда проверка будет пройдена, и задание **зачтено**, его необходимо `merge` в `main` вашего `fork`.
- Результаты выполненных заданий будут повторно использоваться в последующих домашних работах.

### Опциональные домашние задания
Часть задач, связанных с работой с GPGPU, будет помечена как опциональная. Это означает что и без их выполнения (при идеальном выполнении остальных задач) можно набрать полный балл за курс.

### Получение оценки за домашнюю работу

- Если ваша работа **зачтена** _до_ **жёсткого дедлайна**, то вы получаете **полный балл за домашнюю работу**.
- Если ваша работа **зачтена** _после_ **жёсткого дедлайна**, то вы получаете **половину полного балла за домашнюю работу**.
  - Если ревью было запрошено _до_ **жёсткого дедлайна** и задача зачтена сразу без замечаний, то вы всё ещё получаете **полный балл за домашнюю работу**.

## Код

- Исходный код практических задач по программированию размещайте в папке `project`.
- Файлам и модулям даем осмысленные имена, в соответствии с официально принятым стилем.
- Структурируем код, используем как классы, так и отдельно оформленные функции. Чем понятнее код, тем быстрее его проверять и тем больше у вас будет шансов получить полный балл.

## Тесты

- Тесты для домашних заданий размещайте в папке `tests`.
- Формат именования файлов с тестами `test_[какой модуль\класс\функцию тестирует].py`.
- Для работы с тестами рекомендуется использовать [`pytest`](https://docs.pytest.org/en/6.2.x/).
- Для запуска тестов необходимо из корня проекта выполнить следующую команду:
  ```shell
  python ./scripts/run_tests.py
  ```

## Эксперименты

- Для выполнения экспериментов потребуется не только код, но окружение и некоторая его настройка.
- Эксперименты должны быть воспроизводимыми (например, проверяющими).
- Эксперимент (настройка, замеры, результаты, анализ результатов) оформляется как Python-ноутбук, который публикуется на GitHub.
  - В качестве окружения для экспериментов с GPGPU (опциональные задачи) можно использовать [`Google Colab`](https://research.google.com/colaboratory/) ноутбуки. Для его создания требуется только учетная запись `Google`.
  - В `Google Colab` ноутбуке выполняется вся настройка, пишется код для экспериментов, подготовки отчетов и графиков.

## Структура репозитория

```text
.
├── .github - файлы для настройки CI и проверок
├── docs - текстовые документы и материалы по курсу
├── project - исходный код домашних работ
├── scripts - вспомогательные скрипты для автоматизации разработки
├── tasks - файлы с описанием домашних заданий
├── tests - директория для unit-тестов домашних работ
├── README.md - основная информация о проекте
└── requirements.txt - зависимости для настройки репозитория
```

## Контакты

- Семен Григорьев [@gsvgit](https://github.com/gsvgit)
- Егор Орачев [@EgorOrachyov](https://github.com/EgorOrachyov)
- Вадим Абзалов [@vdshk](https://github.com/vdshk)
- Рустам Азимов [@rustam-azimov](https://github.com/rustam-azimov)
- Екатерина Шеметова [@katyacyfra](https://github.com/katyacyfra)

## Graph Query Language

```
program = List<statement>
statement =
    assign of variable * expression
  | display of expression
value =
    Text of string
  | Number of int
  | Boolean of bool
  | Network of graph
  | Tags of labels
  | Nodes of vertices
  | Links of edges
expression =
    Variable of variable              // variables
  | Constant of value                // constants
  | Initiate_start of Set<value> * expression // set initial states
  | Initiate_final of Set<value> * expression // set final states
  | Append_start of Set<value> * expression // add to initial states
  | Append_final of Set<value> * expression // add to final states
  | Acquire_start of expression      // get initial states
  | Acquire_final of expression      // get final states
  | Acquire_reachable of expression  // get all reachable node pairs
  | Acquire_nodes of expression      // get all nodes
  | Acquire_links of expression      // get all edges
  | Acquire_tags of expression       // get all labels
  | Transform of lambda * expression // classic map
  | Refine of lambda * expression    // classic filter
  | Load_graph of expression         // load graph
  | Intersection of expression * expression // intersect languages
  | Linkage of expression * expression       // concatenate languages
  | Merge of expression * expression         // unite languages
  | Closure of expression                    // language closure (Kleene star)
  | Transition of expression                 // single transition
  | Membership of expression * expression    // element membership in set
  | Collection of List<expression>           // set of elements
lambda =
    lambda = variable * expression
```
### Specific Syntax
```
program --> (instruction ENDLINE)*
instruction -->
    variable ASSIGN expression SEMICOLON
  | 'display' expression SEMICOLON
variable --> initial_char var_sequence
initial_char --> LETTER | '_'
var_sequence --> (initial_char | DIGIT)*
expression -->
    LEFT_BRACKET expression RIGHT_BRACKET
  | variable
  | value
  | map
  | filter
  | intersection
  | linkage
  | merge
  | closure
  | membership
lambda --> LEFT_BRACE 'function' variable '->' expression RIGHT_BRACE
map --> 'map' LEFT_BRACKET lambda COMMA expression RIGHT_BRACKET
filter --> 'filter' LEFT_BRACKET lambda COMMA expression RIGHT_BRACKET
intersection --> 'intersection' LEFT_BRACKET expression COMMA expression RIGHT_BRACKET
linkage --> 'linkage' LEFT_BRACKET expression COMMA expression RIGHT_BRACKET
merge --> 'merge' LEFT_BRACKET expression COMMA expression RIGHT_BRACKET
closure --> LEFT_BRACKET expression RIGHT_BRACKET '*'
membership --> expression 'belongs_to' collection
value -->
    LEFT_BRACKET value RIGHT_BRACKET
  | QUOTE string QUOTE
  | NUMBER
  | BOOLEAN
  | network
  | tags
  | nodes
  | links
string --> (LETTER | NUMBER | '.' | '?' | '*')*
network -->
    'initiate_start' LEFT_BRACKET nodes COMMA network RIGHT_BRACKET
  | 'initiate_final' LEFT_BRACKET nodes COMMA network RIGHT_BRACKET
  | 'append_start' LEFT_BRACKET nodes COMMA network RIGHT_BRACKET
  | 'append_final' LEFT_BRACKET nodes COMMA network RIGHT_BRACKET
  | 'load_network' LEFT_BRACKET path RIGHT_BRACKET
  | variable
path --> QUOTE string QUOTE | variable
nodes -->
    'acquire_start' LEFT_BRACKET network RIGHT_BRACKET
  | 'acquire_final' LEFT_BRACKET network RIGHT_BRACKET
  | 'acquire_reachable' LEFT_BRACKET network RIGHT_BRACKET
  | 'acquire_nodes' LEFT_BRACKET network RIGHT_BRACKET
  | collection
  | variable
tags --> 'acquire_tags' LEFT_BRACKET network RIGHT_BRACKET | collection
links --> 'acquire_links' LEFT_BRACKET network RIGHT_BRACKET | collection
collection --> LEFT_BRACE expression (COMMA expression)* RIGHT_BRACE
  | 'empty_set()'
  | LEFT_BRACE ( LEFT_BRACKET NUMBER COMMA (value | variable) COMMA NUMBER RIGHT_BRACKET )* RIGHT_BRACE
ASSIGN ---> '='
BOOLEAN --> 'true' | 'false'
LETTER --> [a-z] | [A-Z]
COMMA --> ','
DIGIT --> [0-9]
ENDLINE --> [\n]
NUMBER --> '0' | '-'? [1-9][0-9]*
LEFT_BRACE --> '{'
LEFT_BRACKET --> '('
QUOTE --> '"'
RIGHT_BRACE --> '}'
RIGHT_BRACKET --> ')'
SEMICOLON --> ';'
```
## Examples
### Finding Reachable Nodes
```
network = load_network("network/path"); // Load a graph from a specified path
start_nodes = collection(1, 5); // Define a set of start nodes
network = initiate_start(start_nodes, network); // Set defined nodes as initial in the graph
reachable_nodes = acquire_reachable(network); // Get all nodes reachable from the start nodes
display reachable_nodes; // Display the reachable nodes
```

### Filtering Edges Based on a Condition
```
network = load_network("edges/path"); // Load graph from a path
edges = acquire_links(network); // Retrieve all edges from the graph
filtered_edges = refine({function edge -> edge belongs_to collection((1, "A", 2), (3, "B", 4))}, edges); // Filter edges based on a condition
display filtered_edges; // Display the filtered edges
```

### Modifying Graph Labels
```
network = load_network("label/path"); // Load graph from a path
labels = acquire_tags(network); // Retrieve all labels from the graph
updated_labels = transform({function label -> if label == "Old" then "New" else label}, labels); // Modify labels based on a condition
display updated_labels; // Display the updated labels
```
### Union of Two Graphs
```
graph1 = load_network("path/one"); // Load first graph
graph2 = load_network("path/two"); // Load second graph
union_graph = merge(graph1, graph2); // Perform union of two graphs
display union_graph; // Display the union graph
```

### Creating a Star Closure of a Regular Expression
```
regular_expression = "abc"; // Define a regular expression
star_closure = closure(regular_expression); // Create star closure of the regular expression
display star_closure; // Display the star closure result
```

### Set Operations on Graph Nodes
```
network = load_network("node/path"); // Load graph from a path
nodes_set1 = acquire_nodes(network); // Acquire nodes from the graph
nodes_set2 = collection(2, 4, 6); // Define another set of nodes
intersection_nodes = intersection(nodes_set1, nodes_set2); // Find intersection of two node sets
union_nodes = merge(nodes_set1, nodes_set2); // Find union of two node sets
difference_nodes = refine({function node -> node not belongs_to nodes_set2}, nodes_set1); // Find difference between two node sets
display intersection_nodes; // Display intersection nodes
display union_nodes; // Display union nodes
display difference_nodes; // Display difference nodes
```
