# plotting
import matplotlib.pyplot as plt 
import numpy as np 

# main function
def main():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)
    plt.xlabel('Time')
    plt.ylabel('Happiness')
    plt.plot(x, y)
    plt.show()

# main execution
if __name__ == '__main__':
    main()