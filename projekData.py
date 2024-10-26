import os
import random
import string
data = dict()
while True:
    os.system("clear")
    print(f" {'DATA DRAKOR':_^35}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range (3))
    drakor1 = input("Drakor pertama\t:")
    drakor2 = input("Drakor favorit\t:")
    drakor3 = input("Drakor paling bagus\t:")
    data [ keyFinal ] = { keyFinal : { 'drakor1key' : drakor1, 'drakor2key' : drakor2, 'drakor3key' : drakor3}}
    print(data)

    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"key\t Bussines proposal\t Love Next Door\t Family  by choice\t")
    
