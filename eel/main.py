import pandas as pd
import eel

#function for java state


#------------------------------------

#test dataframe
df = pd.DataFrame({'stock':['ptt','bcp'],'sector':['energy','energy'],'grade':['a','c'],'hlfc':['4','2'],'rsi10':['33.234','30.955'],'rsi_wtb':['6:w.4-5:t.3:tp.2-4(lower)','6:w.4-5:t.3:tp.2-4(lower)'],'inv_harami_pattern':['TRUE','FALSE'],'double_pattern':['FALSE','TRUE']})

eel.init("web")
eel.start("main.html",block=False)
#calculate rsi10 set100 and get rsi10_val and rsi10_level
#eel.update_set100_rsi10(rsi10_val,rsi10_level)
eel.fetch_table_data(df.to_json(orient="values"))
eel.update_highlight_hlfc()
eel.update_highlight_inv_harami_pattern()
eel.update_highlight_double_pattern()
while True:
    print('active')
    eel.sleep(10)