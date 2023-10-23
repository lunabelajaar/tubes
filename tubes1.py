TARIF_TOL = {
    "1": 5000,
    "2": 7000,
    "3": 10000,
    "4": 12000,
    "5": 15000,
}
PINTU_TOL = ["pasteur", "pasir koja", "kopo", "moh toha", "buah batu", "cileunyi"]
TARIF_JOURNEY = 1500

print("================== PROGRAM PINTU TOL =================")

golongan = input("Masukkan golongan kendaraan (1/2/3/4/5): ")
masuk = input("Masukkan pintu masuk tol: ")
keluar = input("Masukkan pintu keluar tol: ")

in_journey = False
for gerbang_tol in PINTU_TOL:
    if in_journey:
        total_tarif += 1500
    if gerbang_tol == masuk:
        total_tarif = TARIF_TOL[golongan]
        in_journey = True
    if gerbang_tol == keluar:
        print(f"Total tarif Rp {total_tarif}")
