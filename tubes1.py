print("================== PROGRAM PINTU TOL =================")

golongan = int(input("Masukkan golongan kendaraan: "))
masuk = str(input("Masukkan pintu masuk tol: "))
keluar = str(input("Masukkan pintu keluar tol: "))

pintu_tol = ["pasteur", "pasir koja" , "kopo" , "moh toha" , "buah batu" , "cileunyi"]

i = 0 
if golongan == 1: 
    tarif_1 = 5000
    while masuk == pintu_tol[0] and keluar <= pintu_tol[5]:
        tarif_1 += 1500
        pintu_tol[i+1]
    print (f'harga {tarif_1}')




