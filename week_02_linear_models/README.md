# Неделя 2 — Линейные модели

Материалы скачаны из [DeepLearningSchool/part_1_ml_cv](https://github.com/DeepLearningSchool/part_1_ml_cv), ветка **autumn26**.

## Что где лежит

```
week_02_linear_models/
├── Lecture/
│   └── Линейные модели.pdf
├── Practice/                            семинары, запускаются как есть
│   ├── part_1_linear_regression.ipynb       ✓ работает целиком
│   ├── part_2_regularization.ipynb          есть 3 ячейки с # YOUR CODE
│   └── part_3_logistic_regression.ipynb     ✓ работает целиком
└── Homework/
    ├── hw_2_linear_models.ipynb         6 ячеек с # YOUR CODE
    └── train.csv                        73 МБ, в git не попадает
```

## Данные

`train.csv` — это **MNIST**: 42 000 рукописных цифр, 785 колонок (`label` + 784 пикселя изображения 28×28).

Домашка читает его как `./train.csv`, то есть файл должен лежать **рядом с ноутбуком**. Так и лежит.

В репозиторий файл не попадает — он подпадает под `*.csv` в `.gitignore`. Если потеряется, скачать заново:

```bash
curl -L -o Homework/train.csv \
  https://raw.githubusercontent.com/DeepLearningSchool/part_1_ml_cv/autumn26/week_02_linear_models/Homework/train.csv
```

## Про ветки репозитория курса

Веток две: `main` и `autumn26`. Я сравнил все файлы недели 2 по хешам:

| файл | main | autumn26 |
|---|---|---|
| семинары (3 шт) | одинаковые | одинаковые |
| лекция PDF | одинаковая | одинаковая |
| train.csv | одинаковый | одинаковый |
| **домашка** | 52 ячейки | **53 ячейки** |

Отличается только домашка: в `autumn26` добавлена ячейка с проверкой `MyLogisticRegression`. Взята версия из **autumn26** как более новая.

Видео лежат не в репозитории, а ссылками в README — ниже они собраны.

---

# Видеозаписи

## Лекции (Григорий Лелейтнер)

| тема | YouTube | VK |
|---|---|---|
| Линейная регрессия | [смотреть](https://youtu.be/khdaLtu9i-s) | [смотреть](https://vkvideo.ru/video-155161349_456239169) |
| LogLoss | [смотреть](https://youtu.be/HV4Bm8UJwIs) | [смотреть](https://vkvideo.ru/video-155161349_456239170) |
| Логистическая регрессия | [смотреть](https://youtu.be/FssgYm7FYM8) | [смотреть](https://vkvideo.ru/video-155161349_456239171) |
| Градиентный спуск в линейных алгоритмах | [смотреть](https://youtu.be/YWr3S1IqnlQ) | [смотреть](https://vkvideo.ru/video-155161349_456239172) |
| Регуляризация | [смотреть](https://youtu.be/7lKwdPwqVHc) | [смотреть](https://vkvideo.ru/video-155161349_456239173) |
| Нормализация | [смотреть](https://youtu.be/tOiwAyilk3I) | [смотреть](https://vkvideo.ru/video-155161349_456239174) |

## Семинары (Юрий Яровиков)

| тема | YouTube | VK |
|---|---|---|
| Линейная регрессия | [смотреть](https://youtu.be/GNbDq0570gw) | [смотреть](https://vkvideo.ru/video-155161349_456239175) |
| Регуляризация в линейной регрессии | [смотреть](https://youtu.be/xzkfLfb5OMQ) | [смотреть](https://vkvideo.ru/video-155161349_456239176) |
| Логистическая регрессия | [смотреть](https://youtu.be/aGtbbiPCHdE) | [смотреть](https://vkvideo.ru/video-155161349_456239177) |

### Осторожно: в README курса две ссылки битые

В оригинальном README авторы ошиблись в разметке. У семинаров «Регуляризация» и «Логистическая регрессия» правильные YouTube-ссылки попали в атрибут `<img src=...>` вместо `href`, а в `href` стоит ссылка на **первый** семинар.

То есть если кликать прямо в README курса, все три семинара откроют одно и то же видео. В таблице выше ссылки уже исправлены.

Плюс у VK-ссылки на третий семинар в начале лишняя русская буква «ё» — она тоже убрана.

---

# Открыть в Colab

```
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Homework/hw_2_linear_models.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_1_linear_regression.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_2_regularization.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_3_logistic_regression.ipynb
```

Значки «Open In Colab» в README курса ведут на ветку `main`, то есть на **старую** версию домашки. Ссылки выше — на `autumn26`.

---

# Проверка среды

Все нужные библиотеки установлены: `numpy`, `pandas`, `matplotlib`, `scipy`, `sklearn`, `plotly`, `mpl_toolkits`.

Прогон ноутбуков:

```
part_1_linear_regression    21 ячейка, 0 ошибок
part_3_logistic_regression  10 ячеек,  0 ошибок
part_2_regularization       есть 3 ячейки с # YOUR CODE
hw_2_linear_models          есть 6 ячеек с # YOUR CODE
```

Ошибок окружения нет — всё, что падает, падает на местах, которые нужно заполнить самому.

## Что предстоит написать в домашке

```
[10]  return # YOUR CODE
[12]  curr_r -= # YOUR CODE. Не забудьте про lr!
[24]  for batch_start in <YOUR CODE>:
```

Темы: градиентный спуск руками, мини-батчи, своя реализация логистической регрессии.

## Связь с конспектом по математике

Вся неделя 2 — ровно про то, что разобрано в [ml_math](../../ml_math/README.md): градиентный спуск, линейная и логистическая регрессия, log loss, регуляризация.

Если домашка буксует, стоит пройти там главы 6–8.
