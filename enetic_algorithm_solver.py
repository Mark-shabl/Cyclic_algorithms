# 4
import random


def genetic_algorithm_solver(f, target, bounds, pop_size=100, generations=100, mutation_rate=0.1):
    """
    Решает уравнение f(x1, x2, x3, x4) = target с помощью генетического алгоритма.
    bounds - список кортежей с минимальными и максимальными значениями для каждой переменной.
    """
    # Инициализация популяции
    population = []
    for _ in range(pop_size):
        individual = [random.uniform(b[0], b[1]) for b in bounds]
        population.append(individual)

    for _ in range(generations):
        # Оценка приспособленности
        fitness = []
        for individual in population:
            error = abs(f(*individual) - target)
            fitness.append(1 / (error + 1e-10))  # Чтобы избежать деления на 0

        # Селекция (турнирный отбор)
        new_population = []
        for _ in range(pop_size):
            candidates = random.choices(range(pop_size), weights=fitness, k=3)
            winner = max(candidates, key=lambda i: fitness[i])
            new_population.append(population[winner].copy())

        # Скрещивание (одноточечное)
        for i in range(0, pop_size, 2):
            if i + 1 < pop_size and random.random() < 0.7:
                crossover_point = random.randint(1, len(bounds) - 1)
                new_population[i][crossover_point:], new_population[i + 1][crossover_point:] = \
                    new_population[i + 1][crossover_point:], new_population[i][crossover_point:]

        # Мутация
        for i in range(pop_size):
            for j in range(len(bounds)):
                if random.random() < mutation_rate:
                    new_population[i][j] = random.uniform(bounds[j][0], bounds[j][1])

        population = new_population

    # Находим лучшую особь
    best_individual = min(population, key=lambda ind: abs(f(*ind) - target))
    return best_individual


# Пример использования:
def example_equation(x1, x2, x3, x4):
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2


bounds = [(-5, 5) for _ in range(4)]
solution = genetic_algorithm_solver(example_equation, 10, bounds)
print(f"Решение уравнения: {solution}, значение функции: {example_equation(*solution)}")