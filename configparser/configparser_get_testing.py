#ref:https://docs.python.org/3/library/configparser.html
import configparser

config = configparser.RawConfigParser()
config.read('test.txt')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
a_float = config.getfloat('page_status', 'a_float')
an_int = config.getint('page_status', 'an_int')
print(a_float)
print(an_int)

print(config.get('page_status','an_int').isnumeric())