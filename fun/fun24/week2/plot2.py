# plot
import numpy as np 
import matplotlib.pyplot as plt 

# main function
def main():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.plot(x, y)

    plt.xlabel('Time')
    plt.ylabel('Attraction')
    plt.title('Plot')
    
    plt.show()

# main execution
if __name__ == '__main__':
    main()