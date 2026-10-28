print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan suku pertama(a): "))
beda = int(input("Masukkan beda (b): "))


banyak = int(input("Masukkan banyak suku    (n): ")) 
while banyak <= 0:
    print("Banyak suku harus lebih dari 0.")
    banyak = int(input("Masukkan banyak suku    (n): "))


suku = awal
total = 0

print("Barisan Deret:", end=" ")
for i in range(banyak):
    print(suku, end=" ")
    total += suku
    suku += beda

print(f"\nTotal Jumlah Seluruh Deret = {total}")