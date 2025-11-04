import math

# ===== Fungsi Bangun Datar =====
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(p, l):
    return p * l

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c

def luas_lingkaran(r):
    return math.pi * r * r

def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def keliling_belah_ketupat(sisi):
    return 4 * sisi

# ===== Program Utama =====
riwayat = []

while True:
    print("\n=== Kalkulator Bangun Datar ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Belah Ketupat")
    print("7. Lihat Riwayat")
    print("8. Keluar")

    pilihan = input("Pilih bangun datar (1-8): ")

    if pilihan == '1':
        try:
            sisi = float(input("Masukkan sisi persegi (cm): "))
            if sisi <= 0:
                raise ValueError
            luas = luas_persegi(sisi)
            keliling = keliling_persegi(sisi)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Persegi - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '2':
        try:
            p = float(input("Masukkan panjang (cm): "))
            l = float(input("Masukkan lebar (cm): "))
            if p <= 0 or l <= 0:
                raise ValueError
            luas = luas_persegi_panjang(p, l)
            keliling = keliling_persegi_panjang(p, l)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Persegi Panjang - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '3':
        try:
            alas = float(input("Masukkan alas (cm): "))
            tinggi = float(input("Masukkan tinggi (cm): "))
            a = float(input("Masukkan sisi A (cm): "))
            b = float(input("Masukkan sisi B (cm): "))
            c = float(input("Masukkan sisi C (cm): "))
            if alas <= 0 or tinggi <= 0 or a <= 0 or b <= 0 or c <= 0:
                raise ValueError
            luas = luas_segitiga(alas, tinggi)
            keliling = keliling_segitiga(a, b, c)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Segitiga - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '4':
        try:
            r = float(input("Masukkan jari-jari (cm): "))
            if r <= 0:
                raise ValueError
            luas = luas_lingkaran(r)
            keliling = keliling_lingkaran(r)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Lingkaran - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '5':
        try:
            alas = float(input("Masukkan alas (cm): "))
            tinggi = float(input("Masukkan tinggi (cm): "))
            sisi = float(input("Masukkan sisi miring (cm): "))
            if alas <= 0 or tinggi <= 0 or sisi <= 0:
                raise ValueError
            luas = luas_jajar_genjang(alas, tinggi)
            keliling = keliling_jajar_genjang(alas, sisi)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Jajar Genjang - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '6':
        try:
            d1 = float(input("Masukkan diagonal 1 (cm): "))
            d2 = float(input("Masukkan diagonal 2 (cm): "))
            sisi = float(input("Masukkan sisi (cm): "))
            if d1 <= 0 or d2 <= 0 or sisi <= 0:
                raise ValueError
            luas = luas_belah_ketupat(d1, d2)
            keliling = keliling_belah_ketupat(sisi)
            print(f"Luas: {luas:.2f} cm²")
            print(f"Keliling: {keliling:.2f} cm")
            riwayat.append(f"Belah Ketupat - Luas: {luas:.2f} cm², Keliling: {keliling:.2f} cm")
        except:
            print("Input tidak valid.")

    elif pilihan == '7':
        print("\n📄 Riwayat Perhitungan:")
        if not riwayat:
            print("Belum ada perhitungan.")
        else:
            for i, item in enumerate(riwayat, start=1):
                print(f"{i}. {item}")

    elif pilihan == '8':
        print("\n=== Program selesai. Terima kasih telah menggunakan kalkulator bangun datar! ===")
        break

    else:
        print("Pilihan tidak valid.")

    # Tanya lanjut
    lanjut = input("\nIngin kembali ke menu utama? (y/n): ").lower()
    if lanjut != 'y':
        print("======= Program dihentikan. Sampai jumpa! =======")
        break
