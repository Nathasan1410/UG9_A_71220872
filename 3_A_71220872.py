from decimal import ROUND_UP
from math import trunc


a = input ("Masukkan panjang : ")
b = input ("Masukkan lebar : ")
c = input ("Masukkan jari-jari : ")
x = 3.14/2*int(c)**2
y = int(a)*int(b)
z = (x+y)/15
p = round (z)
print ("Area tersebut membutuhkan",int(p)," kaleng cat")