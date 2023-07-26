import multiprocessing
import time


# Create a function to run in the subprocess
def subprocess_function(e,name):
  # Receive data from the pipe
    e.wait()
    print(f'{name} received')
    print(e.is_set())


if __name__ == '__main__':
    # Create a pipe with two endpoints
    e = multiprocessing.Event()
    # Create the subprocess and pass it the connection
    p1 = multiprocessing.Process(target=subprocess_function, args=(e,'sub1',),daemon=True)
    p2 = multiprocessing.Process(target=subprocess_function, args=(e,'sub2',),daemon=True)

    # Start the subprocesses
    p1.start()
    p2.start()

    time.sleep(5)
    num_subprocesses = len(multiprocessing.active_children())
    print(f'Number of subprocesses: {num_subprocesses}')

    print('set event')
    e.set()

    # Wait for the subprocesses to finish
    p1.join()
    p2.join()

    print('after join')
    time.sleep(5)