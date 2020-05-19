with open('output.txt') as f:
    todo = f.read().split('\n')



while True:
    todo = []
    print('do you want to input anything :')
    print('Enter what you want to do here')
    to = input('')
    todo.append(to)
    print('we have added ')
    print("You need to do  : \n")
    for i in todo:
        with open('output.txt', 'w') as f:
            for item in todo:              #note: don't call your variable list as that is a python reserved keyword
                f.write(str(item)+'\n')
        print(i, end = '\n')
        print('\ndo you want to add more  y / n?')
        yn = input('')
    if yn == 'y':
        continue
    elif yn != 'n':
        print('I did not understand type again')
        print('do you want to add more  y / n?')
        yn = input('')
    else:
        print('you need to :')
        print('')
        for i in todo:
            print(i, end = ' ')
            print(u'\u2713          \n' )
    break

