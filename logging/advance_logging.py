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
    try:
        result = x / y
    except ZeroDivisionError:
        #main_logger.error('ZeroDivisonError') # it'will be show message only in advance_testng.log
        #if you need to throw error and message 
        main_logger.exception('ZeroDivisonError')
    else:
        return result

if __name__ == "__main__":
    #default level logging is warnning , it's will be aleart in level warnning and higher

    #create main logging instant
    main_logger = logging.getLogger("main")

    main_formatter_logger = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s') #create logging format instant
    main_file_handler_logger = logging.FileHandler('advance_testing.log') #create logging file handler instant
    #set logging format in file_handler instant
    main_file_handler_logger.setFormatter(main_formatter_logger)

    #set logging level
    main_logger.setLevel(logging.INFO)

    #set logging file handler
    main_logger.addHandler(main_file_handler_logger)

    num_1 = 10
    num_2 = 0

    add_result = devide(num_1,num_2)
    #logging.debug('add : {} + {} = {}'.format(num_1,num_2,add_result)) #DEBUG:root:add : 10 + 5 = 15
    #logging.warning('add : {} + {} = {}'.format(num_1,num_2,add_result)) #WARNING:root:add : 10 + 5 = 15
    add_result = add(num_1,num_2)
    main_logger.info('add : {} + {} = {}'.format(num_1,num_2,add_result)) #DEBUG:root:add : 10 + 5 = 15
    main_logger.info('add : {} + {} = {}'.format(num_1,num_2,add_result)) #WARNING:root:add : 10 + 5 = 15