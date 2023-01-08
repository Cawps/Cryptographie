'''
PredefineMatrix = []
test = [0x19, 0xa0, 0x9a, 0xe9, 0x3d, 0xf4, 0xc6, 0xf8, 0xe3, 0xe2, 0x8d, 0x48, 0xbe, 0x2b, 0x2a, 0x08]
newTest = []
print(test)
i = 0
while i<len(test):
    newTest.append(test[i:i+4])
    i+=4

def mix_columns(column):
    mixed_column = [0] * len(newTest)
    mixed_column[0] = (2 * column[0] + 3 * column[1] + 1 * column[2] + 1 * column[3]) % 256
    mixed_column[1] = (1 * column[0] + 2 * column[1] + 3 * column[2] + 1 * column[3]) % 256
    mixed_column[2] = (1 * column[0] + 1 * column[1] + 2 * column[2] + 3 * column[3]) % 256
    mixed_column[3] = (3 * column[0] + 1 * column[1] + 1 * column[2] + 2 * column[3]) % 256
    return mixed_column

mixed_state = []
for i in range(len(newTest)):
    mixed_state.append(mix_columns(newTest[i]))

print(mixed_state)
'''

K = ''
SubBytes = ['0xd4', '0xe0', '0xb8', '0x1e', '0xbf', '0xb4', '0x41', '0x27', '0x5d', '0x52', '0x11', '0x98', '0x30', '0xae', '0xf1', '0xe5']

for i in range(len(L)):
        K = K + SubBytes[i]
M = []

def mixColumns(a, b, c, d):
    e = (gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    f = (gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    g = (gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    h = (gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    return e,f,g,h

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

for i in range(4):
    M = M + [mixColumns(int(K[i*4:(i+1)*4], 16), int(K[(i*4)+16:((i+1)*4)+16], 16), int(K[(i*4)+32:((i+1)*4)+32], 16), int(K[(i*4)+48:((i+1)*4)+48], 16))] # 0x8e 0x4d 0xa1 0xbc










    
