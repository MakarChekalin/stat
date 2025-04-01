import numpy as np
import matplotlib.pyplot as plt
import math
from task_2_12 import prob, gen_random, check_prob



def plot_of_prob(n = 10, r=1, a=6):
    teor_p = prob(r, a)
    real_p = []
    gap_n = []


    for i in range(2, n-2):
        gap_n.append(n**i)

    
    for k in gap_n:
        real_p.append(check_prob(r = r, n = k))

    
    plt.figure(figsize=(8, 5))
    plt.plot(gap_n, real_p, marker='o', label='Приближённая вероятность $\\hat{p}(n)$')
    plt.axhline(teor_p, color='red', linestyle='--', label='Теоретическая вероятность $p$')

    plt.xscale('log')  # логарифмическая шкала для n
    plt.xlabel("Количество точек n")
    plt.ylabel("Вероятность попадания в круг")
    plt.title(f"График $\\hat{{p}}(n)$ при r = {r}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(plot_of_prob(r=4, a=6))