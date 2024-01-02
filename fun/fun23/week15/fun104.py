# matpolotlib plot
import matplotlib.pyplot as plt 
import numpy as np 

def plot_sine():
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('mV')
    plt.title('Sine function')
    plt.show()

# main function
def main():
    plot_sine()

# main execution
if __name__ == '__main__':
    main()