import pandas as pd

# linear regression
def main():
    df = pd.read_csv('student_performance.csv')
    df = df.sample(50)
    

if __name__ == '__main__':
    main()