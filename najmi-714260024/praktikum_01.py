kehadiran = int(input("Jumlah Kehadiran?(1-14)): "))
nilai = int(input("Nilai Ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
        print("REMEDIAL - nilai Ujian Kurang")
else:
    print("TIDAK LULUS - Kehadiran Kurang dari 12")