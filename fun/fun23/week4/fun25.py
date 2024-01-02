
# processing time
def minimum_processing_time(processing_time, tasks):
    tasks.sort()
    processing_time.sort()
    processing_time.reverse()

    time = []
    for i in range(0, len(processing_time)):
        time.append(tasks[(i+1)*4-1] + processing_time[i])
    
    return max(time)

# main execution
if __name__ == '__main__':
    processing_time = [8, 10]
    tasks = [2, 5, 4, 1, 1, 9, 8, 7]

    min_time = minimum_processing_time(processing_time, tasks)
    print(min_time)