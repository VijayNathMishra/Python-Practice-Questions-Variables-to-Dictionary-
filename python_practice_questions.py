#Create a variable name and store your name.
name ="ram"
#print the name variable 
print(name)


#Create variables age, city, and college and print them.
age =25
city = "delhi"
college ="abc college"
print(age)
print(city)
print(college)

#store two number and print their sum.
num1 = 10
num2 = 20
sum = num1 +num2 
print(sum)

#swap two variables and print the result.
a =5
b=10
temp =a
a=b
b=temp
print("after swapping a:",a)


#take user input and print a greeting message with the input name.
user_name =input("enter your naem:")
print("Hello " +user_name+" Welcome to python programming!")


#check data type of a integer  float ,string and boolean. values.
int_var = 10
float_var = 3.14
string_var= "hello"
boolean_var =True
print(type(int_var))
print(type(float_var))
print(type(string_var))
print(type(boolean_var))

# Convert integer into string.
num_str = '123'
num_int = int(num_str)
print(num_int)
print(type(num_int))


#Convert string "100" into integer.
str_num = 100
int_num = int(str_num)
print(int_num)
#conbert string "3.14"into float.
str_float ="3.14"
float_num = float(str_float)
print(float_num)

# Day 2 python 
#Create a string "Python" and print first character.
string ="python"
print(string[0])


#Print last character of a string.
a = input("Enter a string: ")
print("last character of the string is :", a[-1])


#Find length of a string using len().
my_str ="hello Vijay"
print(len(my_str))

#Convert a string into uppercase
a= "hello vijay"
print(a.upper())

#Convert a string into lowercase.
a= "hello vijay"
print(a.lower())



#Print every second character from "Python".
a= "python"
print(a[: :2])


#Check if a word exists in a string.
a= input("Enter a string ")
b= input("Enter a word to check if it exists in the string ")
print(b in a)


#Concatenate two strings.
a= "hello"
b = "world"
c= a+ " "+b
print(c)

#Create a list of 5 fruits.
a =["apple","banana","garpe","orange","kiwi"]
print(a)


#Add a new item into list using append().
a =["vijay", "mishra"]
a.append("nath")
print(a)

#Insert an item at specific position in list.
a =[1,2,3,4,5]
a.insert(6,10)
print(a)

#Remove an item from list.
a =[1,2,3,4,5]
a.remove(3)
print(a)

#Print first and last item of list..
a =[1,2,3,4,5]
print(a[0])
print(a[-1])

#Find length of list..
a =[1,2,3,4,5]
print(len(a))

#Loop through a list using for loop.
a =[1,2,3,4,5]
for i in a:
    print(i)

#Create a tuple of 5 numbers.
num =(1,2,3,4,5)
print(num)

#Access second element from tuple.
a_tuple =("apple","bananana","cherry")
print(a_tuple)


#Count occurrence of an element in tuple.
a_tuple =("apple","bananana","cherry")
print(a_tuple.count("apple"))

#Find index of an element in tuple.
a_tuple =("apple","bananana","cherry")
print(a_tuple.index("cherry"))

#Create a set with duplicate valuesAdd a new value into set.
a ={1,2,3,4,5,5}
a.add(6)
print(a)

#Remove an item from set.

a ={1,2,3,4,5,5}
a.remove(5)
print(a)

#Create two sets and find union.
a ={1,2,3,4}
b={3,4,5,6}
print(a.union(b))

#Create two sets and find intersection.
a ={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))


#Create a dictionary with name and age.
a = {"name" : "vijay","age": 27}
print(a)

#Print all keys of dictionary.
a ={"name": "sachin","age": 30,"city": "pune"}
print(a.keys())

#Print all values of dictionary.
a ={"name": "sachin","age": 30,"city": "pune"}
print(a.values())

#Add a new key-value pair in dictionary.
a ={"name": "sachin","age": 30,"city": "pune"}
a["country"] = "india"
print(a.items())

#Update value of existing key in dictionary.
my_dict={'naem': "python",'version': 3.6}
my_dict['version'] = 3.11
print(my_dict)

#Remove a key from dictionary.
my_dict={'name': "python",'version': 3.6}
print(my_dict)
my_dict.pop('version')
print(my_dict)


#Loop through dictionary using for loop.
my_dict ={"name":"shukal","age": 28, "city": "nepal"}
for key in my_dict:
    print(key,my_dict[key])


#Create a list of marks and find maximum value.
marks =[45,67,67,89,90]
print(max(marks))

#Count vowels in a string.
a =input("enter a string ")
vowels="aeiouAEIOU"
count =0
for i in   a:
    if i in vowels:
        count+=1
        print("number of vowels in the string is ",count)


#Create a dictionary for 3 students and their marks.
students_marks = {
    "Vivek": 90,
    "Vishnu": 80,
    "Ram": 70
}
print(students_marks


 #Find sum of all elements in a list.
lis = [1, 2, 3, 4, 5, 6, 7]
total = 0

for i in lis:
    total += i

print("Sum of all elements in list is:", total)


#Create nested dictionary for student details.
student_details ={"student1": {
        "name": "Ram",
        "age": 20,
        "marks": 90
    }}
print(student_details)


#Create a list of numbers and print only even numbers.
numbera= [1,2,3,4,5,6,7,8,9,10]
for number in numbera:
    if number % 2== 0:
        print(number)

#odd numbers
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i%2!=0:
        print(i)


#Sum of Even Numbers
a= [1,2,3,4,5,6,7,8,9,10]
sum  = 0
for i in a:
    if i%2 ==0:
        sum = sum+i
        print(sum)


#Largest Even Number
a =int(input("Enter a number:"))
if a%2==0:
    print("The largest even number is ",a)
else:
    print("The largest even number is ",a-1)


#List Comprehension Tricks
numbers = [1,2,3,4,5,6,7,8,9,10]

evens = [n for n in numbers if n % 2 == 0]

print(evens)


#odd number 
odds = [n for n in numbers if n % 2 != 0]

print(odds)

#squares if numbers
squares = [n*n for n in numbers]

print(squares)

#Create a string and count total characters.
str = "hello python"
print(len(str))

#Create a set and check if a value exists.
my_set ={1,2,3,4,5}
print(3 in my_set)


# Create a dictionary and print specific value using key

my_dict = {"name": "python", "age": 30}

print(my_dict["name"])

#Create a program to store and display your favorite movies in a list.
a =["harry potter","ther lord of the rings","the hobbit","the hunger games", "the maze runner"]
print(a)
