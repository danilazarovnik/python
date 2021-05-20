from sys import argv

name, chasi_raboti, stavka, premiya = argv

zp = (int(chasi_raboti) * int(stavka)) + int(premiya)
print("ЗП равна: ", zp)
