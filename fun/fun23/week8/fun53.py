
# prints staircase
def staircase(n):
    step = "#"
    for i in range(n):
        print(step)
        step = step + "#"

# main execution
if __name__ == "__main__":
    staircase(3)