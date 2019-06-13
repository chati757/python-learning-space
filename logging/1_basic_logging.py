import logging

"""
Logging Level 

[10]DEBUG: Detailed infomation , typically of interest only when diagnosing problems.

[20]INFO: Confirmation that things are working as expected.

[30]WARNING: An indication that something unexpected hanppened , or indicative of some problem in the near future Ex. disk space low , the software is still working as expected.

[40]ERROR:Due to a more serious problem, the software has not been able to proform some function.

[50]CRITICAL:A serious error , indicating that the program itself may be unable to continue running.
"""

def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x,y):
    return x / y

if __name__ == "__main__":
    #default level logging is warnning , it's will be aleart in level warnning and higher

    #change default logging level with debug, change format
    #ref for change logging format : https://docs.python.org/3/library/logging.html#logrecord-attributes
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    num_1 = 10
    num_2 = 5

    add_result = add(num_1,num_2)
    logging.debug('add : {} + {} = {}'.format(num_1,num_2,add_result)) #DEBUG:root:add : 10 + 5 = 15
    logging.warning('add : {} + {} = {}'.format(num_1,num_2,add_result)) #WARNING:root:add : 10 + 5 = 15