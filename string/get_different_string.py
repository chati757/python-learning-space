import difflib

master = "http://www.brushlovers.com/"
content =["http://www.brushlovers.com/web/all-brushes/page/116","http://www.brushlovers.com/web/all-brushes/page/1"]

#**target want ot : web/all-brushes/page/
    #first cut http://www.brushlovers.com/ 
print(content[0].replace(master,"")) # web/all-brushes/page/116
#find max range
print("max range of str")
print(max(content,key=len))

cases=[('test', 'tesA')] 
difval=difflib.ndiff(cases[0][0],cases[0][1]) #result > difval=('  't,'  'e,'  's,-' 't,+' 'A)

print(','.join(difval))
for a,b in cases:
    print("first loop")
    print("a :"+a[0])
    print("b :"+b[0])
    for i,s in enumerate(difflib.ndiff(a,b)): #i is counter , s is string
        print("second loop")
        print("i :",i)
        print("s :",s)
        print("s[0]:",s[0])
        if(s[0]==' '):
            continue
        elif(s[0]=='-'):
            print("Delete",s[-1],"from position",i)
        elif(s[0]=='+'):
            print("Add",s[-1],"to position",i)    
    print()  