import logging

class someInfoFilter(logging.Filter):

    def filter(self, record):
        print(record.levelno)
        
        return (record.levelno==30) #write warnning only

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    hdlr = logging.FileHandler("./log/testing.log")
    hdlr.setLevel(logging.INFO)

    hdlr2 = logging.StreamHandler()
    #hdlr.setLevel(logging.DEBUG)
    logger.addHandler(hdlr)
    logger.addFilter(someInfoFilter())

    logger.debug("test debug")
    logger.info("test info")
    logger.warning("test warnning")
    logger.exception("ERROR WILL ROBINSON")
    logger.error("error testing filter")
    logger.error("error2 testing filter")
    logger.info("test info 2")