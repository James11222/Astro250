#First we need to write the naive implementation

from random import uniform
from math import sqrt
from time import time
import concurrent.futures


def estimate_π(num):
    """
    A simple function to estimate π using
    sampling from a normal distribution
    """
    number_of_darts = num
    number_of_darts_in_circle = 0

    start_time = time()

    for n in range(number_of_darts):
        x, y = uniform(0,1), uniform(0,1)
        if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
            number_of_darts_in_circle += 1

    end_time = time()
    execution_time = end_time - start_time

    pi_approx = 4 * number_of_darts_in_circle / float(number_of_darts)

    print("π = ", pi_approx)
    print("Number of Darts: ", number_of_darts)
    print("Execution Time: {} seconds ".format(execution_time))
    print("Darts Thrown per second: ", number_of_darts/execution_time)

    

def throw_dart(i):
    x, y = uniform(0,1), uniform(0,1)
    if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
        return 1
    else:
        return 0
    

def estimate_π_concurrent_futures(num):
    
    number_of_darts = num
    
    start_time = time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(throw_dart, list(range(number_of_darts))))

    number_of_darts_in_circle = sum(results)
    
    end_time = time()
    execution_time = end_time - start_time
    pi_approx = 4 * number_of_darts_in_circle / float(number_of_darts)
    
    print("π = ", pi_approx)
    print("Number of Darts: ", number_of_darts)
    print("Execution Time: {} seconds ".format(execution_time))
    print("Darts Thrown per second: ", number_of_darts/execution_time)
    
print("\nSingle Thread: \n")
estimate_π(1e6)

print("\nMultithread: \n")
estimate_π_concurrent_futures(1e6)