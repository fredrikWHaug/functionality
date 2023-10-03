import numpy as np

# every thoght you have 
# every interaction you make
# must be robust (implementation)
def robustness(x, y):
    sum = 0
    sum += (np.sqrt(x) + np.sqrt(y));
    return sum

# main execution
if __name__ == '__main__':
    x = int(input("Give me an x: "));
    y = int(input('Give me a y: '));
    print(f"Here is the output of the function with your specifications: {robustness(x, y)}")
    print(f"Here is the output of the function with your specifications: {robustness(x, y)}")
    print(f"Here is the output of the function with your specifications: {robustness(x, y)}")

