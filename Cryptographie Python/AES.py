Sbox = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]

Erreur = ['0x00x', '0x10x', '0x20x', '0x30x', '0x40x', '0x50x', '0x60x', '0x70x', '0x80x', '0x90x', '0xa0x', '0xb0x', '0xc0x', '0xd0x', '0xe0x', '0xf0x']

Rcon = [[0x01, 0x00, 0x00, 0x00],
        [0x02, 0x00, 0x00, 0x00],
        [0x04, 0x00, 0x00, 0x00],
        [0x08, 0x00, 0x00, 0x00],
        [0x10, 0x00, 0x00, 0x00],
        [0x20, 0x00, 0x00, 0x00],
        [0x40, 0x00, 0x00, 0x00],
        [0x80, 0x00, 0x00, 0x00],
        [0x1b, 0x00, 0x00, 0x00],
        [0x36, 0x00, 0x00, 0x00],
        ]

table = 'abcdefghijklmnopqrstuvwxyz '           #la table doit contenir un espace pour le padding
Phrase = 'testd'
hexKey = [
    [0x2b,0x28,0xab,0x09],
    [0x7e,0xae,0xf7,0xcf],
    [0x15,0xd2,0x15,0x4f],
    [0x16,0xa6,0x88,0x3c]
    ]

NewPhrase = ''
hexa = []
SubBytes = []
NewSubBytes = []

while len(Phrase)%16 != 0:                      #padding pour avoir des multiple de 16 en héxa (ce qui nous servira pour les tables)
    Phrase = Phrase + ' '

for i in range(len(table)-1):                                               #conversion héxa de la table à partir de la table ASCII
    hexa = hexa + [hex(i+97)]
hexa = hexa + [hex(len(table)+5)]                                           #on associe [space] à 20 toujours selon la table ASCII

for i in range(len(Phrase)):                                                #conversion héxa du message à crypter
    for j in range(len(table)):
        if table[j] == Phrase[i]:
            NewPhrase = NewPhrase + hexa[j]

NewPhrase = '0xa40x9c0x7f0xf20x8e0x720x600x990xf00xd90x710xc10xb00x8c0xbd0x1c'#attention '0x08' différent de '0x8' test : 0xa40x9c0x7f0xf20x8e0x720x600x990xf00xd90x710xc10xb00x8c0xbd0x1c | 0x190xa00x9a0xe90x3d0xf40xc60xf80xe30xe20x8d0x480xbe0x2b0x2a0x8
X = []

#DEBUT ========================================================================================#

for KeySchedule in range(10):
    
    countX = 0
    for i in range(len(NewPhrase)):
        if NewPhrase[i] == 'x':
            countX = countX + 1
            X = X + [NewPhrase[i+1:i+4]]
            
    if len(NewPhrase) != countX*4:
        NewPhrase = ''                                                          #début de vérification des valeurs
        for i in range(countX):
            if X[i] == str(X[i][0:1])+'0x':
                NewPhrase = NewPhrase + '0x0'+str(X[i][0:1])
            else:
                NewPhrase = NewPhrase + '0x'+str(X[i][0:2])

        test = ''
        temp = ''
        if NewPhrase[len(NewPhrase)-2] == 'x':
            temp = NewPhrase[len(NewPhrase)-1]
            for i in range(len(NewPhrase)-1):
                test = test + NewPhrase[i]
            test = test + '0' + temp
        else:
            test = NewPhrase
        NewPhrase = ''
        
        for i in range(countX*4):
                NewPhrase = NewPhrase + test[i]                                 #fin de vérification
        X = [] #VOID
    
    for i in range(countX):                                                 #application du SubByte
        SubBytes = SubBytes + [hex(Sbox[int(NewPhrase[i*4:(i+1)*4], 16)])]
    print('SubBytes : ', SubBytes)

    i = 0
    for j in range(int(len(SubBytes)/4)):                                   #application du ShiftRows
        NewSubBytes = NewSubBytes + SubBytes[(j*4+i):((j+1)*4)]
        NewSubBytes = NewSubBytes + SubBytes[(j*4):((j+1)*4)-4+i]
        i = i + 1
        if i == 4:
            i=0 #VOID
    print('ShiftRows du SubBytes : ', NewSubBytes)

    SubBytes = [] #VOID
    for i in range(len(NewSubBytes)):                                       #conversion hex en décimal pour le Mix columns
        SubBytes.append(int(NewSubBytes[i], 16))
    
    i = 0                                                                   #application Mix Column
    NewSubBytes = [] #VOID
    
    mixed_state = []
    for i in range(len(NewSubBytes)):
        mixed_state.append(mix_columns(NewSubBytes[i]))
    
    K = ''
    for i in range(len(SubBytes)):
            K = K + hex(SubBytes[i])

    countX = 0                                                              #début de vérification des valeurs
    for i in range(len(K)):
        if K[i] == 'x':
            countX = countX + 1
            X = X + [K[i+1:i+4]]
    
    if len(K) != countX*4:
        K = ''                                                              
        for i in range(countX):
            if X[i] == str(X[i][0:1])+'0x':
                K = K + '0x0'+str(X[i][0:1])
            else:
                K = K + '0x'+str(X[i][0:2])

        test = ''
        temp = ''
        if K[len(K)-2] == 'x':
            temp = K[len(K)-1]
            for i in range(len(K)-1):
                test = test + K[i]
            test = test + '0' + temp
        else:
            test = K
        K = ''

        for i in range(countX*4):
                K = K + test[i]                                             #fin de vérification
        X = [] #VOID

    mixed_state = []

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
        mixed_state = mixed_state + [mixColumns(int(K[i*4:(i+1)*4], 16), int(K[(i*4)+16:((i+1)*4)+16], 16), int(K[(i*4)+32:((i+1)*4)+32], 16), int(K[(i*4)+48:((i+1)*4)+48], 16))]
    
    
    print('mixed_state : ', mixed_state)

    NewSubBytes = [] #VOID
    SubBytes = []
    
    #KeySchedule AREA ========================================================================================#

    #for KeySchedule in range(10):
    #def KeyScheduling(hexKey, Rcon, Sbox):
    HexKeySecondColumns = []
    for i in range(len(hexKey)):
        HexKeySecondColumns = HexKeySecondColumns + [hexKey[i][1]]

    HexKeyLastColumns = []
    for j in range(len(hexKey)):
        HexKeyLastColumns = HexKeyLastColumns + [hexKey[j][2:3] + hexKey[j][3:4]]

    numRows = len(hexKey)
    newHexKey = []
    newHexKeySubBytes = []
    x = []

    for i in range(numRows):                                                ####application RotWord SEULEMENT POUR LA PREMIERE COLONNE DE LA CLE
        newHexKey.append(hexKey[i].pop(3))                                  #newHexKey = [3,7,11,15]

    lastColumns = newHexKey[0:4]
    x = x + newHexKey[1:4]
    x = x + newHexKey[0:1]                                                  #x = [7,11,15,3]
    newHexKey = x                                                           #newHexKey = [7,11,15,3]
    x = []

    for i in range(len(newHexKey)):                                         ####application du SubByte SEULEMENT POUR LA PREMIERE COLONNE DE LA CLE
        newHexKeySubBytes = newHexKeySubBytes + [int(hex(Sbox[int(newHexKey[i])]), 16)]
    newHexKey = []                                                          #DEBUT DE LA CONSTRUCTION DE LA DEUXIEME CLE

    for i in range(numRows):                                                #prend la première colonne
        x.append(hexKey[i].pop(0))                                          #XOR le SubByte avec le Rcon et la première colonne de la clé pour toutes les colonnes
        newHexKey = newHexKey + [x[i]^newHexKeySubBytes[i]^Rcon[KeySchedule][i]]#Rcon[1//peut être remplacé par la grande boucle de 10][]  <-/
                                    
    x = []
    for j in range(numRows):                                                #calcul de la deuxième colonne en appliquant un XOR avec la première et la deuxième colonne de la première clé
        x.append(HexKeySecondColumns.pop(0))
        newHexKey = newHexKey + [x[j]^newHexKey[j]]
                                    
    for i in range(numRows-2):#le -2 enlève les deux première colonne       #calcul de la deuxième clé grâce aux deux dernière colonnes
        for j in range(4):
            newHexKey = newHexKey + [HexKeyLastColumns[j][i]^newHexKey[j+(i+1)*4]]

    #Nouvelle clé
    hexKey = []
    for i in range(numRows):
        hexKey = hexKey + [newHexKey[i*4:(i+1)*4]]

    newHexKey = []
    for i in range(numRows):
        for j in range(4):
            newHexKey = newHexKey + [hexKey[j][i]]
    hexKey = []
    for i in range(numRows):
        hexKey = hexKey + [newHexKey[i*4:(i+1)*4]]
    newHexKey = []
    print('hexKey : ', hexKey)
    #return hexKey

    #KeySchedule AREA ========================================================================================#
    
    encrypt = []                                                            #application AddRoundKey
    NewPhrase = '' #VOID

    for i in range(len(mixed_state)):
        for j in range(4):
            encrypt = encrypt + [mixed_state[i][j]^hexKey[j][i]]
            
    for i in range(len(encrypt)):
        NewPhrase = NewPhrase + str(hex(encrypt[i]))
        
    print('message encrypté : ', encrypt, ' | Round = ', (KeySchedule+1))
    print('message encrypté réutilisé : ', NewPhrase, '\n\n')
