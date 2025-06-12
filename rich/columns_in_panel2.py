import math
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from rich.text import Text
from rich.align import Align

data = [
    {
        'INDICATOR':'',
        'DVD.LEFT':'123',#intraday-calc
        'R.LEFT':'321',#intraday-calc
        'PRICE':'123.23',
        'BB50_W':'123.23',#(trigger)
        'BB50_D':'123.23',#(trigger)
        'RSI10_D':'23.23',
        'BB20_D':'23.23',
        'BB50_D_STDU':'23.23',
        'BB50_D_RUZ':'23.23',
        'BB50_D_RDZ':'23.23',
        'TDS_D':'3',
        'OGP_D':'FALSE'#(trigger)
    },
    {
        'FUNDAMENTAL':'',
        'PRICE_SPREAD':'0.233',
        'DVD.Y(%)':'23.23',
        'FREE-FLOAT(%)':'12.23',#one-time
        'EPS':'12.23',#intraday-calc (trigger if change)
        'AVG-VALUE(10)':'100000K',#intraday-calc
        'ST-CONS':[216.25,127.25],#one-time,intraday-calc
        'ST-CONS-AVG':'123.23',#one-time,intraday-calc (trigger if >= lastprice)
        'ST-CONS-MOS':'123.23',#one-time,intraday-calc
        'BD-CONS':['2024-03-01','2024-03-01','2024-05-02']#one-time,#intraday-calc
    },
    {
        'SHORT_DETAIL':'',
        'ASP_SBL_VALUE':'99999999',#intraday-calc
        'NET_SO':'99999999',#net_short_outstanding
        'NET_SO_NVDR':'99999999',#net_short_outstanding_nvrd
        'SHORT_PAIDUP':'99999999',#short_paidup
        'TOTAL_SO(%)':'99999999',#total_short_outstanding_percent
        'UNNOWN6':'NO-DATA',
        'UNNOWN7':'NO-DATA',
        'UNNOWN8':'NO-DATA',
        'UNNOWN9':'NO-DATA',
        'UNNOWN10':'NO-DATA',
        'UNNOWN11':'NO-DATA',
        'UNNOWN12':'NO-DATA'
    },
    {
        'SHORT_DESCRIPTOR':'',
        'S.SWING':'3.871',#เราจะใช้ค่า S.SWING *2 เพื่อหา simple
        'A.SIMPLE_NUM':'7.742',#จำนวนตัวอย่างที่เข้าหลักเกณฑ์ S.SWING *2
        'A.SIMPLE_STD':'12.34',#ค่าเบี่ยงเบนของค่าเฉลี่ยมีมากหรือไม่ ถ้ามาก การที่ใช้ AVG มาพิจารณาจะไม่น่าเชื่อถือ
        'A.SWING_AVG':'12.34',#แท่งที่สร้างแรงซื้อผิดปกติ(แท่งเขียวยาว) โดยเฉลี่ยแล้วมี s.swing อยู่ประมาณเท่าไร
        'A.CHG_AVG':'5.6 %',#ค่าเฉลี่ยแท่งที่สร้างแรงซื้อผิดปกติ(แท่งเขียวยาว)(นับจาก open ถึงจุดสูงสุด และคำนวณ chg. ออกมา)
        'A.H.HIGH_M.AVG_VOL':'123.23K',#ปริมาณ match order เฉลี่ยของจุดสูงสุดของวันที่เคยบันทึก (เราจะนับเมื่อแตะ high และนับจนกว่า high-1 จะอยู่ offer)
        'A.MIN_VAL_AT_HIGH':'123.23K',#VAL น้อยสุดของ simple ที่สูงสุดของวัน (ใช้เป็นสัญญาณเฝ้าจับตาความผิดปกติที่อาจจะเริ่มเกิดขึ้น)
        'A.HIGH_INTERVAL.':'02:00',#เวลาที่อยู่ในจุดสูงสุดเป็นเวลาทั้งหมดเท่าไรก่อนปรับตัวลงมา (หมายถึงช่วงที่ high-1 เป็น bid และ high เป็น offer)
        'A.TIME_ATH.':'12:00',#เวลา ณ จุดสูงสุดตอนนั้นเวลากี่โมง (เมื่อราคาแตะจุดสูงสุดตอนนั้นเวลากี่โมง)
    }
]

def reform_obj(data_obj:dict,indent:list):
    #indent = [[<key>,<indent_pos>],...]
    result_obj = data_obj
    reform_list = []

    for d_list in indent:
        indent_list = result_obj[d_list[0]]
        devide_num = math.ceil(len(indent_list)/d_list[1])+1
        get_pos_list_by_indent_list = [i*d_list[1] for i in range(0,devide_num)]
        for i in range(1,devide_num):
            reform_list.append(indent_list[get_pos_list_by_indent_list[i-1]:get_pos_list_by_indent_list[i]])
        
        target_index = list(result_obj.keys()).index(d_list[0])
        se_buff_origin = pd.Series(result_obj)
        se_buff_mod = se_buff_origin.copy()[:(target_index+1)]
        for c,i in enumerate(reform_list):
            if(c==0):
                se_buff_mod[d_list[0]] = i
            else:
                if(c%2==0):
                    se_buff_mod[str(reform_list[c-1])] = str(i)
                else:
                    se_buff_mod[str(i)] = ''

        reform_list = []
        result_obj = pd.concat([se_buff_mod,se_buff_origin[(target_index+1):]]).to_dict()

    return result_obj

'''
data = [{},{}]
highlight = [
        [<key>,<style>],..
    ]
'''
def columns_panel(data_obj_list,topic:str,highlight_list:list):
    panel_data_arr = []
    max_height_data_obj = max([len(i.keys()) for i in data_obj_list])
    for c,data_obj in enumerate(data_obj_list):
        data_keys_list = list(data_obj.keys())[1:]
        data_values_list = [str(i) for i in list(data_obj.values())[1:]]
        max_key_value_width = max([len(i) for i in data_values_list]) + max([len(i) for i in data_keys_list])

        sub_topic_data = '\n'.join(data_keys_list)
        sub_content_data = '\n'.join(data_values_list)

        spans_style_list = []
        try:
            key_and_style_mapping_list = [i for i in highlight_list if(i[0] in sub_topic_data)]
            key_mapping_list,style_mapping_list = zip(*key_and_style_mapping_list)
            key_mapping_list = list(key_mapping_list)
            style_mapping_list = list(style_mapping_list)
            value_mapping_list = [data_obj[i] for i in key_mapping_list]
            indent_mapping_list = [c for c,i in enumerate(sub_content_data) if(i=='\n')]

            index_start_buff = 0
            for c,i in enumerate(value_mapping_list):
                if(index_start_buff==0):
                    index_start_buff = sub_content_data.index(i)
                else:
                    index_start_buff = sub_content_data.index(i,index_start_buff+indent_mapping_list[c]+1)

                spans_style_list.append((index_start_buff,(index_start_buff+len(i)),style_mapping_list[c]))
        except:
            pass
        
        sub_topic = Text(sub_topic_data,justify='left')
        sub_content = Text(sub_content_data,justify='right',spans=spans_style_list)

        columns = Columns([sub_topic,sub_content])
        panel_data_arr.append(Panel(columns,title=list(data_obj.keys())[0],title_align='left',expand=False,height=max_height_data_obj,width=max_key_value_width+5))
    
    return Panel(Align(Columns(panel_data_arr),align='center'),title=topic)

if __name__=='__main__':
    console = Console()

    '''
    'PRICE':'123.23',
    'BB50_W':'123.23',#(trigger)
    'BB50_D':'123.23',#(trigger)
    'RSI10_D':'23.23',
    'BB20_D':'23.23',
    'BB50_D_STDU':'23.23',
    'BB50_D_RUZ':'23.23',
    'BB50_D_RDZ':'23.23',
    'TDS_D':'3'

    FREE-FLOAT(%)
    '''

    highlight_list = [['BB50_W','white on red'],['BB50_D','grey0 on yellow1'],['BB50_D_RUZ','white on red']]
    data[1] = reform_obj(data[1],[['ST-CONS',2],['BD-CONS',1]])
    console.print(columns_panel(data,'SOME_SYMBOL',highlight_list))

    import pdb;pdb.set_trace()