#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
from multiprocessing import Process

processors_arg = []
processor_num = 11
workQueue = queue.Queue()

def get_info(data,processor_id):
    for i in range(1000000):
        a=str(processor_id)+data

def single_processor(q,id):
    while not workQueue.empty():
        get_info(q.get(),id)

def main():
    for i in range(1000):
        workQueue.put(str(i))

    for i in range(processor_num):
        p = Process(target=single_processor, args=(workQueue,i))
        p.start()
        processors_arg.append(p)

    for i in processors_arg:
        i.join()

if __name__ == '__main__':
    main()