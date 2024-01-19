# plot
import matplotlib.pyplot as plt 
import numpy as np 

# main function
def main():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.figure(1)
    plt.plot(x, y, color='magenta')
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Signal')
    
    plt.show()

# main execution
if __name__ == '__main__':
    main()