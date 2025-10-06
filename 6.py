# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм:
    вибирає страви з найбільшим співвідношенням калорій до вартості,
    поки є гроші у бюджеті.
    """
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування (аналог задачі "рюкзака"):
    шукає оптимальний набір страв для максимізації калорійності.
    """
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(names[i - 1])
            b -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in chosen_items)

    return chosen_items[::-1], total_cost, total_calories


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Жадібний алгоритм:")
    print("Обрані страви:", greedy_result[0])
    print("Загальна вартість:", greedy_result[1])
    print("Загальна калорійність:", greedy_result[2])

    print("\nДинамічне програмування:")
    print("Обрані страви:", dp_result[0])
    print("Загальна вартість:", dp_result[1])
    print("Загальна калорійність:", dp_result[2])




   