import csv

def normal_read_text_io():
    with open(r"./csv_testing.csv",newline="") as f: #r meaning raw text for except back slash
        data = f.read()
        print(data)

def read_csv():
    with open(r"./csv_testing.csv") as f:
        data = csv.reader(f,newline="")
        print("print type of data")
        print(type(data))
        print("print data")
        print(data)
        for row in data:
            #print(row)
            print("{:16}: {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],(int(row[1])+int(row[2])+int(row[3]))))

#csv custom seperator 
def read_csv_dat():
    with open(r"./csv_testing_dat.csv",newline="") as f:
        data = csv.reader(f,delimiter="-")
        print("print type of data")
        print(type(data))
        print("print data")
        print(data)
        for row in data:
            print(row)

#csv header
def read_csv_header_dict():
    with open(r"./csv_testing_header_dict.csv",newline="") as f:
        data = csv.DictReader(f)
        print("print data type")
        print(type(data))
        print("print data")
        print(data)
        print(data.fieldnames)
        for row in data:
            print(row)
            #print(row["country"],row["gold"])


if __name__ == "__main__":
    #normal_read_text_io()
    #read_csv()
    #read_csv_dat()
    read_csv_header_dict()