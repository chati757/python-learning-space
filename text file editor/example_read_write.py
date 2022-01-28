buff_arr = []
buff_arr_score = []
buff_len = None

def update_record(name,score):
    try :
        fr = open("record.txt","r")
        data = fr.read()
        data += name+','+str(score)+'\n'
        #sorted sd,2\nss,7 -> ss,7\nsd,2 
        unsorted_data = [float(i.split(',')[1]) for i in data.split('\n') if(i!='')]
        sorted_data = unsorted_data.copy()
        sorted_data.sort(reverse=True)
        data = data.split('\n')
        sorted_data = [j+'\n' for j in [data[unsorted_data.index(j)] for j in sorted_data]]
        fw = open("record.txt","w")
        fw.write("".join(sorted_data))
        fw.close()
        fr.close()
    except FileNotFoundError:
        fw = open("record.txt","w")
        fw.write(name+','+str(score)+'\n')
        fw.close()

while True:
    try :
        fr = open("record.txt","r")
        buff_len = len(fr.read().split('\n'))
        fr.close()
    except FileNotFoundError:
        buff_len = 1

    if(buff_len>10):
        print('record : 10/10')
        break

    name = input(f"please insert name : ({buff_len}/10) : ")
    score = float(input('please insert score : '))
    update_record(name,score)
    buff_len+=1