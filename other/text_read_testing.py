#-*-coding: utf-8 -*-

#-----------------path setting----------------
#pathset="P:/path_console/log_th_acg01.txt"
pathset="C:/Users/lenovo/Desktop/log_th.txt"
#---------------------------------------------
#-----------------log debug-------------------
log_show=False
#set False it'mean not show
#---------------------------------------------
testchar=""
trans_array=[["1","ๅ"],["2","/"],["3","-"],["4","ภ"],["5","ถ"],["6","ุ"],["7","ึ"],["8","ค"],["9","ต"],["0","จ"],["-","ข"],["=","ช"]
    ,["q","ๆ"],["w","ไ"],["e","ำ"],["r","พ"],["t","ะ"],["y","ั"],["u","ี"],["i","ร"],["o","น"],["p","ย"],["[","บ"],["]","ล"],["\\","ฃ"]
    ,["a","ฟ"],["s","ห"],["d","ก"],["f","ด"],["g","เ"],["h","้"],["j","่"],["k","า"],["l","ส"],[";","ว"],["'","ง"]
    ,["z","ผ"],["x","ป"],["c","แ"],["v","อ"],["b","ิ"],["n","ื"],["m","ท"],[",","ม"],[".","ใ"],["/","ฝ"]
    ,["!","+"],["@","๑"],["#","๒"],["$","๓"],["%","๔"],["^","ู"],["&","฿"],["*","๕"],["(","๖"],[")","๗"],["_","๘"],["+","๙"]
    ,["Q","๐"],["W","\""],["E","ฎ"],["R","ฑ"],["T","ธ"],["Y","ํ"],["U","๊"],["I","ณ"],["O","ฯ"],["P","ญ"],["{","ฐ"],["}",","],["|","ฅ"]
    ,["A","ฤ"],["S","ฆ"],["D","ฏ"],["F","โ"],["G","ฌ"],["H","็"],["J","๋"],["K","ษ"],["L","ศ"],[":","ซ"],["\"","."]
    ,["Z","("],["X",")"],["C","ฉ"],["V","ฮ"],["B","ฺ"],["N","์"],["M","?"],["<","ฒ"],[">","ฬ"],["?","ฦ"]]

count=-1

def translate_lang():
    global testchar,trans_array,test_array,count,pathset
    f = open(pathset,"r")
    lines = f.readlines()
    for line in lines:
        set_log(line)
        if(count!=-1):
            testchar+="\n"
        if((line=="<CHANGE TH>\n")):
            testchar+="<CHANGE TH>\n"
            continue
        if((line=="<ENTER>\n")):
            testchar+="<ENTER>\n"
            continue
        if((line=="<TAB>\n")):
            testchar+="<TAB>\n"
            continue
        if((line=="<BACK SPACE>\n")):
            testchar+="<BACK SPACE>\n"
            continue
        count=-1
        for txt in line:
            set_log(("txt>",len(line)-1,txt))
            #testchar+=txt.replace('l','ส').replace(';','ว').replace('f','ด').replace('u','ี').replace('y','ั')
            for checkch in trans_array:
                #print(count)
                if(txt==checkch[0] and (count<(len(line)-1))):
                    count=count+1
                    set_log(("replace count",count))
                    testchar+=txt.replace(checkch[0],checkch[1])
    f.close()
    print(testchar)

def write_replace():
    global pathset,testchar
    f = open(pathset,"w")
    f.write(testchar)
    f.close()

def set_log(msg):
    global log_show
    if(log_show==True):
        print(msg)
        
if __name__=="__main__":
    translate_lang()
    write_replace()