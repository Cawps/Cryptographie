table  = 'abcdefghijklmnopqrstuvwxyz' 
key = input("Entrez une clé de chiffrement : ")
newKey = ''
Phrase = input("Entrez un chaine de caractère à dé/coder : ")
PhraseEncode = ''

for i in range(len(Phrase)):
    if Phrase[i] == ' ':
        PhraseEncode = PhraseEncode + ''
    else:
        PhraseEncode = PhraseEncode + Phrase[i]

L = len(PhraseEncode)
countP = [0]*L
countK = [0]*L
i = 0

while len(key) < L:
    key = key + key[i%len(key)]
if len(key) > L:
  while len(newKey) < L:
      newKey = newKey + key[i]
      i = i + 1

i = 0
l = 0
for k in range(L): 
    for j in range(len(table)): 
        if PhraseEncode[k] == table[j]: 
            countP[i] = j
            i = i + 1
        if key[k] == table[j]: 
            countK[l] = j
            l = l + 1
        
PhraseEncode = ''
PhraseDecode = ''
for i in range(L):
    count = (countP[i] + countK[i])
    decount = (countP[i] - countK[i])
    PhraseEncode = PhraseEncode + table[count%26]
    PhraseDecode = PhraseDecode + table[decount%26]

print('Mot codé : ', PhraseEncode)
print('Mot décodé : ', PhraseDecode)
