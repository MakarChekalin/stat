import matplotlib.pyplot as plt
from task_2_12 import prob, check_prob


def error_n(r = 1, epsi = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]):
    teor_p = prob(r, 6)  # теор
    n_val = []

    for eps in epsi:
        n = 10  

        while n <= 1000000:
            real_p = check_prob(r=r, n=n) #прибл.
            error = abs(real_p - teor_p)

            if error < eps:
                n_val.append(n)
                break

            n += 10 

        else:# если нет
            n_val.append(None)  

    plt.figure(figsize=(8, 5))
    plt.plot(epsi, n_val, marker='o', label=f"r = {r}")
    plt.xscale('log')
    plt.yscale('log')
    plt.gca().invert_xaxis()  # ε убывает справа налево
    plt.xlabel("Точность ε")
    plt.ylabel("Необходимое количество точек N")
    plt.title(f"Зависимость N(ε) при r = {r}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()





if __name__ == "__main__":
    print(error_n())

    

        

