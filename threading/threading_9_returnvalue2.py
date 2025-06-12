def foo(bar, arg_result, index):
    print('hello {0}'.format(bar))
    arg_result[index] = "foo"

from threading import Thread

threads = [None] * 10
arg_results = [None] * 10

for i in range(len(threads)):
    threads[i] = Thread(target=foo, args=('world!', arg_results, i))
    threads[i].start()

# do some other stuff

for i in range(len(threads)):
    threads[i].join()

print(" ".join(arg_results))  # what sound does a metasyntactic locomotive make?