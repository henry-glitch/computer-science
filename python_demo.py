#we can import packages
#these do things that make using python easier eg time features
from datetime import datetime

#comments use # 


# print function
print('hello world')
#string concatenation
print('hello '+ 'world')
#variables store data eg :
num = 2
#arithmatic
#times:
print(1 * 2) 
#divide:
print(1/2)
#subtract:
print(1-2)
#addition
print(1+2)
#remainder
print(1%2)
#+= operater
num += 2
#-= operator
num-=2
#integers or int are just normal numbers eg
int0 = 7
# there are also floats that store decimal point numbers
float0 = 7.2
#strings are a set of charecters eg:
string0 ='Hello world'
#booleans 
bool0 = True
#number and string concatination
print('Hello my favourit number is ' + str(int0))
#this causes an problem ending the string
print('There's a problem here ')
#to fix this we use the backslash charecter \ :
print('There\'s not problem here ')
#numbers in python start with 0 instead of one eg:
#+---+---+---+---+---+---+
#| P | Y | T | H | O | N |
#+---+---+---+---+---+---+
#  0   1   2   3   4   5
print(string0[1])
#this would print the e of Hello world
#string functions:
len(string0)
#this returns the length of the string
string0.upper()
#this converts all of the charecters to upper case
string0.lower()
#this converts all of the string to lower case
print(str(float0))
#this turns the float into a string
#string formatting with %
os ='android'
version = '4'
print ("I have an %sversion %s." % (os, version))
#to get the time from datetime we use this function
print datetime.now()
#the year
current_year = now.year
#the month
current_month = now.month
#the day
current_day = now.day
#mm/dd/yy format
print ('%02d/%02d/%04d' % (now.month, now.day, now.year))
#digital clock from the datetime module
print ('%s:%s:%s' % (now.year, now.month, now.day))
#the compete time
print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
#get user input
name = input('Enter your name:')
#comparaters
2!=3
#not equal to 
2==2
#equal too
2>3
#more than 
2<3
#smaller than 
2<=3
#smaller than or equal too
3>=2
#greater than or equal too
#and this returns true if both statements are True 
2 >3 and 3>2
#or this returns true if one of theses are true
2 ==3 or 1==1
#if statement
if 1+2=3 :
    print('math.upper()')
#if else
if 1==1:
    print(now.day)
else:
    print(now.month)
#if elif else
var age=int(input('Enter your age'))
if age == 116:
    print('Vampire')
elif age >= 0:
    print('youngling')
else :
    print('normal human ')
#Yay! functions
name = str(input('Enter your name'))
def function(name):
    print('Hello %s'(name))
#arrays creating an array
myarray = [1,2,3,4,5,6,7,8,9,10]
#add things to the array
myarray.append(11)
#show certain points of the array
print(myarray[2:5])
#show everything from a certain point of an aaray to the end
print(myarray[1:])
#find the position of something in a list
3_index = myarray.index(3)
#add something to a string
myarray.indert(3_index,-3)
#delete array function
del my_array[4]
#for loop
for number in my_array:
    print(2*number)
#functions and list example and dicts
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler]

avg = get_class_average(students)
print(avg)
print(get_letter_grade(avg))