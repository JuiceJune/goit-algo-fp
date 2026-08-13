import random
from collections import Counter

import matplotlib.pyplot as plt

ANALYTICAL_PROBABILITIES = {
    2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36,
    7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36,
}


def simulate_dice_rolls(num_rolls):
    """Кидає два кубики num_rolls разів, повертає Counter {сума: кількість появ}."""
    counts = Counter()
    for _ in range(num_rolls):
        first_try = random.randint(1, 6)
        second_try = random.randint(1, 6)
        counts[first_try + second_try] += 1
    return counts


def probabilities_from_counts(counts, num_rolls):
    """Переводить кількість появ кожної суми у відсоткову ймовірність."""
    return {s: counts.get(s, 0) / num_rolls * 100 for s in range(2, 13)}


def print_comparison_table(mc_probabilities):
    print(f"{'Сума':<6}{'Монте-Карло, %':<16}{'Аналітично, %':<15}{'Різниця, %':<10}")
    for s in range(2, 13):
        mc = mc_probabilities[s]
        analytic = ANALYTICAL_PROBABILITIES[s] * 100
        diff = mc - analytic
        print(f"{s:<6}{mc:<16.2f}{analytic:<15.2f}{diff:+.2f}")


def plot_comparison(mc_probabilities, path=None):
    sums = list(range(2, 13))
    mc_values = [mc_probabilities[s] for s in sums]
    analytic_values = [ANALYTICAL_PROBABILITIES[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width / 2 for i in x], mc_values, width, label="Монте-Карло")
    plt.bar([i + width / 2 for i in x], analytic_values, width, label="Аналітично")
    plt.xticks(list(x), sums)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Імовірність, %")
    plt.title("Монте-Карло vs аналітичні ймовірності")
    plt.legend()

    if path:
        plt.savefig(path)
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    NUM_ROLLS = 1_000_000

    counts = simulate_dice_rolls(NUM_ROLLS)
    mc_probabilities = probabilities_from_counts(counts, NUM_ROLLS)

    print_comparison_table(mc_probabilities)
    plot_comparison(mc_probabilities)
