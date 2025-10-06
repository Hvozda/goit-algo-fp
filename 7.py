import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_trials=1000000):
    """
    Імітація кидків двох кубиків методом Монте-Карло.
    num_trials — кількість кидків (чим більше, тим точніше).
    """
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    # Обчислюємо ймовірності (%)
    probabilities = {s: (count / num_trials) * 100 for s, count in sums_count.items()}
    return probabilities


def analytical_probabilities():
    """Аналітичні (точні) ймовірності сум при киданні двох кубиків."""
    return {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }


def print_comparison_table(simulated, analytical):
    """Виводить порівняльну таблицю результатів."""
    print(f"{'Сума':<6} {'Monte Carlo (%)':<18} {'Аналітична (%)':<18} {'Різниця (%)':<15}")
    print("-" * 60)
    for s in range(2, 13):
        sim = simulated[s]
        ana = analytical[s]
        diff = abs(sim - ana)
        print(f"{s:<6} {sim:<18.2f} {ana:<18.2f} {diff:<15.2f}")


def plot_probabilities(simulated, analytical):
    """Побудова графіка для порівняння результатів."""
    sums = list(range(2, 13))
    sim_values = [simulated[s] for s in sums]
    ana_values = [analytical[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_values, width=0.4, label="Monte Carlo", align='center', alpha=0.7)
    plt.plot(sums, ana_values, 'ro-', label="Аналітична", linewidth=2)
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    num_trials = 1000000  # можна зменшити для швидшої симуляції

    simulated_probs = monte_carlo_dice_simulation(num_trials)
    analytical_probs = analytical_probabilities()

    print("\nРезультати імітації методом Монте-Карло:\n")
    print_comparison_table(simulated_probs, analytical_probs)

    plot_probabilities(simulated_probs, analytical_probs)



              