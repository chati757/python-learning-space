import os

def Main():
    pemfile_path = './test.pem'
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open(os.path.abspath(pemfile_path),"r")
    lines = f.read()
    clean_data = '\n'.join(lines.split('\\n'))
    print(clean_data)
    #print(''.join(lines[0].rstrip()))
    #print(''.join("\nMItest\n"))
    f.close()

if __name__=="__main__":
    Main()