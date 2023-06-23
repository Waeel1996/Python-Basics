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
# in our case, the super or the bais class is B because the code stoped on B when it found the "do" in it

######## EX :

'''
create student
add marks
get avg

'''
class Student ():
    #def create_student (self,name): or we can add a constructor and delet the
    #object by defining the "self" s1.creat_student(''Wael)
    def __init__(self,name):
        print (f'Welcome {name}')

#class marks

s1 = Student('Wael')
#s1.create_student ('Wael')
