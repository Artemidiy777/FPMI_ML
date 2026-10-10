# Шпаргалка — неделя 1 (pandas, matplotlib, seaborn, sklearn)

Всё, что встречается в `seminar_1_fpmi.ipynb` и `Homework/hw_1_game_of_thrones.ipynb`.

---

## Библиотеки: кто за что отвечает

| Библиотека | Импорт | Зона ответственности |
|---|---|---|
| **pandas** | `import pandas as pd` | таблицы: чтение файлов, колонки, пропуски, группировки |
| **NumPy** | `import numpy as np` | числа и массивы: математика, статистика |
| **matplotlib** | `import matplotlib.pyplot as plt` | графики, полный контроль над деталями |
| **seaborn** | `import seaborn as sns` | графики покрасивее и статистические, поверх matplotlib |
| **scikit-learn** | `from sklearn... import ...` | машинное обучение: кодировщики, масштабирование, модели, метрики |
| **gdown** | `import gdown` | скачивание файлов с Google Drive по ID |

Главное правило различения: `np.функция(данные)` — NumPy, а `данные.метод()` через точку — почти всегда pandas.

---

## pandas

### Загрузка и сохранение

| Код | Что делает |
|---|---|
| `pd.read_csv(path)` | прочитать CSV в DataFrame |
| `pd.read_csv(path, index_col='S.No')` | сделать колонку `S.No` индексом строк |
| `df.to_csv(path, index=False)` | сохранить в CSV; `index=False` — не писать индекс отдельной колонкой |

### Первый осмотр

| Код | Что делает |
|---|---|
| `df.head(n)` | первые n строк (по умолчанию 5) |
| `df.tail(n)` | последние n строк |
| `df.sample(n)` | n случайных строк |
| `df.shape` | кортеж (строк, колонок) — **без скобок**, это атрибут |
| `df.columns` | имена колонок |
| `df.index` | имена/номера строк |
| `df.dtypes` | тип каждой колонки |
| `df.info()` | всё сразу: типы, количество непустых, память |
| `df.describe()` | 8 статистик по числовым колонкам: count, mean, std, min, 25%, 50%, 75%, max |
| `df.describe(include=['int64','float64'])` | только по числовым типам |
| `df.T` | транспонировать — строки и колонки меняются местами |

### Выбор данных

| Код | Что делает |
|---|---|
| `df['col']` | одна колонка → Series |
| `df[['a','b']]` | несколько колонок → DataFrame (двойные скобки!) |
| `df.col` | то же, что `df['col']`, но не работает с пробелами и точками в имени |
| `df.loc[условие]` | строки по условию |
| `df.loc[строка, колонка]` | обращение по **именам** |
| `df['Age'][df['Survived'] == 1]` | значения одной колонки при условии на другую |

### Пропуски (NaN)

| Код | Что делает |
|---|---|
| `df.isna()` | таблица True/False: где пропуск |
| `df.notna()` | наоборот |
| `df.isna().sum()` | **сколько пропусков в каждой колонке** — главный приём |
| `df['col'].fillna(0)` | заменить пропуски на значение |
| `df.fillna({'age': 0}, inplace=True)` | заполнить конкретную колонку на месте |
| `df.dropna()` | удалить **строки**, где есть хоть один NaN |
| `df.dropna(axis=1)` | удалить **колонки** с пропусками |
| `df.dropna(subset=['Age'])` | смотреть только на колонку `Age` |
| `df.dropna(how='all')` | удалить только полностью пустые строки |

**NaN нельзя искать через `==`.** `NaN != NaN` по стандарту IEEE 754, поэтому `df.Cabin == 'NaN'` и `df.Cabin == np.nan` вернут пусто. Только `.isna()`.

### Изменение и создание колонок

| Код | Что делает |
|---|---|
| `df['новая'] = ...` | создать колонку (или перезаписать, если есть) |
| `df['x'] = df['y'] > 0` | колонка из True/False по условию |
| `(df['y'] > 0).astype(int)` | превратить True/False в 1/0 |
| `df['col'].replace(['a','b'], 'c')` | заменить значения |
| `df['col'].map(словарь)` | подменить каждое значение по словарю (ищет **по ключу**) |
| `df.assign(имя=значения)` | добавить колонку, возвращая новую таблицу — удобно в цепочке |
| `df.drop(['a','b'], axis=1)` | удалить колонки |
| `df.drop(columns=['a'])` | то же самое, читается понятнее |
| `pd.concat([df1, df2], axis=1)` | склеить вбок (по колонкам); `axis=0` — вниз |

### Подсчёты и уникальные значения

| Код | Что делает |
|---|---|
| `df['col'].value_counts()` | какие значения и сколько раз каждое |
| `df['col'].value_counts(dropna=False)` | **то же, но считая NaN** |
| `df['col'].unique()` | сами уникальные значения (массив), NaN включён |
| `df['col'].nunique()` | сколько их (число), NaN по умолчанию не считается |
| `df.nunique()` | то же по всем колонкам сразу |
| `df['col'].mode()` | самое частое значение |

`unique()` есть только у Series, `nunique()` — и у DataFrame.

### Статистика

| Код | Что делает |
|---|---|
| `s.sum()`, `s.mean()`, `s.median()` | сумма, среднее, медиана |
| `s.min()`, `s.max()` | минимум, максимум |
| `s.quantile(0.5)` | квантиль: доля от 0 до 1; 0.5 = медиана |
| `df.corr(numeric_only=True)` | матрица корреляций между числовыми колонками; без `numeric_only` упадёт, если в таблице есть текст |
| `df.nlargest(n, 'col')` | n строк с наибольшими значениями |
| `df.sort_values('col', ascending=False)` | сортировка по колонке |
| `df.round(2)` | округление |

Методы pandas **пропускают NaN**, функции NumPy — нет. `s.mean()` посчитает, `np.mean(s.values)` вернёт `nan`.

**Фокус с нулями и единицами:** если колонка состоит из 0 и 1, её среднее — это доля единиц. `df['Survived'].mean() = 0.38` значит «выжило 38%».

### Группировка

| Код | Что делает |
|---|---|
| `df.groupby('col')` | разложить строки по кучкам; **сам ничего не считает** |
| `df.groupby('col').size()` | сколько строк в каждой группе |
| `df.groupby('col')['y'].mean()` | среднее `y` внутри каждой группы |
| `df.groupby(['a','b'])['y'].mean()` | группировка по паре колонок |
| `.groupby('col', as_index=False)` | оставить `col` обычной колонкой, а не индексом |
| `.groupby('col', dropna=False)` | не выбрасывать группу с NaN |
| `pd.crosstab(a, b)` | таблица: сколько раз встретилась каждая пара значений |
| `pd.pivot_table(data=df, values='y', index='col', aggfunc=['mean','count'])` | сводная таблица |

Схема «разделить — посчитать — собрать». Прямой аналог `GROUP BY` в SQL.

### Строковые операции

Все через аксессор `.str`:

| Код | Что делает |
|---|---|
| `df['col'].str.lower()` | в нижний регистр |
| `df['col'].str.casefold()` | то же, но агрессивнее (для не-латиницы) |
| `df['col'].str.extract(r'шаблон', expand=False)` | достать по регулярке; `expand=False` → Series, `True` → DataFrame |
| `df['col'].str.contains('текст')` | содержит ли подстроку |

Регулярки пиши с `r` перед строкой: `r' ([A-Za-z]+)\.'` — иначе `SyntaxWarning`.

Разбор этого шаблона: пробел, затем `(...)` группа захвата — то, что вернётся, `[A-Za-z]` одна буква, `+` одна или больше, `\.` точка (экранированная, потому что `.` в регулярках значит «любой символ»).

### Типы и отбор по типу

| Код | Что делает |
|---|---|
| `df.select_dtypes(include=[object])` | только текстовые колонки (pandas 2) |
| `df.select_dtypes(include=['str'])` | то же в pandas 3 |
| `s.astype(int)` | сменить тип |
| `s.values` | превратить Series в numpy-массив: снять имена и индекс |
| `s.tolist()` | превратить в обычный список Python |

---

## NumPy

| Код | Что делает |
|---|---|
| `np.isnan(x)` | это NaN? (в pandas — `pd.isna`) |
| `np.mean(arr)`, `np.median(arr)` | среднее, медиана — **портятся от NaN** |
| `np.nanmean(arr)` | среднее с игнорированием NaN |
| `np.quantile(arr, q=0.5)` | квантиль; `q` — доля от 0 до 1 |
| `np.arange(a, b, step)` | массив чисел с шагом |
| `np.random.randint(a, b, size)` | случайные целые |
| `np.log10(x)` | десятичный логарифм |
| `np.corrcoef(x, y)` | матрица корреляции |
| `np.unique(arr, return_counts=True)` | аналог `value_counts`, но без имён |

Нет и никогда не было: `np.isna`, `np.notna`, `np.value_counts`.
Нет в pandas: `pd.isnan`. Удалено в pandas 3: `pd.value_counts` как функция.

---

## matplotlib

| Код | Что делает |
|---|---|
| `plt.figure(figsize=(10,7))` | новый холст заданного размера в дюймах |
| `plt.subplots(n, m)` | сетка из нескольких графиков, возвращает `(fig, ax)` |
| `plt.show()` | показать и очистить холст |
| `plt.hist(data, bins=50)` | гистограмма; `bins` — число интервалов |
| `plt.bar(x, y)` | вертикальные столбцы |
| `plt.barh(y, width)` | **горизонтальные** столбцы — удобно для длинных подписей |
| `plt.pie(data, autopct='%1.1f%%')` | круговая диаграмма; `autopct` — формат процентов |
| `plt.scatter(x, y)` | точечный график |
| `plt.boxplot(data, showfliers=False)` | ящик с усами; `showfliers` — показывать выбросы |
| `plt.axvline(x=5, color='r', linestyle='--')` | вертикальная линия (например медиана) |
| `plt.title()`, `plt.suptitle()` | заголовок графика / всей фигуры |
| `plt.xlabel()`, `plt.ylabel()` | подписи осей |
| `plt.xticks(rotation=45)` | настройка делений оси |
| `plt.legend(labels, loc, bbox_to_anchor, ncol)` | легенда и её расположение |
| `plt.grid()` | сетка |

Частые параметры: `figsize`, `color`, `alpha` (прозрачность 0–1), `label` (для легенды), `fontsize`, `size`, `bins`.

Через pandas тоже можно, короче: `df['col'].hist(bins=50)`, `s.plot(kind='bar')`, `df.plot()`.

---

## seaborn

| Код | Что делает |
|---|---|
| `sns.heatmap(df.corr(), annot=True, fmt='.2f', square=True)` | тепловая карта; `annot` — писать числа в клетках |
| `sns.histplot(data=df, x='Age', hue='Survived', kde=True)` | гистограмма с разбивкой по категории; `kde` — сглаженная кривая |
| `sns.pairplot(df, diag_kind='hist', height=2)` | все пары признаков на одной сетке |
| `sns.boxplot(data=df, x='a', y='b')` | ящики с усами по категориям |
| `sns.set(font_scale=1.2)` | глобальные настройки оформления |

Параметры heatmap: `vmax` (верх шкалы), `cbar` (шкала сбоку), `annot_kws` (шрифт чисел), `xticklabels`/`yticklabels`.

---

## scikit-learn

### Кодирование категорий в числа

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
arr = encoder.fit_transform(df[cat_cols])
names = encoder.get_feature_names_out(cat_cols)
ohe_df = pd.DataFrame(arr, columns=names, index=df.index)
```

| Код | Что делает |
|---|---|
| `OneHotEncoder(sparse_output=False)` | каждая категория → отдельная колонка 0/1; `False` даёт обычный массив вместо разреженного |
| `.fit(X)` | изучить, какие категории бывают |
| `.transform(X)` | преобразовать, используя уже изученное |
| `.fit_transform(X)` | оба действия сразу |
| `.get_feature_names_out(cols)` | имена новых колонок вида `Sex_male` |
| `pd.get_dummies(df, columns=[...])` | то же one-hot средствами pandas, проще но без запоминания категорий |
| `LabelEncoder()` | каждая категория → номер 0,1,2… |

**Главное правило:** `fit_transform` только на обучающих данных, на тестовых — **только `transform`**. Иначе кодировщик переучится, набор колонок у train и test разойдётся, и модель упадёт.

`LabelEncoder` вводит ложный порядок (0 < 1 < 2) — для линейных моделей брать one-hot. Для деревьев label-кодирование допустимо.

**`index=df.index` обязателен** при сборке DataFrame из массива — иначе последующий `concat` не сопоставит строки и насыпет NaN.

### Масштабирование чисел

| Код | Что делает |
|---|---|
| `StandardScaler()` | приводит к среднему 0 и разбросу 1 |
| `MinMaxScaler()` | сжимает значения в отрезок [0, 1] |

Нужно, когда признаки в разных масштабах (возраст 0–80 и цена билета 0–500).

### Разделение выборки и метрики

| Код | Что делает |
|---|---|
| `train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)` | поделить на обучающую и проверочную части |
| `accuracy_score(y_true, y_pred)` | доля верных предсказаний |

`random_state` фиксирует случайность — без него каждый запуск даёт другое разбиение, и метрики нельзя сравнивать между собой.

---

## Параметры, которые встречаются повсюду

| Параметр | Где | Что значит |
|---|---|---|
| `axis=0` / `axis=1` | `drop`, `concat`, `dropna` | 0 — строки, 1 — колонки |
| `inplace=True` | многие методы | менять на месте вместо возврата копии |
| `dropna` | `value_counts`, `groupby`, `nunique` | учитывать ли NaN |
| `include=[...]` | `describe`, `select_dtypes` | какие типы колонок брать |
| `index_col` | `read_csv` | какую колонку сделать индексом |
| `as_index` | `groupby` | ключ группировки — в индекс или в колонку |
| `ascending` | `sort_values` | по возрастанию или убыванию |
| `bins` | `hist` | число интервалов |
| `figsize` | `figure`, `plot` | размер картинки |
| `random_state` | `train_test_split`, модели | фиксация случайности |

---

## Грабли, на которые легко наступить

1. **Методы возвращают копию.** `fillna`, `replace`, `map`, `dropna`, `astype` ничего не меняют в исходной таблице. Надо присваивать: `df['col'] = df['col'].fillna(0)`. Ошибки при этом нет — код «работает», данные прежние.

2. **`df['col'].fillna(0, inplace=True)` в pandas 3 молча не работает.** Выдаёт предупреждение и ничего не меняет. Либо присваивай, либо `df.fillna({'col': 0}, inplace=True)`.

3. **NaN не ищется через `==`.** Только `.isna()`.

4. **`KeyError` или `NameError` в ноутбуке** почти всегда значит «не запустил ячейку выше», а не «код сломан».

5. **Ноутбук показывает только последнее выражение ячейки.** Если после полезной строки стоит одинокое `df`, увидишь `df`, а первый результат потеряется.

6. **Двойные скобки меняют тип:** `df['a']` → Series, `df[['a']]` → DataFrame из одной колонки.

7. **Разные версии.** Локально pandas 3.0.5, в Colab 2.2.3. Отличается поведение `select_dtypes(include=[object])`, `inplace` на колонке, вывод `dtypes` (`str` против `object`).

8. **Опечатки в похожих именах:** `np.isnan` (не `isna`), `pd.isna` (не `isnan`).

---
---

# 📊 ГРАФИКИ — ПОЛНЫЙ СПРАВОЧНИК

---

## Главное: два разных способа

Почти любой график можно построить двумя путями, и их **нельзя смешивать**.

```python
# ── СПОСОБ 1: pandas — коротко, всё одним вызовом ────────────────
data['popularity'].plot(kind='hist', bins=50, figsize=(10, 7), title='Заголовок')
# .plot() ПРИНИМАЕТ оформление параметрами: figsize, title, xlabel, ylabel, grid, color

# ── СПОСОБ 2: matplotlib — длиннее, но полный контроль ───────────
plt.figure(figsize=(10, 7))      # создать холст нужного размера
plt.title('Заголовок')           # заголовок — отдельным вызовом
plt.hist(data['popularity'], bins=50)   # сам график
plt.show()                       # показать
# plt.hist() НЕ принимает figsize/title — только данные и настройки самих столбцов
```

Если написать `plt.hist(..., figsize=(10,7))` — получишь
`AttributeError: Rectangle.set() got an unexpected keyword argument 'figsize'`.

---

## Гистограмма — распределение одного числового признака

```python
# одной строкой (pandas)
data['popularity'].plot(kind='hist', bins=50, figsize=(10, 7),
                        title='Распределение popularity',
                        xlabel='popularity', ylabel='кол-во персонажей')
# kind='hist'  - тип графика: гистограмма
# bins=50      - на сколько интервалов разбить ось X
# figsize      - размер картинки в дюймах (ширина, высота)
# title        - заголовок
# xlabel/ylabel- подписи осей

# многострочно (matplotlib)
plt.figure(figsize=(10, 7))                 # новый холст
plt.title('Распределение popularity', fontsize=20)   # fontsize - размер шрифта заголовка
plt.xlabel('popularity')                    # подпись горизонтальной оси
plt.ylabel('кол-во персонажей')             # подпись вертикальной оси
plt.hist(data['popularity'], bins=50)       # сама гистограмма
plt.show()                                  # отрисовать и очистить холст

# короткий метод .hist() — принимает figsize, но НЕ title/xlabel
data['popularity'].hist(bins=50, figsize=(10, 7))

# сразу несколько колонок — сетка гистограмм
df[['Age', 'Fare']].hist(bins=30, figsize=(10, 4))
```

### Две гистограммы наложением — сравнить группы

```python
plt.figure(figsize=(8, 5))
plt.hist(df['Age'][df['Survived'] == 0], alpha=0.5, label='не выжил')
plt.hist(df['Age'][df['Survived'] == 1], alpha=0.5, label='выжил')
# alpha=0.5 - полупрозрачность, иначе второй график закроет первый
# label     - подпись для легенды
plt.legend()     # показать легенду; без неё label не отобразится
plt.show()
```

### Вертикальные линии на графике — отметить среднее и медиану

```python
plt.figure(figsize=(8, 5))
plt.hist(df['Age'].dropna(), bins=30)
plt.axvline(df['Age'].mean(),   color='r', linestyle='-',  label='mean')
plt.axvline(df['Age'].median(), color='g', linestyle='--', label='median')
# axvline   - вертикальная линия в точке x
# color     - цвет: 'r' красный, 'g' зелёный, 'b' синий, 'black'
# linestyle - '-' сплошная, '--' пунктир, ':' точки
plt.legend()
plt.show()
```

---

## Столбчатые диаграммы

```python
# ── ГОРИЗОНТАЛЬНЫЕ (barh) — когда подписи длинные ───────────────
corr = data.corr(numeric_only=True)['isAlive'].drop('isAlive').sort_values()

# одной строкой
corr.plot(kind='barh', figsize=(10, 8), title='Корреляция с isAlive', grid=True)
# grid=True - сетка

# многострочно, с настройками
plt.figure(figsize=(10, 8))
plt.barh(corr.index, corr.values)        # первый аргумент - подписи, второй - длины полос
plt.grid(axis='x', linestyle='--', alpha=0.6)   # axis='x' - только вертикальные линии сетки
plt.axvline(0, color='black', linewidth=0.8)    # нулевая отметка
plt.tight_layout()                       # чтобы длинные подписи не обрезались
plt.show()

# цвет по знаку значения
colors = ['tomato' if v < 0 else 'seagreen' for v in corr.values]
corr.plot(kind='barh', figsize=(10, 8), color=colors)

# ── ВЕРТИКАЛЬНЫЕ (bar) ──────────────────────────────────────────
data['numDeadRelations'].value_counts().sort_index().plot(kind='bar', figsize=(10, 5))
# value_counts()  - посчитать, сколько раз встретилось каждое значение
# .sort_index()   - упорядочить по значению, а не по частоте

# ── ПРОПУСКИ ПО КОЛОНКАМ — классический приём ───────────────────
nul = df.isna().sum()                    # сколько NaN в каждой колонке
plt.figure(figsize=(10, 7))
plt.barh(nul.index, nul.values)          # .index - имена колонок, .values - числа
plt.title('Пропуски по колонкам')
plt.show()
```

---

## Круговая диаграмма

```python
vc = df['Survived'].value_counts()       # Series: значение -> сколько раз

# matplotlib
plt.figure(figsize=(6, 6))
plt.pie(vc, autopct='%1.1f%%')           # autopct - формат подписи процентов
plt.legend(['не выжили', 'выжили'], bbox_to_anchor=(1.0, 0.5))
# bbox_to_anchor=(x, y) - куда поставить легенду: (0,0) левый низ, (1,1) правый верх
#                         значения больше 1 выносят легенду за пределы графика
plt.title('Доля выживших')
plt.show()

# pandas, одной строкой
vc.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), ylabel='')
# ylabel='' - убрать лишнюю подпись сбоку, которую pandas ставит по умолчанию
```

Разбор `autopct='%1.1f%%'`:
`%` начало подстановки · `1` ширина поля · `.1` знаков после запятой · `f` дробное число · `%%` сам знак процента

---

## Точечный график — связь двух числовых признаков

```python
# matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Fare'], alpha=0.5)   # alpha - прозрачность точек
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# pandas, одной строкой
df.plot(kind='scatter', x='Age', y='Fare', figsize=(8, 6), alpha=0.5, title='Возраст и цена билета')
```

---

## Ящик с усами — разброс и выбросы

```python
# matplotlib, одна колонка
plt.figure(figsize=(8, 5))
plt.boxplot(df['Age'].dropna(), showfliers=False)
# dropna()         - boxplot не умеет в NaN, их надо убрать
# showfliers=False - не показывать выбросы отдельными точками
plt.show()

# seaborn, разбивка по группам — вот где он сильнее
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Pclass', y='Age')
# x - категория (по ней разделятся ящики), y - число
plt.show()
```

---

## Seaborn — статистические графики

```python
import seaborn as sns

# ── ТЕПЛОВАЯ КАРТА КОРРЕЛЯЦИЙ ───────────────────────────────────
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,        # писать числа внутри клеток
            fmt='.2f',         # формат чисел: 2 знака после запятой
            cmap='coolwarm',   # палитра: синий-белый-красный
            center=0,          #белый цвет соответствует нулю
            square=True)       # квадратные клетки
plt.show()
# numeric_only=True ОБЯЗАТЕЛЕН, иначе ValueError на текстовых колонках

# ── ГИСТОГРАММА С РАЗБИВКОЙ ПО КАТЕГОРИИ ────────────────────────
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Age', hue='Survived', kde=True)
# hue='Survived' - раскрасить по значению этой колонки
# kde=True       - добавить сглаженную кривую плотности
plt.show()

# ── ВСЕ ПАРЫ ПРИЗНАКОВ СРАЗУ ────────────────────────────────────
sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']].dropna(),
             diag_kind='hist',  # что рисовать на диагонали: 'hist' или 'kde'
             height=2)          # размер одной ячейки сетки
plt.show()

# ── ТОЧКИ + ЛИНИЯ ТРЕНДА ────────────────────────────────────────
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Age', y='Fare')   # сам проводит прямую через облако точек
plt.show()

# ── ГЛОБАЛЬНЫЕ НАСТРОЙКИ ────────────────────────────────────────
sns.set(font_scale=1.2)    # увеличить все шрифты разом
```

---

## Несколько графиков рядом

```python
fig, ax = plt.subplots(1, 2, figsize=(12, 4))   # 1 строка, 2 колонки
# ax - массив областей; обращение по номеру

ax[0].hist(df['Age'].dropna(), bins=20)
ax[0].set_title('Возраст')      # у ax НЕ plt.title(), а .set_title()

ax[1].hist(df['Fare'], bins=20)
ax[1].set_title('Цена билета')

plt.tight_layout()   # расставить без наложений
plt.show()
```

У областей `ax` свои имена методов: `set_title`, `set_xlabel`, `set_ylabel` вместо `plt.title`, `plt.xlabel`, `plt.ylabel`.

---

## Сохранить картинку в файл

```python
plt.figure(figsize=(10, 7))
plt.hist(df['Age'].dropna())
plt.savefig('график.png', dpi=100, bbox_inches='tight')
# dpi               - качество (точек на дюйм)
# bbox_inches='tight' - обрезать пустые поля по краям
plt.show()           # savefig ВСЕГДА до show(), иначе файл будет пустым
```

---

## Что чем рисовать

| задача | график |
|---|---|
| распределение одного числа | `hist` |
| сравнить распределения двух групп | две `hist` с `alpha=0.5`, или `sns.histplot(hue=...)` |
| сколько чего по категориям | `bar` / `barh` |
| длинные подписи категорий | `barh` (горизонтальный) |
| доли целого | `pie` |
| связь двух чисел | `scatter`, `sns.regplot` |
| разброс и выбросы | `boxplot` |
| все корреляции разом | `sns.heatmap` |
| всё со всем | `sns.pairplot` |

---

## Частые параметры

| параметр | где | что делает |
|---|---|---|
| `figsize=(ш, в)` | `plt.figure`, `.plot` | размер картинки в дюймах |
| `bins=50` | `hist` | число интервалов |
| `alpha=0.5` | везде | прозрачность от 0 до 1 |
| `color='r'` | везде | цвет |
| `label='текст'` | при отрисовке | подпись для легенды |
| `fontsize=20` | `title`, `xlabel` | размер шрифта |
| `linestyle='--'` | линии | пунктир |
| `grid=True` | `.plot` | сетка |
| `rotation=45` | `plt.xticks` | повернуть подписи оси |

---

## Три частые ошибки

```python
plt.barh(corr.index, corr.values, figsize=(10,8))   # ✗ figsize не параметр plt.*
plt.barh(data, figsize=(10,8))                      # ✗ передана вся таблица вместо данных
sns.heatmap(df.corr())                              # ✗ упадёт, если есть текстовые колонки
```

```python
plt.figure(figsize=(10,8)); plt.barh(corr.index, corr.values)   # ✓
corr.plot(kind='barh', figsize=(10,8))                          # ✓
sns.heatmap(df.corr(numeric_only=True))                         # ✓
```
