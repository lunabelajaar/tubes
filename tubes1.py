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

total_tarif = TARIF_TOL[golongan]
id_masuk = 0
for count, gerbang_tol in enumerate(PINTU_TOL):
    if gerbang_tol == masuk:
        id_masuk = count
    if gerbang_tol == keluar:
        id_keluar = count

total_tarif += abs(id_keluar-id_masuk) * TARIF_JOURNEY
print(f"Total tarif Rp {total_tarif}")

