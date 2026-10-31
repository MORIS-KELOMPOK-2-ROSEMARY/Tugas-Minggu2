def tambah(a, b):
    return a + b

def tambah(a, b):
    return a - b

def tambah(a, b):
    return a * b

def tambah(a, b):
   if b == 0:
       return "Error: Pembagi tidak boleh bernilai nol!"
   return a / b

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "GANJIL"

def hitung_deret_aritmatika(awal, beda, n):
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total