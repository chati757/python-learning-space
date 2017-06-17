'''
#concept in java
public class InstanceVariable {
    public int a;
    private int b;
    public void getNumber() {
        System.out.println( "a + b = " + (a + b) );
    }
    public void setNumber(int a2, int b2) {
        a = a2;
        b = b2;
    }
    public static void main(String args[]){
        InstanceVariable instance = new InstanceVariable();
        instance.setNumber(10, 30);
        instance.getNumber();
    }
}
'''

class InstanceVariable:
    versionval = 1
    def __init__(self):
        self.a = 0
        self.b = 0

    def getNumber(self):
        print("result:")
        print(self.a+self.b)
    
    def setNumber(self,test1,test2):
        self.a = test1
        self.b = test2

class inheritance_instance(InstanceVariable):
    inherclassa=2
    inherclassb=3
    
if __name__=="__main__":
    print("normal instance class")
    ins=InstanceVariable()
    ins.setNumber(2,5)
    ins.getNumber()

    print("inheritance instance class testing")
    inher=inheritance_instance()
    inher.setNumber(5,3)
    inher.getNumber()
    print(inher.a)
    print(inher.b)
    print(inher.inherclassa)
    print(inher.inherclassb)

    #override type function inclass "instanceVariable" with assign instance class
    print("override instance class testing")
    class overrideInstance(InstanceVariable):
        versionval = 2 #if change variable name it's goto master class [InstanceVariable] and get versionval form master class
        
    InstanceVariable=overrideInstance()
    print(InstanceVariable.versionval)
    