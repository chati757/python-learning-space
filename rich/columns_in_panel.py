import pandas as pd
import time
import random
from rich import print
from rich.table import Table
from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.padding import Padding
from rich.layout import Layout
from rich.text import Text
from rich.live import Live
from rich.console import Console
from rich.columns import Columns

topic = Padding(Align.center('COLUMNS IN PANEL'),(0,1),style="bright_white on blue", expand=True)
gap = Padding(Align.center(' '),(0,1), expand=True)

console = Console()
console.print(topic)
console.print(gap)

indicator_topic_list = [
    'DVD.LEFT',
    'R.LEFT',
    'PRICE',
    'BB50_M',
    'BB50_W',
    'BB50_D',
    'RSI10_D',
    'BB20_D',
    'BB50_D_STDU ',
    'BB50_D_RZ',
    'TDS_D',
    'OGP_D'
    ]

indicator_result_list = [
    '123',
    '321',
    '123.23',
    '123.23',
    '123.23',
    '23.23',
    '123.33',
    '23.23',
    '23.23',
    '23.23',
    '23',
    'FALSE'
]

indicator_topic_columns = "\n".join(indicator_topic_list)
indicator_result_columns = Text("\n".join(indicator_result_list),justify='right')
indicator_panel = Panel(Columns([indicator_topic_columns,indicator_result_columns]),expand=True,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel.width = 23
indicator_panel.height = len(indicator_result_list)+2

symbol_panel_columns = Columns([indicator_panel,indicator_panel,indicator_panel])
console.print(Panel(symbol_panel_columns,title='SYMBOL',title_align='center',height=len(indicator_result_list)+4))

topic2 = Padding(Align.center('LAYOUY IN PANEL'),(0,1),style="bright_white on red", expand=True)
console.print(topic2)
console.print(gap)

indicator_panel21 = Panel(Columns([indicator_topic_columns,indicator_result_columns]),expand=False,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel21.width = 23
indicator_panel21.height = len(indicator_result_list)+2

indicator_panel22 = Panel(Columns([indicator_topic_columns,indicator_result_columns],width=16,expand=False),expand=False,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel22.width = 39
indicator_panel22.height = len(indicator_result_list)+2

indicator_panel23 = Panel(Columns([indicator_topic_columns,indicator_result_columns]),expand=False,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel23.width = 23
indicator_panel23.height = len(indicator_result_list)+2

layout = Layout(name='panel_layout')
layout.split_row(
    Align.left(indicator_panel21),
    Align.left(indicator_panel22),
    Align.left(indicator_panel23)
)
console.print(Panel(layout,title='SYMBOL',title_align='center',height=len(indicator_result_list)+4))

topic3 = Padding(Align.center('COLUMNS IN PANEL DYNAMIC'),(0,1),style="bright_white on blue", expand=True)
gap3 = Padding(Align.center(' '),(0,1), expand=True)
console.print(topic3)
console.print(gap3)

indicator_topic_list3 = [
    'DVD.LEFT',
    'R.LEFT',
    'PRICE',
    'BB50_M',
    'BB50_W',
    'BB50_D',
    'RSI10_D',
    'BB20_D',
    'BB50_D_STDU ',
    'BB50_D_RZ',
    'TDS_D',
    'OGP_D'
    ]

indicator_result_list3 = [
    '123',
    '321',
    '123.23',
    '123.23',
    '123.23',
    '23.23',
    '123.33',
    '23.23',
    '23.23',
    '23.23',
    '23',
    'FALSE'
]

indicator_topic_columns31 = "\n".join(indicator_topic_list3)
indicator_result_columns31 = Text("\n".join(indicator_result_list3),justify='right')
indicator_panel31 = Panel(Columns([indicator_topic_columns31,indicator_result_columns31]),expand=True,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel31.width = 23
indicator_panel31.height = len(indicator_result_list3)+2

indicator_topic_columns32 = "\n".join(indicator_topic_list3)
indicator_result_columns32 = Text("\n".join(indicator_result_list3),justify='right')
indicator_panel32 = Panel(Columns([indicator_topic_columns32,indicator_result_columns32],width=15,expand=True),expand=True,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel32.width = 36
indicator_panel32.height = len(indicator_result_list3)+2

indicator_topic_columns33 = "\n".join(indicator_topic_list3)
indicator_result_columns33 = Text("\n".join(indicator_result_list3),justify='right')
indicator_panel33 = Panel(Columns([indicator_topic_columns33,indicator_result_columns33]),expand=True,title='INDICATOR',title_align='left',border_style='khaki1')
indicator_panel33.width = 23
indicator_panel33.height = len(indicator_result_list3)+2

symbol_panel_columns3 = Columns([indicator_panel31,indicator_panel32,indicator_panel33])
console.print(Panel(symbol_panel_columns3,title='SYMBOL',title_align='center',height=len(indicator_result_list3)+4))
