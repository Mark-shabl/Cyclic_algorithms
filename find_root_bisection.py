#1
def find_root_bisection(f, a, b, epsilon=1e-6):
    """
    Находит корень уравнения f(x) = 0 на отрезке [a, b] с точностью epsilon.
    Использует метод бисекции.
    """
    if f(a) * f(b) > 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка")

    while (b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Пример использования:
def example_function(x):
    return x ** 3 - 2 * x - 5


root = find_root_bisection(example_function, 2, 3)
print(f"Корень уравнения: {root:.6f}")