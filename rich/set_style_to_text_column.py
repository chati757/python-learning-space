import math
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from rich.text import Text
from rich.align import Align

style_target = [['a','white on red'],['c','red'],['e','grey0 on yellow1']]

data_list = [
    {
        'a':'qwerty',
        'b':'zxcvbn',
        'c':'ertyui'
    },
    {
        'd':'rtyui',
        'e':'cvbhg',
        'f':'yhnuj'
    }
]

console = Console()
for obj in data_list:
    spans_style = []

    key_str = ('\n'.join(list(obj.keys())))
    value_str = ('\n').join(list(obj.values()))

    key_and_style_mapping_list = [i for i in style_target if(i[0] in key_str)]
    key_mapping_list,style_mapping_list = zip(*key_and_style_mapping_list) #['a','b'] , ['c','d']
    key_mapping_list = list(key_mapping_list) #['a','c']
    style_mapping_list = list(style_mapping_list) #['b','d']
    value_mapping_list = [obj[i] for i in key_mapping_list]

    spans_style_list = []
    for c,i in enumerate(value_mapping_list):
        index_start_buff = value_str.index(i)
        spans_style_list.append((index_start_buff,index_start_buff+len(i),style_mapping_list[c]))
    #start_pos_value
    #end_pos_value

    key_txt =  Text(key_str)
    value_txt = Text(value_str,spans=spans_style_list)

    console.print(Columns([key_txt,value_txt]))
    print('---')