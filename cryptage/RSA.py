import math
import random

m = 10 #message

p = 5003
q = 6733

n = p*q
phi_n = (p-1)*(q-1)

#PGCD(e, phi_n)
e = 65537 #plus grand entier connu étant nombre de fermat et premier
print('hey')

d=0
while (d*e)%phi_n != 1: d=d+1

#p, q, phi_n is null

# 0 <= m < n

#===== Partie Chiffrement =====#
x = (m**e)%n #x = m chiffré
print(x)

#===== Partie Déchiffrement =====#
m = (x**d)%n
print(m)
