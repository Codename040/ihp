import random

def mulai_game():
    print("=== GAME TEBAK ANGKA LEVEL UP ===")
    nama = input("Masukkan nama kamu: ")
    print(f"Halo {nama}! Siap menantang otakmu? 😎")

    level = 1
    skor = 0

    while True:
        batas_atas = level * 10
        angka_rahasia = random.randint(1, batas_atas)
        kesempatan = max(5 - (level // 3), 2)

        print(f"\n🔢 Level {level} - Tebak angka antara 1 dan {batas_atas}")
        print(f"💡 Kamu punya {kesempatan} kesempatan")

        menang = False
        for i in range(kesempatan):
            try:
                tebakan = int(input("Tebakanmu: "))
            except ValueError:
                print("⚠️ Masukkan angka yang valid.")
                continue

            if tebakan == angka_rahasia:
                print("🎉 Keren! Tebakan kamu benar!")
                menang = True
                skor += 10 * level
                # Bonus kesempatan jika menang cepat
                if i == 0:
                    skor += 5
                    print("⚡ Bonus! Kamu menebak dalam 1 kali.")
                break
            elif tebakan < angka_rahasia:
                print("📉 Terlalu kecil!")
            else:
                print("📈 Terlalu besar!")
            print(f"Kesempatan tersisa: {kesempatan - i - 1}")

        if not menang:
            print(f"😢 Kamu kalah di level {level}. Angkanya adalah {angka_rahasia}.")
            break
        else:
            level += 1
            lanjut = input("Lanjut ke level berikutnya? (y/n): ").lower()
            if lanjut != 'y':
                break

    print("\n=== GAME SELESAI ===")
    print(f"Level terakhir: {level}")
    print(f"Skor akhir: {skor}")
    print("Terima kasih sudah bermain! 🎮")

# Mulai game
mulai_game()