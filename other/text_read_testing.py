#-*-coding: utf-8 -*-

testchar=""
trans_array=[["1","ๅ"],["2","/"],["3","-"],["4","ภ"],["5","ถ"],["6","ุ"],["7","ึ"],["8","ค"],["9","ต"],["0","จ"],["-","ข"],["=","ช"]
    ,["q","ๆ"],["w","ไ"],["e","ำ"],["r","พ"],["t","ะ"],["y","ั"],["u","ี"],["i","ร"],["o","น"],["p","ย"],["[","บ"],["]","ล"],["\\","ฃ"]
    ,["a","ฟ"],["s","ห"],["d","ก"],["f","ด"],["g","เ"],["h","้"],["j","่"],["k","า"],["l","ส"],[";","ว"],["'","ง"]
    ,["z","ผ"],["x","ป"],["c","แ"],["v","อ"],["b","ิ"],["n","ื"],["m","ท"],[",","ม"],[".","ใ"],["/","ฝ"]
    ,["!","+"],["@","๑"],["#","๒"],["$","๓"],["%","๔"],["^","ู"],["&","฿"],["*","๕"],["(","๖"],[")","๗"],["_","๘"],["+","๙"]
    ,["Q","๐"],["W","\""],["E","ฎ"],["R","ฑ"],["T","ธ"],["Y","ํ"],["U","๊"],["I","ณ"],["O","ฯ"],["P","ญ"],["{","ฐ"],["}",","],["|","ฅ"]
    ,["A","ฤ"],["S","ฆ"],["D","ฏ"],["F","โ"],["G","ฌ"],["H","็"],["J","๋"],["K","ษ"],["L","ศ"],[":","ซ"],["\"","."]
    ,["Z","("],["X",")"],["C","ฉ"],["V","ฮ"],["B","ฺ"],["N","์"],["M","?"],["<","ฒ"],[">","ฬ"],["?","ฦ"]]

test_array=[["l","ส"],[";","ว"],["y","ั"],["u","ี"],["f","ด"]]
count=-1

def Main():
    global testchar,trans_array,test_array,count
    f = open("C:/Users/lenovo/Desktop/log_th.txt","r")
    lines = f.readlines()
    for line in lines:
        print(line)
        if(count!=-1):
            testchar+="\n"
        count=-1
        for txt in line:
            print("txt>",len(line)-1,txt)
            #testchar+=txt.replace('l','ส').replace(';','ว').replace('f','ด').replace('u','ี').replace('y','ั')
            for checkch in trans_array:
                #print(count)
                if(txt==checkch[0] and (count<(len(line)-1))):
                    count=count+1
                    print("replace count",count)
                    testchar+=txt.replace(checkch[0],checkch[1])
    f.close()
    print(testchar)
    #testtxt="l;ylfu"
    #print(testtxt.decode("utf-8").replace('l',u'ส').replace(';',u'ว').replace('f',u'ด').replace('u',u'ี').replace('y',u'ั'))
    
def translate_lang():
    print(len(trans_array))
    #for checkar in test_array:
    #    print(checkar[0])
    #    print(checkar[1])
    
    
if __name__=="__main__":
    Main()
    translate_lang()