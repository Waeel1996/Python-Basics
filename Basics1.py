# some Basics instructions on how to start with Python

#cods I need to remember
#if and else

x=5
if x<4:
    print(x)
else:
    print('unknown')

#loop :

x=1
while x<=5:
    y=1
    while y<=10:
        print (f'{x} X {y} = {x*y}')
        y+=1
        
    x+=1
    print('--------------------')

#Nested loop (for)

for x in range (1,11):
    for y in range (1,11):
        print (f'{x} X {y} = {x*y}')
    print('--------------------')

#all and any
#instade of typing many ands OR ors, you can use all for many ands, and any for many ors
x=5
y=2
z=6

#if x==5 and y==2 and z==6:
    #print (' welcome ')
if all([x==5 , y==2 , z==6]):
    print (' welcome ')

#if x==5 or y==2 or z==6:
    #print (' welcome ')

if any([x==5 , y==2 , z==6]):
     print (' unwelcome ')
