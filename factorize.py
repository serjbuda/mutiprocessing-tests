import multiprocessing
import time

def factorize(*numbers):
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize_number, numbers)
    end_time = time.time()
    print('Time:', end_time - start_time, 'seconds')
    return results

def factorize_number(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result

results = factorize(128, 255, 99999, 10651060)
print(results)
