#! /usr/bin/env python3

import time
import multiprocessing

N = 50_000_000
N_PROC = 2

def countdown(n):
    while n > 0:
        n -= 1

def main():

    start_ts = time.time()
    for _ in range(N_PROC):
        countdown(N)

    end_ts = time.time()
    print(f"Time of sync execution is {end_ts - start_ts}")

    start_ts = time.time()
    with multiprocessing.Pool(N_PROC) as p:
        for _ in range(N_PROC):
            response = p.apply_async(countdown, (N,))
            print(type(response))
            print(dir(response))
            print(response.successful())
        p.close()
        p.join()
    end_ts = time.time()
    print(f"Time of sync execution is {end_ts - start_ts}")

if __name__ == '__main__':
    main()
