#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
from multiprocessing import Process
processors = []
processor_num = 11
workQueue = Queue.Queue()
def single_processor(q,id):
while not workQueue.empty():
get_info(q.get(),id)
def get_info(data,processor_id):
for i in range(1000000):
a=str(processor_id)+data
def main():
for i in range(1000):
workQueue.put(str(i))
for i in range(processor_num):
p = Process(target=single_processor, args=(workQueue,i))
p.start()
processors.append(p)
for i in processors:
i.join()

if __name__ == '__main__':
main()