import tkinter as tk
from tkinter import ttk

# Data bela diri
data_beladiri = {
    "Silat": {
        "deskripsi": "Silat adalah seni bela diri Asia Tenggara. "
        "Fokus pada langkah, pukulan, dan elakan.",
        "latihan": "1. Kuda-kuda depan\n2. Pukulan lurus\n3. Elakan samping"
    },
    "Karate": {
        "deskripsi": "Karate dari Jepang, menekankan pukulan, tendangan, dan blok.",
        "latihan": "1. Zenkutsu dachi\n2. Gyaku zuki\n3. Gedan barai"
    },
    "Taekwondo": {
        "deskripsi": "Taekwondo Korea dikenal dengan tendangan tinggi dan cepat.",
        "latihan": "1. Ap seogi\n2. Ap chagi\n3. Momtong jireugi"
    },
    "Muay Thai": {
        "deskripsi": "Muay Thai dari Thailand. Fokus pada siku, lutut, dan clinch.",
        "latihan": "1. Jab-Cross\n2. Elbow\n3. Clinch & knee"
    },
    "Wing Chun": {
        "deskripsi": "Wing Chun adalah bela diri Cina, teknik cepat jarak dekat.",
        "latihan": "1. Tan sau\n2. Pak sau\n3. Chain punch"
    },
    "Tarung Derajat": {
        "deskripsi": "Tarung Derajat dari Indonesia, agresif dan kuat.",
        "latihan": "1. Langkah 3\n2. Kombinasi pukulan\n3. Serangan balasan"
    }
}

# Fungsi
def tampilkan_latihan():
    gaya = combo.get()
    hasil_var.set(f"Latihan Dasar - {gaya}:\n{data_beladiri[gaya]['latihan']}")

def tampilkan_deskripsi():
    gaya = combo.get()
    hasil_var.set(f"{gaya}:\n{data_beladiri[gaya]['deskripsi']}")

# Root window
root = tk.Tk()
root.title("Pelatihan Bela Diri")
root.geometry("800x500")
root.configure(bg="#1e1e1e")

# Frame utama
frame = tk.Frame(root, bg="#2e2e2e", padx=30, pady=30)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Judul
judul = tk.Label(frame, text="🔥 LATIHAN BELA DIRI", font=("Impact", 22), fg="white", bg="#2e2e2e")
judul.pack(pady=10)

# Dropdown pilihan bela diri
combo = ttk.Combobox(frame, state="readonly", font=("Arial", 14))
combo['values'] = list(data_beladiri.keys())
combo.current(0)
combo.pack(fill="x", pady=10)

# Tombol lihat deskripsi
ttk.Button(frame, text="Lihat Deskripsi", command=tampilkan_deskripsi).pack(fill="x", pady=5)

# Tombol mulai latihan
ttk.Button(frame, text="Mulai Latihan", command=tampilkan_latihan).pack(fill="x", pady=5)

# Label hasil
hasil_var = tk.StringVar()
hasil_var.set("Pilih gaya bela diri terlebih dahulu.")
hasil_label = tk.Label(frame, textvariable=hasil_var, font=("Courier", 12), fg="#ffc107", bg="#2e2e2e", justify="left")
hasil_label.pack(pady=15)

# Tombol keluar
ttk.Button(frame, text="Keluar", command=root.destroy).pack(fill="x", pady=5)

root.mainloop()
