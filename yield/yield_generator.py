#python3 only
def zipdemo():
    pretest = [5,7,4,8,10] 
    posttest= [6,7,5,10,9]
    z = zip(pretest,posttest)
    print(next(z)) # 5,6
    print("----------------")
    for i,j in z:
        print(i,j) #7 7 \n 4 5 \n 8 10 \n 10 9

zipdemo()  