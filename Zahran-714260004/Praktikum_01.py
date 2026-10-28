#======================== IF
# PRAKTIKUM 1 : NESTED(EVALUASI KELULUSAN)
# simpan sebai : praktikum_01.py

kehadiran = int(input("Jumlah kehadiran (1-14):"))
nilai = int(input ("Nilai Ujian (0-100):"))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
        print("REMEDIAL- Niali Ujian Kurang")
else:
    print("Tidak LULUS - kehadiran kurang dari 12")

