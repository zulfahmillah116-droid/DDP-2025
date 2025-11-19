#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus :
#nilai (80) #lulus
#nilai(60) #gagal

def nilai(n = 0):
    if n <= 60:
        print("tidak lulus")
    elif n > 60 and n <= 100:
        print("lulus")
    else:
        print("tidak diketahui")  

nilai(80)
nilai()           
