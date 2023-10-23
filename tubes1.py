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

for i in range(len(PINTU_TOL)):
    print(f"sekarang loop-{i} ada di {PINTU_TOL[i]}")
    if masuk == PINTU_TOL[i]:
        gerbang_masuk = i
    if keluar == PINTU_TOL[i]:
        gerbang_keluar = i

delta = gerbang_keluar - gerbang_masuk
if delta < 0:
    delta = -delta
total_tarif = (delta * TARIF_JOURNEY) + TARIF_TOL[golongan]
print(f"Total tarif Anda dengan kendaraan golongan {golongan} adalah Rp {total_tarif}")
