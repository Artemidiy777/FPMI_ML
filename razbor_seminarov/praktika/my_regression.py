"""Задание: реализовать три класса линейной регрессии с нуля.

Заполни тела методов вместо raise NotImplementedError.
Проверка: python3 test_my_regression.py

Подсказки по формулам — в ../02_analiticheskoe.md и ../03_gradientnoe.md
Подсказки по numpy — в ../05_numpy.md
"""
import numpy as np


class MyLinearRegression:
    """Линейная регрессия через точную формулу w = (XᵀX)⁻¹Xᵀy."""

    def __init__(self):
        self.w = None

    def fit(self, X, y):
        """X: (ℓ, n) признаки, y: (ℓ,) ответы.

        Шаги:
        1. привести к np.array
        2. сделать y столбцом через np.newaxis
        3. добавить к X столбец единиц (фиктивный признак для b)
        4. посчитать веса по формуле
        5. вернуть self
        """
        raise NotImplementedError

    def predict(self, X):
        """X: (ℓ, n) -> предсказания (ℓ, 1).

        Не забудь добавить столбец единиц, как в fit.
        """
        raise NotImplementedError

    def get_weights(self):
        """Вернуть КОПИЮ весов, а не ссылку."""
        raise NotImplementedError


class MyGradientLinearRegression(MyLinearRegression):
    """Та же регрессия, но веса ищутся градиентным спуском."""

    def fit(self, X, y, lr=0.01, max_iter=1000):
        """Шаги:
        1. подготовка как в MyLinearRegression (newaxis, столбец единиц)
        2. начальные веса: нули или np.random.randn(n + 1, 1)
        3. self.losses = []
        4. цикл max_iter раз:
             y_pred = self.predict(X)
             записать MSE в self.losses
             grad = self._calc_gradient(X_train, y, y_pred)
             self.w -= lr * grad
        5. вернуть self
        """
        raise NotImplementedError

    def _calc_gradient(self, X, y, y_pred):
        """Градиент MSE: (2/ℓ) · Xᵀ(y_pred − y).

        Здесь X — уже со столбцом единиц.
        Результат должен иметь ту же форму, что self.w
        """
        raise NotImplementedError

    def get_losses(self):
        return self.losses


class MySGDLinearRegression(MyGradientLinearRegression):
    """Стохастический спуск: градиент по случайному батчу."""

    def __init__(self, n_sample=10):
        super().__init__()
        self.n_sample = n_sample

    def _calc_gradient(self, X, y, y_pred):
        """То же, но по случайным n_sample объектам.

        Шаги:
        1. выбрать индексы: np.random.choice(..., size=self.n_sample, replace=False)
        2. посчитать градиент только по X[inds], y[inds], y_pred[inds]
        3. делить на self.n_sample, а не на ℓ
        """
        raise NotImplementedError
