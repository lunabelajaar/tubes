TARIF_TOL = {
    "1": 5000,
    "2": 7000,
    "3": 10000,
    "4": 12000,
    "5": 15000,
}
PINTU_TOL = ["pasteur", "pasir koja", "kopo", "moh toha", "buah batu", "cileunyi"]
TARIF_JOURNEY = 1500


# Fungsi untuk mengecek apakah input golongan benar atau tydac.
def is_golongan(golongan):
    if golongan in ["1", "2", "3", "4", "5"]:
        return True
    else:
        return False


# Fungsi untuk mengecek pintu tol.
def is_gerbang_valid(gerbang):
    if gerbang in PINTU_TOL:
        return True
    else:
        return False


print("================== PROGRAM PINTU TOL =================")

# input golongan.
ask_golongan = True
while ask_golongan:
    golongan = input("Masukkan golongan kendaraan (1/2/3/4/5): ")
    if is_golongan(golongan):
        ask_golongan = False
    else:
        print("---WARNING: Masukkan golongan yang benar (1/2/3/4/5)")

ask_gerbang = True
while ask_gerbang:
    masuk = input("Masukkan pintu masuk tol: ")
    if is_gerbang_valid(masuk):
        ask_gerbang = False
    else:
        print("---WARNING: Masukkan gerbang tol yang benar:")
        print(f"---{PINTU_TOL}")

ask_gerbang = True
while ask_gerbang:
    keluar = input("Masukkan pintu keluar tol: ")
    if is_gerbang_valid(keluar):
        ask_gerbang = False
    else:
        print("---WARNING: Masukkan gerbang tol yang benar:")
        print(f"---{PINTU_TOL}")


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
