import matplotlib.pyplot as plt

a = 6
r = [1, 2, 3, 4, 5]


def graf(n):
    fig, ax = plt.subplots(figsize=(5, 5)) 


    square = plt.Rectangle((-a, -a), 2*a, 2*a, edgecolor='black', facecolor='none', linewidth=2) # квадрат 
    ax.add_patch(square)



    circle = plt.Circle((0, 0), r[n], edgecolor='blue', facecolor='lightblue', alpha=0.5, linewidth=2) # круг
    ax.add_patch(circle)


    ax.axhline(0, color='black', linewidth=1.5) # ось x 
    ax.axvline(0, color='black', linewidth=1.5) # ось y
    ax.set_xlim(-a - 3, a + 3)
    ax.set_ylim(-a - 3, a + 3)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

    plt.show()

if __name__ == "__main__":
    graf(1)