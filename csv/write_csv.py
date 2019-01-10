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

#custom dilimeter use like this : fw=csv.writer(f,delimiter="|")
#custom in quoting string only : fw=csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)

#append file
def append_write_csv():
    with open("csv_testing_writer.csv","a",newline="") as f:
        fw=csv.writer(f)
        fw.writerow(["three","four"])


if __name__=="__main__":
    #write_csv()
    #write_csv_th()
    #write_csv_multi_array()
    append_write_csv()