
while True:
    todo = []
    print('do you want to input anything :')
    print('Enter what you want to do here')
    to = input('')
    todo.append(to)
    print('we have added ')
    print("You need to do  : \n")
    for i in todo:
        print(i, end = ' \n')
        print('\ndo you want to add more  y / n?')
        yn = input('')
    if yn == 'y':
        continue
    elif yn != 'n':
        print('I did not understand type again')
        print('do you want to add more  y / n?')
        yn = input('')
    else:
        break