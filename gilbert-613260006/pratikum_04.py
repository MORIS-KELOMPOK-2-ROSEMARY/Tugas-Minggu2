# PRAKTIKUM 4 : NESTED LOOP & MANIPULASI LIST
# Simpan sebagai: praktikum_04.py

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris*kolom}\t", end="")
    print()  # Pindah baris

# 2. Pengenalan List Data Nilai
nilai_mhs = [12, 32, 21]
nilai_mhs.append(85)  # Menambah data di akhir

print("Daftar Nilai : ", nilai_mhs)
print("Nilai Tertinggi: ", max(nilai_mhs))