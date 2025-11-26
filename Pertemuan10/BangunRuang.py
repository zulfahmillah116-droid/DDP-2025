import math
def kubus(sisi):
   hasil = math.pow(sisi,3)
   return hasil
#return berfungsi untuk mengahasilkan nilai

# print(kubus(3))

def balok(p,l,t):
   hasil = p * l* t
   return hasil
# print(balok(3,3,3))

def prisma(alas,tinggi_segitiga,tinggi_prisma):
   luas_alas = 0.5 * alas * tinggi_segitiga
   hasil = luas_alas * tinggi_prisma
   return hasil
# print(prisma(3,3,3))

def tabung(luas_alas,tinggi,r):
   luas_alas = 22/7 * r * r
   hasil = luas_alas * tinggi
   return hasil 
# print(tabung(7,7,10))

def kerucut(r,t):
   hasil = 1/3 * 22/7 * r**2 * t
   return hasil 
