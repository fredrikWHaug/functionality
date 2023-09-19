import matplotlib.pyplot as plt
import numpy as np

def scatter_plot(x, y):
    scatter(x, y)

if __name__ == '__main__':
    my_x = [*range(10, 20, 1)]
    my_y = [*range(10, 20, 1)]

    plt.scatter(my_x, my_y)
    plt.show()
