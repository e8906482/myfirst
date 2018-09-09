try:
    file = open('eee.txt','r+')
except Exception as e:
    print('there is no file named as eee')
    response = input('do you want to create a new file?')
    if response == 'y':
        file = open('eee.txt','w')
    else:
        pass
else:
    file.write('sss')
    file.close()
