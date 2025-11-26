import BangunRuang as br ,Bangundatar as bd
#as itu digunakan untuk menyingkat nama
#boleh diimport kesamping atau ke bawah

print("----BANGUN RUANG----")
print(f"volum kubus dengan sisi 3 adalah{br.kubus(3)}")
print(f"volum balok adalah {br.balok(4,5,2)}")
print(f"volum prisma adalah{br.prisma(5,4,5)}")
print(f"volum tabung  adalah{br.tabung(7,7,10)}")
print(f"volum kerucut  adalah{br.kerucut(14,30)}")

print("----BANGUN DATAR----")
print(f"luas jajarganjar adalah{bd.jajarganjar(4,7)}")
print(f"luas persegi adalah{bd.persegi(4)}")
print(f"luas persegi panjang adalah{bd.persegi_panjang(2,6)}")
print(f"luas lingkaran adalah{bd.lingkaran(7)}")
print(f"luas segitiga adalah{bd.segitiga(10,8)}")