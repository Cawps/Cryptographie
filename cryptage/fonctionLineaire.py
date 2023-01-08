from math import sqrt
table = 'abcdefghijklmnopqrstuvwyxz'
chaine = input('Entrez la chaine à coder : ')
encrypt = '>>> '
impossible = False
a = int(input('Entrez un premier cœfficient : '))
b = int(input('Entrez un second cœfficient : '))

for i in range(2, round(sqrt(len(chaine))+1)+1):
    if(len(chaine)%i==0 and i == a):
        impossible = True

for j in range(len(chaine)):
    for i in range(len(table)):
        if table[i] == chaine[j]:
            encrypt = encrypt + table[(i*a+b)%26]
        
if impossible:
    print("Le cœfficient n'est pas premier avec la longueur de l'alphabet")
else:
    print(encrypt)
