NewPhrase = '0x190xa00x9a0xe90x3d0xf40xc60xf80xe30xe20x8d0x480xbe0x2b0x2a0x8'
X = []

countX = 0
for i in range(len(NewPhrase)):
    if NewPhrase[i] == 'x':
        countX = countX + 1
        X = X + [NewPhrase[i+1:i+4]]
print(countX)

if len(NewPhrase) != countX*4:    
    NewPhrase = ''
    for i in range(countX):
        if X[i] == str(X[i][0:1])+'0x':
            print(X[i], ' = ', X[i][0:1]+'0x', '  |  ', X[i][0:1])
            NewPhrase = NewPhrase + '0x0'+str(X[i][0:1])
            print(NewPhrase)
        else:
            NewPhrase = NewPhrase + '0x'+str(X[i][0:2])
            print(NewPhrase)

    test = ''
    temp = ''
    if NewPhrase[len(NewPhrase)-2] == 'x':
        temp = NewPhrase[len(NewPhrase)-1]
        for i in range(len(NewPhrase)):
            print(test)
            test = test + NewPhrase[i]
        test = test + '0' + temp
    else:
        test = NewPhrase

    NewPhrase = ''
    print(test)
    for i in range(countX*4):
        NewPhrase = NewPhrase + test[i]

print(NewPhrase,'\n- ',len(NewPhrase))
