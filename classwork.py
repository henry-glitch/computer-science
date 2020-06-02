import time
from datetime import datetime
from datetime import datetime as date
currentweek = 0
dayname = date.today().strftime("%A")


print('\n \n \n \n \n \n \n')
Monday = { 'RS',  'DT',  'French',  'Bioligy',  'Maths', }

Tuesday = { 'RS', 'PSHE',  'French',  'Chemistry',  'English', }

Wednesday = { 'Music',  'English', 'RS',  'Bioligy',  'Maths', }

Thursday = { 'Geography',  'French',  'PE',  'Games',  'Games', }

Friday = { 'French',  'Physics',  'Maths', 'English',  'Bioligy', }

weekA = (Monday,Tuesday,Wednesday,Thursday,Friday)



Monday2 = { 'French',  'Maths',  'English',  'DT', 'Physics', }

Tuesday2 = { 'Art',  'RS',  'Maths',  'Chemistry',  'French', }

Wednesday2 = { 'Music',  'Maths',  'Physics',  'History',  'Geography', }

Thursday2 = { 'Art',  'History',  'English',  'Games',  'Games', }

Friday2 = { 'Maths',  'Chemistry',  'English',  'Bioligy',  'History', }

weekB = (Monday2,Tuesday2,Wednesday2,Thursday2,Friday2)




books = []


today = datetime.today()
week = int(today.strftime("%U"))

print('\n \n \n')
if week % 2 == 0:
    print('\n \n \n')
    print("It is  %s weekB" % (dayname,))
    currentweek = weekA
    if dayname == 'Monday':
        print(weekA[0])
        day = weekA[0]
    elif dayname == 'Tuesday':
        print(weekA[1])
        day = weekA[1]
    elif dayname == 'Wednesday':
        print(weekA[2])
        dayname = weekA[2]
    elif dayname == 'Thursday':
        print(weekA[3])
        day = weekA[3]
    elif dayname == 'Friday':
        print(weekA[4])
        day = weekA[4]
    else:
        print('its the weekend silly!')
elif week %2 != 0:
    print('\n \n \n')
    print("It is  %s weekB" % (dayname,))
    if dayname == 'Monday':
        print(weekB[0])
        day = weekA[0]
    elif dayname == 'Tuesday':
        print(weekB[1])
        day = weekA[1]
    elif dayname == 'Wednesday':
        print(weekB[2])
        day = weekA[2]
    elif dayname == 'Thursday':
        print(weekB[3])
        day = weekA[3]
    elif dayname == 'Friday':
        print(weekB[4])
        day = weekA[4]
    else:
        print('its the weekend silly!')
    currentweek = weekB

print('\n \n \n')



while True:
    books = []
    print('do you have any more books :')
    print('Enter the books you have taken out here')
    book = input('')
    file = open("output.txt", "a")
    file.writelines(book + '\n')
    print('\n do you want to add more  y / n?')
    yn = input('')
    if yn == 'y':
        continue
    elif yn != 'n':
        print('I did not understand type again')
        print('do you want to add more  y / n?')
        yn = input('')
    else:
        break

with open('output.txt') as f:
    books = f.read().split('\n')

# Python program to find common elements in 
# both sets using intersection function in 
# sets 
  
  
# function  
def common_member(a, b): 
      
    a_set = set(a) 
    b_set = set(b) 
      
    # check length  
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return("you do not need to take any books") 
      
with open('output.txt') as f:
    book = f.read().split('\n')


print('You have these books')
print(book)
print('This is what lessons you have today')
print(day)
print('you need to take in these books')
print(common_member(day, book)) 