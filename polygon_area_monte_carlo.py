# 3
import random


def polygon_area_monte_carlo(vertices, num_points=100000):
    """
    Вычисляет площадь выпуклого многоугольника методом Монте-Карло.
    vertices - список вершин многоугольника в порядке обхода.
    """
    # Находим ограничивающий прямоугольник
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    count_inside = 0

    for _ in range(num_points):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        if point_in_polygon((x, y), vertices):
            count_inside += 1

    area_rect = (max_x - min_x) * (max_y - min_y)
    return area_rect * count_inside / num_points


def point_in_polygon(point, polygon):
    """
    Проверяет, находится ли точка внутри многоугольника (алгоритм ray casting).
    """
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# Пример использования:
vertices = [(0, 0), (2, 0), (2, 2), (1, 3), (0, 2)]
area = polygon_area_monte_carlo(vertices)
print(f"Площадь многоугольника: {area:.6f}")