# Неделя 2 — Линейные модели

Материалы из [DeepLearningSchool/part_1_ml_cv](https://github.com/DeepLearningSchool/part_1_ml_cv), ветка **autumn26**.

---

# ПОРЯДОК ПРОХОЖДЕНИЯ

Шесть шагов. Каждый опирается на предыдущий — не прыгай вперёд.

## Шаг 1 — Линейная регрессия: теория

| | |
|---|---|
| **смотреть** | лекция [Линейная регрессия](https://youtu.be/khdaLtu9i-s) · [VK](https://vkvideo.ru/video-155161349_456239169) |
| **и** | лекция [Градиентный спуск в линейных алгоритмах](https://youtu.be/YWr3S1IqnlQ) · [VK](https://vkvideo.ru/video-155161349_456239172) |
| **время** | ~1 час |

Обе темы разобраны в конспекте [ml_math](../../ml_math/README.md), главы 3, 6 и 7. Если конспект уже прочитан — лекции можно смотреть на полуторной скорости, это повторение.

## Шаг 2 — Линейная регрессия: практика

| | |
|---|---|
| **смотреть** | семинар [Линейная регрессия](https://youtu.be/GNbDq0570gw) · [VK](https://vkvideo.ru/video-155161349_456239175) |
| **решать** | [Practice/part_1_linear_regression.ipynb](Practice/part_1_linear_regression.ipynb) |
| **время** | ~2 часа |

В ноутбуке три класса, написанные целиком:

```
[6]   MyLinearRegression            аналитическое решение (XᵀX)⁻¹Xᵀy
[23]  MyGradientLinearRegression    полный градиентный спуск
[32]  MySGDLinearRegression         стохастический спуск
```

**Не читай их сразу.** Сначала попробуй написать сам — хотя бы первые два. Потом открой и сравни. Расхождения и есть то, чего ты не понял.

## Шаг 3 — Регуляризация

| | |
|---|---|
| **смотреть** | лекция [Регуляризация](https://youtu.be/7lKwdPwqVHc) · [VK](https://vkvideo.ru/video-155161349_456239173) |
| **и** | лекция [Нормализация](https://youtu.be/tOiwAyilk3I) · [VK](https://vkvideo.ru/video-155161349_456239174) |
| **потом** | семинар [Регуляризация в линейной регрессии](https://youtu.be/xzkfLfb5OMQ) · [VK](https://vkvideo.ru/video-155161349_456239176) |
| **решать** | [Practice/part_2_regularization.ipynb](Practice/part_2_regularization.ipynb) |
| **время** | ~2.5 часа |

Эти две лекции — **новый материал**, в конспекте `ml_math` регуляризация упомянута вскользь. Пропускать не стоит.

В ноутбуке три места с `# YOUR CODE`:

```
[6]   signs = …            мягкий знак весов для Lasso
[21]  X_train_scaled = …   обучить и применить scaler
[22]  …                    проверить, что масштабирование сработало
```

Плюс в конце готовый `MyRidgeRegression` для самостоятельного разбора.

## Шаг 4 — Логистическая регрессия

| | |
|---|---|
| **смотреть** | лекция [LogLoss](https://youtu.be/HV4Bm8UJwIs) · [VK](https://vkvideo.ru/video-155161349_456239170) |
| **и** | лекция [Логистическая регрессия](https://youtu.be/FssgYm7FYM8) · [VK](https://vkvideo.ru/video-155161349_456239171) |
| **потом** | семинар [Логистическая регрессия](https://youtu.be/aGtbbiPCHdE) · [VK](https://vkvideo.ru/video-155161349_456239177) |
| **решать** | [Practice/part_3_logistic_regression.ipynb](Practice/part_3_logistic_regression.ipynb) |
| **время** | ~2 часа |

Короткий ноутбук, 18 ячеек. Внутри готовый `MyLogisticRegression` — тот же приём: сначала напиши сам, потом сверь.

## Шаг 5 — Домашнее задание

| | |
|---|---|
| **решать** | [Homework/hw_2_linear_models.ipynb](Homework/hw_2_linear_models.ipynb) |
| **время** | ~4 часа |

Четыре задания, все про написание кода:

```
Задание 1  [10] [12]   градиентный спуск
Задание 2  [24]        генератор мини-батчей
Задание 3  [31]        логистическая регрессия
Задание 4  [37] [51]   elastic net: L1 + L2 вместе
```

После каждого задания в ноутбуке идёт тестовая ячейка — она проверит твой код. Не переходи к следующему, пока тест не прошёл.

Данные — MNIST, 42 000 рукописных цифр.

## Шаг 6 — Сдача

Как на первой неделе: прикрепить `.ipynb`, отправить на рецензию, написать рецензии другим.

---

# Если застрял

1. **Перечитай нужную главу** [ml_math](../../ml_math/README.md) — там те же формулы на четырёх точках
2. **Пересмотри кусок лекции** — обычно непонимание в одном конкретном месте
3. **Спроси меня** — но лучше конкретно: «не понимаю, почему в этой строке делим на n», а не «объясни всё»

---

# Что где лежит

```
week_02_linear_models/
├── Lecture/
│   └── Линейные модели.pdf          48 страниц, справочник по формулам
├── Practice/
│   ├── part_1_linear_regression.ipynb       41 ячейка, 3 готовых класса
│   ├── part_2_regularization.ipynb          42 ячейки, 3 пропуска
│   └── part_3_logistic_regression.ipynb     18 ячеек, 1 готовый класс
├── Homework/
│   ├── hw_2_linear_models.ipynb     53 ячейки, 4 задания
│   └── train.csv                    73 МБ, в git не попадает
└── README.md
```

PDF открывается прямо в VSCode — установлено расширение `tomoki1207.pdf`.

---

# Все видео одним списком

## Лекции (Григорий Лелейтнер)

| тема | YouTube | VK | нужна? |
|---|---|---|---|
| Линейная регрессия | [→](https://youtu.be/khdaLtu9i-s) | [→](https://vkvideo.ru/video-155161349_456239169) | повторение |
| LogLoss | [→](https://youtu.be/HV4Bm8UJwIs) | [→](https://vkvideo.ru/video-155161349_456239170) | да |
| Логистическая регрессия | [→](https://youtu.be/FssgYm7FYM8) | [→](https://vkvideo.ru/video-155161349_456239171) | да |
| Градиентный спуск | [→](https://youtu.be/YWr3S1IqnlQ) | [→](https://vkvideo.ru/video-155161349_456239172) | повторение |
| **Регуляризация** | [→](https://youtu.be/7lKwdPwqVHc) | [→](https://vkvideo.ru/video-155161349_456239173) | **обязательно** |
| **Нормализация** | [→](https://youtu.be/tOiwAyilk3I) | [→](https://vkvideo.ru/video-155161349_456239174) | **обязательно** |

Колонка «нужна» — с учётом того, что уже разобрано в конспекте `ml_math`.

## Семинары (Юрий Яровиков)

| тема | YouTube | VK |
|---|---|---|
| Линейная регрессия | [→](https://youtu.be/GNbDq0570gw) | [→](https://vkvideo.ru/video-155161349_456239175) |
| Регуляризация в линейной регрессии | [→](https://youtu.be/xzkfLfb5OMQ) | [→](https://vkvideo.ru/video-155161349_456239176) |
| Логистическая регрессия | [→](https://youtu.be/aGtbbiPCHdE) | [→](https://vkvideo.ru/video-155161349_456239177) |

### В README курса две ссылки битые

У семинаров «Регуляризация» и «Логистическая регрессия» авторы перепутали атрибуты в HTML: правильные ссылки попали в `<img src=...>`, а в `href` стоит первый семинар. Если кликать там — все три откроют одно видео.

В таблице выше ссылки исправлены, все девять проверены.

---

# Технические заметки

## Данные

`train.csv` — MNIST: 42 000 строк, 785 колонок (`label` + 784 пикселя 28×28).

Домашка читает `./train.csv` рядом с собой. В git файл не попадает (`*.csv` в `.gitignore`). Если пропал:

```bash
curl -L -o Homework/train.csv \
  https://raw.githubusercontent.com/DeepLearningSchool/part_1_ml_cv/autumn26/week_02_linear_models/Homework/train.csv
```

## Про ветки курса

`main` и `autumn26`. Сравнил все файлы недели по хешам: отличается **только домашка** — в `autumn26` на одну ячейку больше (проверка `MyLogisticRegression`). Взята версия из `autumn26`.

Значки «Open In Colab» в README курса ведут на `main`, то есть на старую домашку.

## Открыть в Colab

```
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Homework/hw_2_linear_models.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_1_linear_regression.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_2_regularization.ipynb
https://colab.research.google.com/github/DeepLearningSchool/part_1_ml_cv/blob/autumn26/week_02_linear_models/Practice/part_3_logistic_regression.ipynb
```

## Среда

Все библиотеки стоят: `numpy`, `pandas`, `matplotlib`, `scipy`, `sklearn`, `plotly`, `mpl_toolkits`.

Прогон ноутбуков:

```
part_1_linear_regression    21 ячейка, 0 ошибок
part_3_logistic_regression  10 ячеек,  0 ошибок
part_2_regularization       падает только на # YOUR CODE
hw_2_linear_models          падает только на # YOUR CODE
```

Ошибок окружения нет. Колабовских зависимостей (`gdown`, `/content`, монтирование Drive) в этой неделе нет вообще.
