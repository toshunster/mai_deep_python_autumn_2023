#! /usr/bin/env python3

import os
import time
import multiprocessing as mp

N = 10 ** 7
N_PROC = 4
COUNT_SIZE = N // N_PROC

def task(left, right):
    print(f"{left=}, {right=}, pid={os.getpid()}, ppid={os.getppid()}")
    while left < right:
        left += 1

def main():
    start_ts = time.time()
    task(0, N)
    end_ts = time.time()
    print(f"Time of sync execution of task function is {end_ts - start_ts} seconds")

    procs = [
        mp.Process(target=task,
                   args=(num * COUNT_SIZE, (num+1) * COUNT_SIZE),
                   name=f"Process #{num}") for num in range(N_PROC)
    ]

    start_ts = time.time()
    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()
    end_ts = time.time()

    print(f"Time of sync execution of task function for {N_PROC} processes is {end_ts - start_ts} seconds")

if __name__ == "__main__":
    main()
