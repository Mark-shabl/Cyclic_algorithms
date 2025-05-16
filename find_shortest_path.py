# 5
from collections import deque


def find_shortest_path(maze):
    """
    Находит кратчайший путь в лабиринте от 'C' до 'B'.
    Возвращает длину пути и сам путь.
    """
    # Находим стартовую позицию
    start = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'C':
                start = (i, j)
                break
        if start is not None:
            break

    if not start:
        return -1, []  # Старт не найден

    # Направления движения (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(maze), len(maze[0])

    # Очередь для BFS: (row, col, path)
    queue = deque()
    queue.append((start[0], start[1], []))
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        row, col, path = queue.popleft()

        # Проверяем, достигли ли выхода
        if maze[row][col] == 'B':
            full_path = [(start[0], start[1])] + path
            return len(full_path) - 1, full_path

        # Исследуем соседние клетки
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                if (r, c) not in visited and maze[r][c] != 'X':
                    visited.add((r, c))
                    queue.append((r, c, path + [(r, c)]))

    return -1, []  # Путь не найден


# Пример использования:
maze = [
    ['C', '0', '0', '0', '0', 'X', '0', '0'],
    ['0', '0', 'X', '0', '0', 'X', '0', '0'],
    ['X', '0', 'X', '0', '0', 'X', '0', 'X'],
    ['0', '0', 'X', '0', '0', '0', '0', '0'],
    ['0', '0', 'X', '0', 'X', 'X', 'X', '0'],
    ['X', '0', '0', '0', '0', '0', '0', '0'],
    ['X', '0', '0', '0', 'X', '0', '0', 'B']
]

length, path = find_shortest_path(maze)
print(f"Длина пути: {length}")
print("Путь (координаты строк и столбцов):")
for step in path:
    print(step)