import random

print("=== GAME TEBAK ANGKA ===")
nama = input("Masukkan nama kamu: ")
print(f"Halo {nama}, saya telah memilih angka antara 1 dan 20.")
angka_rahasia = random.randint(1, 20)
kesempatan = 5

while kesempatan > 0:
    tebakan = int(input("Tebak angka: "))
    if tebakan == angka_rahasia:
        print("🎉 Selamat! Tebakan kamu benar!")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")
    
    kesempatan -= 1
    print(f"Sisa kesempatan: {kesempatan}")

if kesempatan == 0:
    print(f"😢 Maaf, kamu kalah. Angka yang benar adalah {angka_rahasia}.")

print("Terima kasih sudah bermain!")
