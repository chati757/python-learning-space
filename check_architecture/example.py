#aviliable linux and window

"""
$ python-32 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
('7fffffff', False)
$ python-64 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
('7fffffffffffffff', True)
"""

import sys
print("%x" % sys.maxsize, sys.maxsize > 2**32)