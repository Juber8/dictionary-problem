#sort the dict by key and value
#by key
'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
lst1=sorted(d.items(),key=lambda x:x[0])
print(lst1)

#by value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
lst1=sorted(d.items(),key=lambda x:x[1])
print(lst1)

#reverse the dict
d={'juber':55,'ajay':52,'nilesh':85,'nawaj':23}
j={v:k for k,v in d.items()}
print(j)

#i want value by descending oeder
import operator
d={'juber':55,'ajay':52,'nilesh':85,'nawaj':23}
sorted_d =dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)

#add key to dictionry
#to add key to dict use update method
j={0: 10, 1: 20}
j.update({2:30,3:40,4:60})
print(j)

# concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

#check key is present or not
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_present(x):
    if x in d:
        print('key is present in dict')
    else:
        print('key is not present in dict')
key_present(0)

d = {'x': 10, 'y': 20, 'z': 30}
for k,v in d.items():
    print(k,v,sep=':')

# Generate and print
# a
# dictionary
# that
# contains
# a
# number in the
# form(x, x * x)
n=int(input('enter the number'))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)

n=int(input('enter the number'))
d={}
for i in range(1,n+1):
    print(i)

d={}
for i in range(1,16):
    d[i]=i**2
print(d)

#MERGE TWO DICT
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d1.update(d2)
print(d1)

d = {'Red': 1, 'Green': 2, 'Blue': 3}
for k,v in d.items():
    print(k,v)

#sum of all values
my_dict = {'data1':100,'data2':-54,'data3':247}
sum=0
for i in my_dict.values():
    sum+=i
print(sum)

print(sum(my_dict.values()))

#multiply all values
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for i in my_dict.values():
    result=result * i

print(result)

#remove key in my dict
myDict = {'a':1,'b':2,'c':3,'d':4}
myDict.pop('a')
print(myDict)

myDict = {'a':1,'b':2,'c':3,'d':4}
if 'a' in myDict:
        del myDict['a']
print(myDict)

myDict = {'a':1,'b':2,'c':3,'d':4}
myDict[2]=300
print(myDict)

myDict = {'a':1,'b':2,'c':3,'d':4}
myDict.fromkeys()

print(myDict)

l=[1,2,3,4]
j=dict.fromkeys(l,100)
print(j)

import sys
for i in range(4):
    num= int(input('Enter no:.'))
    print(i)
else:
    print('Loop executed...')
    #sys.exit()
print('Lets do the new code')
#for highest key
my_dict = {'x':500, 'y':5874, 'z': 560}
highest=(max(my_dict,key=my_dict.get))
print(highest)

#for highest value
my_dict = {'x':500, 'y':5874, 'z': 560}
highest=max(my_dict.values())
print(highest)

l=[1,2,3,4]
j=dict.fromkeys(l,100)
print(j)

def display(name):
    print('hello',name)
display('juber')


import math as m

def sum():
    pass
def display():
    pass

x,y,z=input('enter a number')
print(x,y,z)

myDict = {'a':1,'b':2,'c':3,'d':4}
myDict[2]=300
print(myDict)

marks = {'Physics':67, 'Maths':87}
print(marks.get('Maths'))

marks = {'Physics':67, 'Maths':87}
print(marks.items())

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.popitem())

person = {'name': 'Phill', 'age': 22}
print(person.setdefault('time',100))
print(person)

# create a dictionary
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

print(marks.pop())

 #tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print(fSet)

message = 'Python is fun'

# convert string to bytes
byte_message = bytes(message,'utf8')
print(byte_message)

# Output: b'Python is fun'

prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)
'''
