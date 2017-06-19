#ref:https://docs.python.org/3/library/configparser.html
import configparser

config = configparser.RawConfigParser()

config.add_section('page_status')
config.set('page_status', 'an_int', '15')
config.set('page_status', 'a_bool', 'true')
config.set('page_status', 'a_float', '3.1415')
config.set('page_status', 'baz', 'fun')
config.set('page_status', 'bar', 'Python')
config.set('page_status', 'foo', '%(bar)s is %(baz)s!')


# Writing our configuration file to 'example.cfg'
with open('E:/project w/clicker bot/bot/log_page.txt','w') as configfile:
    config.write(configfile)