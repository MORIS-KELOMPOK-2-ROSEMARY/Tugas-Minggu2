# ==========================================================
# Modul: Operasi_3.py
# Modul fungsi mandiri (def) dengan nilai kembalian (return)
# ==========================================================

def tambah (a, b):
    """Mengembalikan hasil penjumlahan a + b"""
    return a + b

def kurang (a, b):
    """Mengembalikan hasil pengurangan"""
    return a - b 

def kali (a, b):
    """Mengembalikan hasil perkalian"""
    return a * b 

def bagi(a, b):
    """     Mengembalikan hasil pembagian a / b. menangani pembagi bernilai 0.       
    mengembalikan hasil pembagian  a / b 
    Menangani pencegahan error saat pembagi bernilai nol.
    """
    if b == 0:
        return "Error: Pembagi tidak boleh bernilai 0!"
    return a / b

def cek_ganjil_genap(angka):
    """     Memeriksa sifat bilangan ganjil atau genap  menggunakan operator modulus (%)    
    Memeriksa sifat bilangan ganjil atau genap 
    mengguankan operator modulus(%)
    """
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    """     Menghitung total akumulasi deret mengguanakan perulangan for    
    Menghitung total akumulasi deret menggunakan perulangan for 
    """
    total = 0 
    suku = awal 
    for i in range(n):
        total += suku
        suku += beda 
    return total
    