import logging

if __name__ == '__main__':
    #create core_logger instant
    #for logger
    core_logger = logging.getLogger("core")
    core_logger.setLevel(logging.DEBUG)

    core_format = logging.Formatter('%(name)s:%(levelname)s:%(asctime)s:%(funcName)s:%(lineno)d:%(message)s')
    
    core_file_handler_logger = logging.FileHandler('./log/core.log')
    core_file_handler_logger.setLevel(logging.INFO)
    core_file_handler_logger.setFormatter(core_format)
    
    core_file_handler_debugger = logging.FileHandler('./log/core_debug.log')
    core_file_handler_debugger.setLevel(logging.DEBUG)
    core_file_handler_debugger.setFormatter(core_format)

    core_logger.addHandler(core_file_handler_logger)
    core_logger.addHandler(core_file_handler_debugger)

    core_logger.debug("test debbug")
    core_logger.info("test info")
    core_logger.warning("test warning")