import matplotlib.pyplot as plt
from task_2_12 import prob, check_prob

def plot_of_error(n=10, r=1, a=6):
    teor_p = prob(r, a)  # теор. вер.
    errors = []
    gap_n = []


    for i in range(n - 3):
        gap_n.append(n ** i)

    for k in gap_n:
        real_p = check_prob(r=r, n=k)
        error = abs(real_p - teor_p)
        errors.append(error)


    plt.figure(figsize=(8, 5))
    plt.plot(gap_n, errors, marker='o', label='Ошибка')
    plt.xscale('log')
    plt.yscale('log')  # лог шкала по Y тоже, для мелких ошибок
    plt.xlabel("Количество точек n")
    plt.ylabel("Ошибка")
    plt.title(f"График ошибки r = {r}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_of_error(r = 1)