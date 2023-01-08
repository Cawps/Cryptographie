table = 'abcdefghijklmnopqrstuvwxyz'
Phrase = input('Entrer une chaine à coder : ') 
encryptPhrase = '' 
for j in range(len(table)): 
  for i in range(len(Phrase)): 
    for k in range(len(table)): 
      if(Phrase[i] == table[k]): 
        encryptPhrase = encryptPhrase + table[(k+j)%26]#si la taille de la table change il faut changer le modulo par le nombre correspondant à la longueur de la table, 26 a été mis afin d’être plus explicite.
  print(encryptPhrase, ' <<<', j+1) 
  encryptPhrase = ''
