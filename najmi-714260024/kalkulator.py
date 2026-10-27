import operasi3

while True:
    print("\n" + "=" * 45)
    print("        APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+,-,*,/)")
    print("2. Cek sifat Bilangan (Ganjil/ Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "5":
        print("\nTerima kasih telah menggunakan kalkulator konsol. Program selesai.")
        break

    elif pilihan == "1":
        print("\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        op = input("Pilihan operasi (A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan bilangan pertama: ")
            inp2 = input("Masukkan bilangan kedua: ")

            if inp1.replace("-", "", 1).isdigit() and inp2.replace("-", "", 1).isdigit():
                num1 = float(inp1)
                num2 = float(inp2)

                if op == "A":
                    hasil = operasi3.tambah(num1, num2)
                    print(f"Hasil {num1} + {num2} = {hasil}")
                elif op == "B":
                    hasil = operasi3.kurang(num1, num2)
                    print(f"Hasil {num1} - {num2} = {hasil}")
                elif op == "C":
                    hasil = operasi3.kali(num1, num2)
                    print(f"Hasil {num1} * {num2} = {hasil}")
                elif op == "D":
                    if num2 != 0:
                        hasil = operasi3.bagi(num1, num2)
                        print(f"Hasil {num1} / {num2} = {hasil}")
                    else:
                        print("Peringatan: Pembagi tidak boleh 0!")
            else:
                print("Peringatan: Masukkan wajib berupa bilangan bulat!")
        else:
            print("Peringatan: Pilihan operasi tidak valid!")

    elif pilihan == "2":
        print("\n--- Cek Ganjil / Genap ---")
        inp_angka = input("Masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"Hasil: Angka {angka} tergolong bilangan {status}.")
        else:
            print("Peringatan: Masukkan harus berupa bilangan murni!")

    elif pilihan == "3":
        print("\n--- Hitung Deret Aritmatika ---")
        inp_a = input("Suku Pertama (a): ")
        inp_b = input("Beda Deret (b): ")
        inp_n = input("Banyak Suku (n): ")

        if inp_a.replace("-", "", 1).isdigit() and inp_b.replace("-", "", 1).isdigit() and inp_n.replace("-", "", 1).isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("Peringatan: Banyak suku n harus lebih dari 0!")
                n = int(input("Masukkan ulang banyak suku (n): "))

            total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
            print(f"Total Jumlah Seluruh Deret = {total_deret}")
        else:
            print("Peringatan: Seluruh masukan wajib berupa angka bulat!")

    elif pilihan == "4":
        print("\n--- Matriks Perkalian 1-3 (Nested Loop) ---")

        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end=" ")
            print()

    else:
        print("Pilihan tidak valid! Silakan masukkan opsi 1 sampai 5.")