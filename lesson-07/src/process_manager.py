#! /usr/bin/env python3

import time
import multiprocessing as mp


def update_data(data):
    print(f"[Process] data before", data)
    data['qwerty'] = 100500
    data['str'] = [1,2,3]
    print(f"[Process] data after", data)

def main():
    data = {}
    print("before", data)
    pr = mp.Process(target=update_data, args=(data,))
    pr.start()
    pr.join()
    print("after", data)

    print("========================")
    with mp.Manager() as manager:
        data = manager.dict()
        print("before", data)
        pr = mp.Process(target=update_data, args=(data,))
        pr.start()
        pr.join()
        print("after", data, data['qwerty'])

if __name__ == "__main__":
    main()
