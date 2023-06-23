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
class Student:
    #def create_student (self,name): or we can add a constructor and delet the
    #object by defining the "self" s1.creat_student(''Wael)
    def __init__(self,name):
        print (f'Welcome {name}')
        self.marks=[]
        print('')
    def add_mark (self,mark):
        self.marks.append(mark)
        print (self.marks)
        print('')
    def avg (self):
        avg = sum(self.marks)/len(self.marks)
        print(avg)
s1 = Student('Wael')
#s1.create_student ('Wael')
s1.add_mark (20)
s1.add_mark (30)
s1.add_mark (40)
s1.add_mark (50)
s1.add_mark (60)

s2 = Student('Ahmad')
s2.add_mark (40)
s2.add_mark (50)
s2.add_mark (60)
s2.add_mark (70)
s2.add_mark (80)
s2.add_mark (90)

######### EX:

class User :
    def __init__(self,name,age,gender):
            print(f'Welcome {name}')
            self.balance=0
        
class Bank(User):
    def __init__(self,name,age,gender):
        print(f'Welcome {name}')
        self.balance=0
    
    def deposite (self,amount):
        self.balance += amount
        print(f'your current balance : {self.balance}')
    def withdraw (self,amount):
        if amount > self.balance :
            print (f'your balance is not enough')
            return
        self.balance -=amount
        print (f'you have just withdrawed : {amount}')
    def view_balance(self):
        print(f'your current balance : {self.balance}')
        
u1= Bank('Wael',26,'male')
u1.deposite(600)
u1.withdraw(100)
u1.view_balance()
