import sys
import time
'''
in java type

function add = function(a,b){
    return a+b;
}

function mutiply = function(a,b){
    return a*b;
}

function calc = function(num1,num2,callback){
    return callback(num1,num2);
};

console.log(calc(2,3,add))
'''
def add(a0,b0):
    return (a0+b0)

def mutiply(a0,b0):
    return (a0*b0)

def calc(a1,b1,callback):
    return (callback(a1,b1))



if __name__=="__main__":
    #print(mutiply(3,4))
    #print(calc(2,3,add))