"""Проверка твоих классов. Запуск: python3 test_my_regression.py

Каждый тест сравнивает твою реализацию с sklearn.
Пока метод не написан, тест покажет "не реализовано" — это нормально.
"""
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from sklearn.linear_model import LinearRegression
from my_regression import (MyLinearRegression, MyGradientLinearRegression,
                           MySGDLinearRegression)

OK, FAIL, SKIP = "\033[92mОК\033[0m", "\033[91mНЕ СОШЛОСЬ\033[0m", "\033[93mне реализовано\033[0m"


def make_data(n=200, seed=0):
    rng = np.random.default_rng(seed)
    X = rng.uniform(-5, 5, size=(n, 1))
    y = 5 * X[:, 0] + 6 + rng.normal(0, 2, n)
    return X, y


def check(name, fn):
    try:
        msg = fn()
        print(f"  {OK}   {name}" + (f"   {msg}" if msg else ""))
        return True
    except NotImplementedError:
        print(f"  {SKIP}  {name}")
    except AssertionError as e:
        print(f"  {FAIL}  {name}\n          {e}")
    except Exception as e:
        print(f"  {FAIL}  {name}\n          {type(e).__name__}: {e}")
    return False


def t_exact_weights():
    X, y = make_data()
    mine = MyLinearRegression().fit(X, y)
    ref = LinearRegression().fit(X, y)
    w = np.asarray(mine.get_weights()).ravel()
    assert len(w) == 2, f"ожидалось 2 веса (наклон и b), получено {len(w)}"
    assert abs(w[0] - ref.coef_[0]) < 1e-6, f"наклон: твой {w[0]:.6f}, sklearn {ref.coef_[0]:.6f}"
    assert abs(w[1] - ref.intercept_) < 1e-6, f"свободный член: твой {w[1]:.6f}, sklearn {ref.intercept_:.6f}"
    return f"w = {w[0]:.4f}, b = {w[1]:.4f}"


def t_exact_predict():
    X, y = make_data()
    mine = MyLinearRegression().fit(X, y)
    p = np.asarray(mine.predict(X)).ravel()
    ref = LinearRegression().fit(X, y).predict(X)
    assert p.shape == ref.shape, f"форма предсказаний {p.shape}, ожидалась {ref.shape}"
    assert np.allclose(p, ref, atol=1e-6), f"макс. расхождение {np.abs(p - ref).max():.2e}"
    return f"{len(p)} предсказаний"


def t_weights_copy():
    X, y = make_data()
    m = MyLinearRegression().fit(X, y)
    w = m.get_weights()
    before = np.asarray(m.get_weights()).ravel()[0]
    w[0] = 12345.0
    after = np.asarray(m.get_weights()).ravel()[0]
    assert abs(before - after) < 1e-12, "get_weights вернул ссылку, а не копию — нужен .copy()"
    return "копия, а не ссылка"


def t_grad_shape():
    X, y = make_data(50)
    m = MyGradientLinearRegression()
    Xt = np.hstack((X, np.ones((50, 1))))
    m.w = np.zeros((2, 1))
    g = m._calc_gradient(Xt, y[:, None], Xt @ m.w)
    assert np.asarray(g).shape == (2, 1), f"форма градиента {np.asarray(g).shape}, ожидалась (2, 1)"
    return "форма (2, 1)"


def t_grad_value():
    X = np.array([[1.], [2.], [3.], [4.]])
    y = np.array([4., 4., 6., 10.])
    Xt = np.hstack((X, np.ones((4, 1))))
    m = MyGradientLinearRegression()
    m.w = np.zeros((2, 1))
    g = np.asarray(m._calc_gradient(Xt, y[:, None], Xt @ m.w)).ravel()
    assert np.allclose(g, [-35., -12.]), f"градиент в нуле: твой {g.round(3)}, правильный [-35. -12.]"
    return "в точке (0,0) градиент (−35, −12)"


def t_gd_converges():
    X, y = make_data()
    mine = MyGradientLinearRegression().fit(X, y, lr=0.05, max_iter=3000)
    ref = LinearRegression().fit(X, y)
    w = np.asarray(mine.get_weights()).ravel()
    assert abs(w[0] - ref.coef_[0]) < 0.01, f"наклон: твой {w[0]:.4f}, sklearn {ref.coef_[0]:.4f}"
    assert abs(w[1] - ref.intercept_) < 0.01, f"b: твой {w[1]:.4f}, sklearn {ref.intercept_:.4f}"
    return f"сошёлся к w = {w[0]:.4f}, b = {w[1]:.4f}"


def t_losses_decrease():
    X, y = make_data()
    m = MyGradientLinearRegression().fit(X, y, lr=0.05, max_iter=500)
    L = list(m.get_losses())
    assert len(L) == 500, f"в истории {len(L)} значений, ожидалось 500"
    assert L[-1] < L[0], f"потери не упали: было {L[0]:.3f}, стало {L[-1]:.3f}"
    return f"MSE {L[0]:.1f} -> {L[-1]:.3f}"


def t_sgd_converges():
    X, y = make_data()
    mine = MySGDLinearRegression(n_sample=20).fit(X, y, lr=0.05, max_iter=3000)
    ref = LinearRegression().fit(X, y)
    w = np.asarray(mine.get_weights()).ravel()
    assert abs(w[0] - ref.coef_[0]) < 0.3, f"наклон: твой {w[0]:.4f}, sklearn {ref.coef_[0]:.4f}"
    assert abs(w[1] - ref.intercept_) < 0.3, f"b: твой {w[1]:.4f}, sklearn {ref.intercept_:.4f}"
    return f"сошёлся к w = {w[0]:.4f}, b = {w[1]:.4f}"


TESTS = [
    ("MyLinearRegression: веса совпали с sklearn", t_exact_weights),
    ("MyLinearRegression: предсказания совпали", t_exact_predict),
    ("MyLinearRegression: get_weights возвращает копию", t_weights_copy),
    ("MyGradientLinearRegression: форма градиента", t_grad_shape),
    ("MyGradientLinearRegression: значение градиента", t_grad_value),
    ("MyGradientLinearRegression: спуск сходится", t_gd_converges),
    ("MyGradientLinearRegression: потери падают", t_losses_decrease),
    ("MySGDLinearRegression: спуск сходится", t_sgd_converges),
]

if __name__ == "__main__":
    print("\nПроверка реализации\n" + "─" * 60)
    passed = sum(check(n, f) for n, f in TESTS)
    print("─" * 60)
    print(f"пройдено: {passed} из {len(TESTS)}\n")
