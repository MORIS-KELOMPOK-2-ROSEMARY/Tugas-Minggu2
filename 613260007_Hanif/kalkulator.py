import modul_logika

while True:
    print("\n" + "=" *45)
    print(" APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (Ganjil / Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")


    if pilihan == "5":
        print("\nTerima kasih telah menggunakan Kalkukator Konsol. Program selesai")
        break

    elif pilihan == "1":
        print("\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pe,bagian (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukan angka pertama : ")
            inp2 = input("Masukan angka kedua : ")

            if inp1.isdigit() and inp2.isdigit() :
                a = int(inp1)
                b = int(inp2)

                if op == "A":
                    hasil = modul_logika.tambah(a,b)
                    print(f"Hasil {a} + {b} = {hasil}")
                elif op == "B":
                    hasil = modul_logika.kurang(a,b)
                    print(f"Hasil {a} - {b} = {hasil}")
                elif op == "C":
                    hasil = modul_logika.kali(a,b)
                    print(f"Hasil {a} * {b} = {hasil}")
                elif op == "D":
                    hasil = modul_logika.bagi(a,b)
                    print(f"Hasil {a} / {b} = {hasil}")
            else:
                print("Peringatan: Masukan wajib berupa bilangan bulat!")
        else:
            print("Peringatan: Pilihan operasi tidak valid!")


    elif pilihan == "2":
        print("\n--- Cek Ganjil / Genap (Modulus %) ---")
        inp_angka = input("Masukan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = modul_logika.cek_ganjil_genap(angka)
            print(f"Hasil: Angka {angka} tergolong bilangan {status}")
        else:
            print("Peringatan: Masukan harus berupa angka murni!")


    elif pilihan == "3":
        print("\n---Hitung Deret Aritmatika ---")
        inp_a = input("Suku Pertama (a) : ")
        inp_b = input("Beda Deret (b) : ")
        inp_n = input("banyak Suku (n) : ")

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <=0:
                print("Peringatan: Banyak suku (n) harus lebih dari 01")
                n = int(input("masukkan ulang banyak suku (n): "))

                total_deret = modul_logika.hitung_deret_aritmatika(a, b, n)
                print(f"Total Jumlah Seluruh Deret = {total_deret}")
        else:
            print(f"Peringatan: Seluruh masukan wajib berupa angka bulat!")


    elif pilihan == "4":
        print("\n--- Matriks Tabel Perkalian 1-3 (Nested Loop)")

        for baris in range(1,4):
            for kolom in range(1,4):
                print(f"{baris * kolom}\t", end="")
            print()

    else:
        print("Pilihan tidak valid! Silahkan masukan opsi  1 sampai 5.")    