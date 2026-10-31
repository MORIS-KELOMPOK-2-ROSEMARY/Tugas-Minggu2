kehadiran =  int(input("Jumlah kehadiran (1-14):  "))
nilai = int(input("Nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
        print("REMEDIAL - Nilai Ujian kurang")
else:
    print("TIDAK LULUS - kehadiran kurang dari 12")