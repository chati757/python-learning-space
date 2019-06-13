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
    main_logger.setLevel(logging.INFO)

    main_logger_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    main_logger_handler = logging.StreamHandler(stream=None)

    main_logger_handler.setFormatter(main_logger_formatter)

    main_logger.addHandler(main_logger_handler)

    main_logger.info("test")