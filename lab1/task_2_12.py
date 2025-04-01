# from task_1 import graf
import random
import matplotlib.pyplot as plt
import math


def prob(r, a = 6): #вероятность
    sq_sq = (2 * a) ** 2 # площадь квадрата 
    ci_sq = math.pi * ((r) ** 2) # площадь окружности

    probability = ci_sq / sq_sq
    return probability


def in_sq(set_of_cords : set, r):
    if set_of_cords[0]**2 + set_of_cords[1]**2 <= r ** 2:
        return True
    else:
        return False


def gen_random(n = 100, a = 6):
    all_n = []

    for _ in range(n):
        x = random.uniform(-a, a)
        y = random.uniform(-a, a)
        all_n.append((x, y))
    
    return all_n


def check_prob(r, n): # ген. рандом точки и выч вероятность
    all_n = gen_random(n)
    in_ci = 0

    for i in range(len(all_n)): # проверка на попадение в круг
        if in_sq(all_n[i], r):
            in_ci += 1

    real_probability = in_ci/n
    return (real_probability)



if __name__ == "__main__":
    print(prob(1))
    print(check_prob(1, 10000))