######## format str functions: ##########



#exp:
s='welcome'
s="welcome"
s='''welcome'''
f_name = 'ahmad'
l_name = 'ali'
print (f"{f_name} {l_name}")

#\n to jump down a line

print('ahmad \nwael')

#\t to leave a space:

print('mahmod \twael')

#some of text funktions

text = 'my name is wael'
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace('is','was')) #to replace words
print(text.split(','))
print(text.split(' '))

#indexing :

text = 'my name is wael'
print(text[0])
print(text[-1])
print(text[-2])

#slicing

print(text[0:6])
print(text[:6])
print(text[6:0])

######## list functions: ##########

l = [1,2,3,True,'welcome']

#slicing and indexing can also be used with lisitng
#we can also replcae some of the itmes inside the liste using indexing

l[0]=100
print(l[0])
#100
print(l)
#[100, 2, 3, True, 'welcome']

#to add an itme to the list we can use "append"

l.append(1000)
print(l)
[100, 2, 3, True, 'welcome', 1000] #it will be added as a last itme in the list

#we can aslo use "insert" to add an item in a specific place :

l.insert(0,200)
print(l)
#[200, 100, 2, 3, True, 'welcome', 1000]

#to remove an itme we can use "remove" by naming the item we need to delete :

l.remove(200)
print(l)
#[100, 2, 3, True, 'welcome', 1000]

#we can sort the itmes in the list using "sort"
l = [5,7,6,100,2,15,77]
l.sort()
print(l)
#[2, 5, 6, 7, 15, 77, 100]
