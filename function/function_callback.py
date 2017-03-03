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
def add(a,b):
    return (a+b)

def mutiply(a,b):
    return (a*b)

def calc(a,b,callback):
    return (callback(a,b))
    
if __name__=="__main__":
    #print(mutiply(3,4))
    print(calc(2,3,add))