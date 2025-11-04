import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random
import time
import threading

USER_FILE = "users.json"
current_user = None
user_data = {}

data_beladiri = {
    "Silat": {"deskripsi": "Silat adalah seni bela diri tradisional dari Asia Tenggara, dikenal dengan kelincahan, teknik kuncian, dan jurus khas yang fleksibel.", "latihan": "1. Kuda-kuda\n2. Pukulan\n3. Elakan"},
    "Karate": {"deskripsi": "Karate berasal dari Jepang, menekankan kekuatan pukulan, tendangan, dan kedisiplinan tinggi.", "latihan": "1. Zenkutsu dachi\n2. Gyaku zuki\n3. Gedan barai"},
    "Taekwondo": {"deskripsi": "Taekwondo adalah bela diri dari Korea yang dikenal dengan tendangan tinggi, kecepatan, dan kombinasi teknik akrobatik.", "latihan": "1. Ap seogi\n2. Ap chagi\n3. Momtong jireugi"},
    "Muay Thai": {"deskripsi": "Muay Thai dari Thailand menonjolkan serangan siku, lutut, dan teknik clinch yang mematikan.", "latihan": "1. Jab\n2. Elbow\n3. Knee"},
    "Wing Chun": {"deskripsi": "Wing Chun adalah bela diri asal Tiongkok yang mengutamakan pertahanan jarak dekat dan reaksi cepat.", "latihan": "1. Tan sau\n2. Pak sau\n3. Chain punch"},
    "Tarung Derajat": {"deskripsi": "Tarung Derajat merupakan bela diri asli Indonesia dengan semangat keras, kuat, dan cepat.", "latihan": "1. Langkah\n2. Kombinasi\n3. Balasan"}
}

motivasi = [
    "Semangat juang tak kenal lelah!",
    "Konsisten adalah kunci keberhasilan.",
    "Kuasai dirimu, kuasai pertarungan.",
    "Satu langkah lebih dekat menjadi ahli."
]

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users():
    with open(USER_FILE, "w") as f:
        json.dump(user_data, f, indent=2)

def start_timer(timer_var):
    def countdown():
        for i in range(10, 0, -1):
            timer_var.set(f"Waktu: {i} detik")
            time.sleep(1)
        timer_var.set("Latihan selesai!")
    threading.Thread(target=countdown, daemon=True).start()

def show_main_ui():
    global current_user
    user = user_data[current_user]

    login_frame.pack_forget()

    main_frame = tk.Frame(root, bg="#2b2b2b", padx=30, pady=30)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(main_frame, text=f"🥋 Selamat Datang, {current_user}", font=("Arial", 24, "bold"),
             bg="#2b2b2b", fg="white").pack(pady=(0, 20))

    combo = ttk.Combobox(main_frame, state="readonly", font=("Arial", 14), width=30)
    combo['values'] = list(data_beladiri.keys())
    combo.current(0)
    combo.pack(pady=(0, 15))

    btn_frame = tk.Frame(main_frame, bg="#2b2b2b")
    btn_frame.pack(pady=(0, 15))

    hasil_var = tk.StringVar()
    hasil_var.set("Pilih bela diri untuk mulai.")

    motivasi_var = tk.StringVar()
    timer_var = tk.StringVar()

    xp_bar = ttk.Progressbar(main_frame, length=350, maximum=100)
    xp_bar['value'] = user["xp"]

    status_var = tk.StringVar()
    status_var.set(f"Level {user['level']} - XP: {user['xp']}/100")

    def update_level():
        if user["xp"] >= 100:
            user["level"] += 1
            user["xp"] = 0
            status_var.set(f"Naik ke Level {user['level']}!")
        save_users()

    def tambah_xp():
        user["xp"] += 25
        if user["xp"] > 100:
            user["xp"] = 100
        xp_bar['value'] = user["xp"]
        status_var.set(f"Level {user['level']} - XP: {user['xp']}/100")
        update_level()

    def tampilkan_latihan():
        gaya = combo.get()
        hasil_var.set(f"Latihan - {gaya}:\n\n{data_beladiri[gaya]['latihan']}")
        user["log"].append(gaya)
        motivasi_var.set(random.choice(motivasi))
        tambah_xp()
        start_timer(timer_var)
        save_users()

    def tampilkan_deskripsi():
        gaya = combo.get()
        deskripsi = data_beladiri[gaya]['deskripsi']
        hasil_teks = (
            f"🛡️ {gaya.upper()}\n\n"
            f"{deskripsi}\n\n"
            f"💡 Info: Gaya ini memiliki filosofi dan teknik khas yang membentuk karakter kuat dan disiplin."
        )
        hasil_var.set(hasil_teks)

    def cetak_sertifikat():
        latihan_count = len(user["log"])
        sertifikat_text = (
            f"SERTIFIKAT PELATIHAN BELA DIRI\n\n"
            f"Nama: {current_user}\n"
            f"Level: {user['level']}\n"
            f"Jumlah Latihan: {latihan_count}\n\n"
            f"Terima kasih telah berlatih dengan semangat!\n"
        )
        hasil_var.set(sertifikat_text)

    ttk.Style().configure("TButton", font=("Arial", 12), padding=8)
    ttk.Button(btn_frame, text="Deskripsi", command=tampilkan_deskripsi).grid(row=0, column=0, padx=12)
    ttk.Button(btn_frame, text="Latihan", command=tampilkan_latihan).grid(row=0, column=1, padx=12)
    ttk.Button(btn_frame, text="Cetak Sertifikat", command=cetak_sertifikat).grid(row=0, column=2, padx=12)

    tk.Label(main_frame, textvariable=hasil_var, font=("Arial", 13), fg="#ffc107",
             bg="#2b2b2b", wraplength=700, justify="left", anchor="w").pack(pady=(0, 12), fill="x")

    tk.Label(main_frame, textvariable=motivasi_var, font=("Arial", 12, "italic"),
             fg="#00ff99", bg="#2b2b2b").pack(pady=(0, 15))

    xp_bar.pack(pady=(0, 6))
    tk.Label(main_frame, textvariable=status_var, font=("Arial", 11), bg="#2b2b2b", fg="white").pack(pady=(0, 10))
    tk.Label(main_frame, textvariable=timer_var, font=("Arial", 11), bg="#2b2b2b", fg="#ffa500").pack(pady=(0, 15))
    ttk.Button(main_frame, text="Keluar", command=root.destroy).pack()

def login():
    global current_user
    u, p = username_entry.get(), password_entry.get()
    if u in user_data and user_data[u]["password"] == p:
        current_user = u
        show_main_ui()
    else:
        messagebox.showerror("Gagal", "Login salah!")

def register():
    u, p = username_entry.get(), password_entry.get()
    if u in user_data:
        messagebox.showwarning("Sudah ada", "User sudah terdaftar.")
    else:
        user_data[u] = {"password": p, "level": 1, "xp": 0, "log": []}
        save_users()
        messagebox.showinfo("Berhasil", "User berhasil dibuat!")

user_data = load_users()

root = tk.Tk()
root.title("Pelatihan Bela Diri Pro")
root.geometry("900x600")
root.configure(bg="#1e1e1e")

login_frame = tk.Frame(root, bg="#1e1e1e", padx=30, pady=30)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_frame, text="Username", bg="#1e1e1e", fg="white", font=("Arial", 12)).pack(pady=8)
username_entry = ttk.Entry(login_frame, font=("Arial", 12), width=30)
username_entry.pack()

tk.Label(login_frame, text="Password", bg="#1e1e1e", fg="white", font=("Arial", 12)).pack(pady=8)
password_entry = ttk.Entry(login_frame, show="*", font=("Arial", 12), width=30)
password_entry.pack()

ttk.Button(login_frame, text="Login", command=login).pack(pady=(20, 8))
ttk.Button(login_frame, text="Daftar Baru", command=register).pack()

root.mainloop()
