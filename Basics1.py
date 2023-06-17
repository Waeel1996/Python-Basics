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
#instade of typing many "and" OR "or", you can use "all" for many "and"
#and "any" for many "or"
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


#true condition false
#instade of typing :
     #if any([x==5 , y==2 , z==6]):
     #print (' unwelcome ')
#you can just reverse it to give the true Type and then the condition you want :
print (' unwelcome ') if any([x==3 , y==1 , z==5]) else print ('False condition')
     
