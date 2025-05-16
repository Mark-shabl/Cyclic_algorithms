#2
def calculate_area_trapezoid(f, a, b, n=1000):
    """
    Вычисляет площадь под графиком функции f(x) на отрезке [a, b]
    методом трапеций с n интервалами.
    """
    h = (b - a) / n
    area = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        area += f(a + i * h)
    return area * h

# Пример использования:
import math

def example_function(x):
    return math.sin(x)

area = calculate_area_trapezoid(example_function, 0, math.pi)
print(f"Площадь под графиком: {area:.6f}")