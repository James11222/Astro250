import matplotlib.pyplot as plt
import matplotlib as mpl
import multiprocessing
from multiprocessing import Array
from random import uniform
from math import sqrt
from time import time
import numpy as np
import dask.array as da
import argparse


parser = argparse.ArgumentParser(description='Parallel Investigation of Computing π')

parser.add_argument('-n', action='store', dest='n_proc',
                    help='Store a constant value')

results = parser.parse_args()
n_proc = int(results.n_proc)

if n_proc is None:
    n_proc = 4

print('Number of Processes   =', n_proc)


mpl.rcParams['axes.linewidth'] = 1.8 #set the value globally
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['font.size'] = 22

######################################################################

#First we need to write the naive implementation


def estimate_π(num):
    """
    A simple function to estimate π using
    sampling from a normal distribution with num points.
    
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
    
    return [execution_time, number_of_darts/execution_time]

######################################################################


def estimate_π_parallel(number_of_darts, n_processes):
    """
    A parallelized function to estimate π using
    sampling from a normal distribution.
    
    """

    chunk_size = int(number_of_darts/n_processes)
    total_sum = Array('i', [0] * n_processes, lock=False)
    
    def throw_dart():
        x, y = uniform(0,1), uniform(0,1)
        if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
            return 1
        else:
            return 0
    
    
    def sample_parallel(chunk_size, total_sum, i):
        total_sum[i] = sum(throw_dart() for j in range(chunk_size))
  
    start_time = time()
    
    processes = []
    for i in range(n_processes):
        p = multiprocessing.Process(target=sample_parallel,
                                   args=(chunk_size, total_sum, i))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    number_of_darts_in_circle = sum(total_sum)
    
    end_time = time()
    execution_time = end_time - start_time
    pi_approx = 4 * number_of_darts_in_circle / float(number_of_darts)
    
    return [execution_time, number_of_darts/execution_time]

######################################################################


def estimate_π_dask(number_of_darts, n_chunks):
    """
    A function to estimate π using dask arrays to
    sample from a normal distribution.
    
    """
    number_of_darts_in_circle = 0
    start_time = time()
    
    if number_of_darts < 1e1:
        n_chunks = 1
        
    x = da.random.uniform(0, 1, size=(number_of_darts), chunks=(int(number_of_darts/n_chunks)))
    y = da.random.uniform(0, 1, size=(number_of_darts), chunks=(int(number_of_darts/n_chunks)))
    r = da.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    
    result = da.where(r <= 0.5)[0]
    number_of_darts_in_circle = len(result.compute())
    
    end_time = time()
    execution_time = end_time - start_time
    pi_approx = 4 * number_of_darts_in_circle / float(number_of_darts)
    
    return [execution_time, number_of_darts/execution_time]
        
######################################################################


def calc_results(darts_list):
    """
    Compile all the simulation results over increasing
    number of darts thrown.
    
    """
    single_thread_results = []
    parallel_results = []
    dask_results = []

    for i, num_darts in enumerate(darts_list):

        single_thread_results.append(estimate_π(int(num_darts)))
        parallel_results.append(estimate_π_parallel(int(num_darts), n_proc))
        dask_results.append(estimate_π_dask(int(num_darts), n_proc))

    single_thread_results = np.array(single_thread_results)
    parallel_results = np.array(parallel_results)
    dask_results = np.array(dask_results)   
    
    return single_thread_results, parallel_results, dask_results


######################################################################


def make_plot(darts_list, avg_results, std_results):
    
    """
    Produce Plot of Results
    """
    fig, axes = plt.subplots(1,1, figsize=(10,8))
    axes.set_title("Macbook Pro - 2.9 GHz Quad-Core Intel Core i7")

    axes.plot(darts_list, avg_results[0,:,0], color="red", linewidth=3,label="Simple")
    axes.plot(darts_list, avg_results[1,:,0], color="blue",linewidth=3, label="Multiprocessing")
    axes.plot(darts_list, avg_results[2,:,0], color="green",linewidth=3, label="Dask")

    axes.fill_between(darts_list, 
                     y1 = avg_results[0,:,0] - std_results[0,:,0]/2, 
                     y2 = avg_results[0,:,0] + std_results[0,:,0]/2, color="red", alpha=0.5)
    axes.fill_between(darts_list, 
                     y1 = avg_results[1,:,0] - std_results[1,:,0]/2, 
                     y2 = avg_results[1,:,0] + std_results[1,:,0]/2, color="blue", alpha=0.5)
    axes.fill_between(darts_list, 
                     y1 = avg_results[2,:,0] - std_results[2,:,0]/2, 
                     y2 = avg_results[2,:,0] + std_results[2,:,0]/2, color="green", alpha=0.5)
    axes.loglog()
    axes.legend(loc="lower right", fontsize=22, shadow=True, edgecolor="black")
    axes.grid()
    axes.set_xlabel("Darts Thrown")
    axes.set_ylabel("Execution Time [s] - Solid Line")
    axes.set_ylim(5e-5,1e2)
    axes.set_xlim(1e1, 1e7)

    axes2 = axes.twinx()
    axes2.set_ylim(2e2,5e7)

    axes2.plot(darts_list, avg_results[0,:,1], color="red", linewidth=3,linestyle="--")
    axes2.plot(darts_list, avg_results[1,:,1], color="blue",linewidth=3,linestyle="--")
    axes2.plot(darts_list, avg_results[2,:,1], color="green",linewidth=3,linestyle="--")
    axes2.loglog()

    axes2.set_ylabel("Simulation Rate [darts/second] - Dashed Line")
    plt.savefig("Scaling_Results_" + str(n_proc) + "_processes.png")
    plt.show()
    
    
######################################################################

def main():
    darts_list = [1e1, 5e1, 1e2, 5e2, 1e3, 5e3, 1e4, 5e4, 1e5, 5e5, 1e6, 1e7]
    
    results = np.array([calc_results(darts_list) for i in range(10)])
    avg_results = np.mean(results, axis=0)
    std_results = np.std(results, axis=0)
    
    make_plot(darts_list, avg_results, std_results)
    
if __name__ == '__main__':
    main()
    



