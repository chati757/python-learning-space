import multiprocessing
import time


# Create a function to run in the subprocess
def subprocess_function(conn,name):
  # Receive data from the pipe
    data = conn.recv()
    if(data!=None):
        print(f'{name} Received data in subprocess: {data}')

if __name__ == '__main__':
    # Create a pipe with two endpoints
    parent_conn, child_conn = multiprocessing.Pipe()
    # Create the subprocess and pass it the connection
    p1 = multiprocessing.Process(target=subprocess_function, args=(child_conn,'sub1',),daemon=True)
    p2 = multiprocessing.Process(target=subprocess_function, args=(child_conn,'sub2',),daemon=True)

    # Start the subprocesses
    p1.start()
    p2.start()

    time.sleep(5)
    num_subprocesses = len(multiprocessing.active_children())
    print(f'Number of subprocesses: {num_subprocesses}')

    # Send data through the pipe
    for i in range(0,len(multiprocessing.active_children())):
        parent_conn.send('Hello from the main process!')
    #parent_conn.send('Hello from the main process!')

    # Wait for the subprocesses to finish
    p1.join()
    p2.join()

    print('after join')
    time.sleep(10)