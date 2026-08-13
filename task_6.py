items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Жадібний вибір: сортуємо за calories/cost (спадання), беремо страву,
    якщо вона влазить у залишок бюджету. Повертає (обрані_страви, сумарні_калорії).
    """
    ranked = sorted(
        items.items(),
        key=lambda pair: pair[1]["calories"] / pair[1]["cost"],
        reverse=True,
    )

    selected = {}
    total_calories = 0
    remaining_budget = budget

    for name, info in ranked:
        if info["cost"] > remaining_budget:
            continue

        selected[name] = info["calories"]
        total_calories += info["calories"]
        remaining_budget -= info["cost"]

    return selected, total_calories


def dynamic_programming(items, budget):
    """0/1 knapsack: dp[i][b] — максимальна калорійність, використовуючи
    перші i страв у межах бюджету b. Повертає (обрані_страви, максимальні_калорії).
    """
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]

    # відновлення набору страв за заповненою таблицею dp
    selected = {}
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            selected[name] = items[name]["calories"]
            b -= items[name]["cost"]

    return selected, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    greedy_selected, greedy_calories = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("  страви:", list(greedy_selected.keys()))
    print("  калорії:", greedy_calories)

    dp_selected, dp_calories = dynamic_programming(items, budget)
    print("Динамічне програмування:")
    print("  страви:", list(dp_selected.keys()))
    print("  калорії:", dp_calories)
