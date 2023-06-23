#############       inheritance       ############


class B () :
    def do(self):
        print ('B')

class A(B):
    pass

class C ():
    def do (self):
        print ('C')

class D (A,C):
    pass


n = D ()
n.do()

# to find the path of the inheritance we can print : print (D.mro())
print (D.mro())
