from time import sleep, perf_counter

def task():
    print('Time to...')
    sleep(1)
    print('eat')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f' {end_time- start_time: 0.2f} second(s) to complete the process.')