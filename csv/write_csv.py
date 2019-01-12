import csv

def write_csv():
    with open("csv_testing_writer.csv","w",newline="") as f:
        fw=csv.writer(f)
        fw.writerow(["one","two"])

def write_csv_th():
    with open("csv_testing_writer_th.csv","w",newline="",encoding="utf8") as f:
        fw=csv.writer(f)
        fw.writerow(["ทดสอบ","ภาษาไทย"])

#write multi-dimension
def write_csv_multi_array():
    menus=[
        ["test01",50],
        ["test02",80],
        ["test03",10]
    ]
    with open("csv_testing_writer_multi_array.csv","w",newline="") as f:
        fw=csv.writer(f)
        fw.writerows(menus)

def write_dict_csv(file_path,dict_data):
    csv_columns = dict_data[0].keys()
    try:
        with open(file_path,'w',newline="") as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=csv_columns)
            w.writeheader()
            for data in dict_data[1:]:
                w.writerow(data)
        csvfile.close()

    except IOError:
        print("I/O error") 

#custom dilimeter use like this : fw=csv.writer(f,delimiter="|")
#custom in quoting string only : fw=csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)

#append file
def append_write_csv():
    with open("csv_testing_writer.csv","a",newline="") as f:
        fw=csv.writer(f)
        fw.writerow(["three","four"])

#update config csv
def update_config_csv(file_path,config_name,config_value):
    search_lines = None
    with open(file_path, 'r',newline="") as readFile:
        reader = csv.reader(readFile)
        search_lines = list(reader)

    readFile.close()
    #print(search_lines) #[['python_IsActive', 'request_update_data_status'], ['true', 'updated']]
    
    match_position = None
    for c,lines in enumerate(search_lines[0]):
        if(lines==config_name):
            match_position=c

    if(match_position!=None):
        with open(file_path, 'w',newline="") as writeFile:
            writer = csv.writer(writeFile)
            search_lines[1][match_position]=config_value
            writer.writerows(search_lines)
        writeFile.close()
    else:
        print("config_name : not found")
    '''
    with open(file_path, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    writeFile.close()
    '''


if __name__=="__main__":
    #write_csv()
    #write_csv_th()
    #write_csv_multi_array()
    #append_write_csv()
    test = [{'test':'testa','testv':'teste'},{'test':'testvv','testv':'e'}]
    write_dict_csv("csv_testing_write_dict.csv",test)