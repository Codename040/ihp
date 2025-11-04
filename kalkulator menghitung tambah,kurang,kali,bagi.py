def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol!"
    return a / b

ulang = True
while ulang:
    print("\n=== Kalkulator Sederhana ===")
    print("Operasi yang tersedia:")
    print("a. Tambah")
    print("b. Kurang")
    print("c. Kali")
    print("d. Bagi")
    print("e. Keluar")

    pilihan = input("Pilih operasi (a/b/c/d/e): ")

    if pilihan == 'e':
        print("Udahkan?!")
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == 'a':
        print("Hasil:", tambah(angka1, angka2))
    elif pilihan == 'b':
        print("Hasil:", kurang(angka1, angka2))
    elif pilihan == 'c':
        print("Hasil:", kali(angka1, angka2))
    elif pilihan == 'd':
        print("Hasil:", bagi(angka1, angka2))
    else:
        print("Pilihan tidak valid.")

    # Konfirmasi pengulangan
    ulangi = input("Ingin menghitung lagi? (y/n): ").lower()
    if ulangi != 'y':
        print("============= Udahkan? =============!")
        break
