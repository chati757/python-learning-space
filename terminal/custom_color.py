'''
...
║ 38       ║  Set foreground color          ║  Next arguments are `5;<n>` or `2;<r>;<g>;<b>`, see below               ║
║ 39       ║  Default foreground color      ║  implementation defined (according to standard)                         ║
║ 40–47    ║  Set background color          ║  See color table below                                                  ║
║ 48       ║  Set background color          ║  Next arguments are `5;<n>` or `2;<r>;<g>;<b>`, see below               ║
║ 49       ║  Default background color      ║  implementation defined (according to standard)                         ║
...
'''

import sys
import os 
os.system('cls')

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print('outloop')
    print(u"\u001b[0m")

test_str = 'rules'.ljust(6)
print(f'\u001b[48;5;200m {test_str}\u001b[0m')
print('sometxt')

#30; is txt color
#48;5; is std. of set_background_color
#94 is color of background
def therme_gray(id,txt):
    return f'\u001b[30;48;5;94m {txt} \u001b[30;48;5;0m {id} \u001b[0m'