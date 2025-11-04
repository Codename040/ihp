# Aplikasi BAKTI - Versi Python GUI (tkinter)
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import datetime
import random

USER_FILE = "users.json"
current_user = None
user_data = {}

# Load dan simpan data pengguna
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users():
    with open(USER_FILE, 'w') as f:
        json.dump(user_data, f, indent=2)

# Jendela login
def show_login():
    login_win = tk.Toplevel()
    login_win.title("Login BAKTI")
    login_win.geometry("300x250")
    login_win.configure(bg="#101820")

    def login():
        u = username_entry.get()
        p = password_entry.get()
        if u in user_data and user_data[u]['password'] == p:
            global current_user
            current_user = u
            login_win.destroy()
            show_main_ui()
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

    def register():
        u = username_entry.get()
        p = password_entry.get()
        if u in user_data:
            messagebox.showwarning("Peringatan", "Username sudah terdaftar.")
        else:
            user_data[u] = {"password": p, "level": 1, "xp": 0, "log": []}
            save_users()
            messagebox.showinfo("Berhasil", "Akun berhasil dibuat!")

    tk.Label(login_win, text="Username", bg="#101820", fg="white").pack(pady=5)
    username_entry = tk.Entry(login_win)
    username_entry.pack()

    tk.Label(login_win, text="Password", bg="#101820", fg="white").pack(pady=5)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack()

    ttk.Button(login_win, text="Login", command=login).pack(pady=10)
    ttk.Button(login_win, text="Daftar Baru", command=register).pack()

# UI utama aplikasi setelah login
def show_main_ui():
    user = user_data[current_user]
    today = datetime.date.today().isoformat()

    header = tk.Label(root, text=f"👊 Selamat datang, {current_user}", font=("Helvetica", 15, "bold"), bg="#101820", fg="#FFD700")
    header.pack(pady=10)

    xp_var = tk.StringVar()
    xp_var.set(f"Level {user['level']} - XP: {user['xp']}/100")
    xp_bar = ttk.Progressbar(root, length=300, maximum=100)
    xp_bar['value'] = user['xp']
    xp_bar.pack()
    tk.Label(root, textvariable=xp_var, bg="#101820", fg="white").pack()

    motivasi = random.choice([
        "Disiplin membentuk karakter sejati",
        "Kekuatan lahir dari ketenangan",
        "Latihan hari ini adalah kemenangan esok"
    ])
    tk.Label(root, text=motivasi, font=("Helvetica", 10, "italic"), bg="#101820", fg="#FF4500").pack(pady=5)

    def tambah_xp():
        user['xp'] += 25
        if user['xp'] >= 100:
            user['xp'] = 0
            user['level'] += 1
            messagebox.showinfo("Level Up!", f"Selamat! Kamu naik ke level {user['level']}")
        xp_bar['value'] = user['xp']
        xp_var.set(f"Level {user['level']} - XP: {user['xp']}/100")
        save_users()

    def log_harian():
        if today not in user['log']:
            user['log'].append(today)
            save_users()

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", pady=10)

    # Tab Latihan Fisik
    tab_fisik = tk.Frame(notebook, bg="#1A1A1A")
    notebook.add(tab_fisik, text="Latihan Fisik")
    tk.Label(tab_fisik, text="Checklist Harian", bg="#1A1A1A", fg="#FFD700").pack(pady=8)
    for item in ["Stretching", "Kardio", "Push-Up", "Sit-Up", "Squat", "Pukulan", "Tendangan"]:
        tk.Checkbutton(tab_fisik, text=item, bg="#1A1A1A", fg="white").pack(anchor='w', padx=20)
    ttk.Button(tab_fisik, text="Selesai", command=lambda:[tambah_xp(), log_harian(), messagebox.showinfo("Sukses", "XP ditambah dan latihan dicatat")]).pack(pady=10)

    # Tab Mental
    tab_mental = tk.Frame(notebook, bg="#1A1A1A")
    notebook.add(tab_mental, text="Latihan Mental")
    for item in ["Meditasi Napas", "Visualisasi Diri", "Audio Motivasi", "Refleksi Emosi"]:
        tk.Checkbutton(tab_mental, text=item, bg="#1A1A1A", fg="white").pack(anchor='w', padx=20)
    ttk.Button(tab_mental, text="Simpan Refleksi", command=lambda: messagebox.showinfo("Refleksi", "Latihan mental tersimpan"))\
        .pack(pady=10)

    # Tab Moral
    tab_moral = tk.Frame(notebook, bg="#1A1A1A")
    notebook.add(tab_moral, text="Tantangan Moral")
    for item in ["Disiplin Waktu", "Hormati Orang Tua", "Tidak Mengeluh", "Komitmen", "Sikap Hormat"]:
        tk.Checkbutton(tab_moral, text=item, bg="#1A1A1A", fg="white").pack(anchor='w', padx=20)
    ttk.Button(tab_moral, text="Tantangan Selesai", command=lambda: messagebox.showinfo("Tantangan", "Tantangan moral selesai!"))\
        .pack(pady=10)

    # Tab Kalender
    tab_kalender = tk.Frame(notebook, bg="#1A1A1A")
    notebook.add(tab_kalender, text="Kalender")
    tk.Label(tab_kalender, text="Log Latihan", bg="#1A1A1A", fg="#FFD700").pack(pady=8)
    for log in sorted(user['log'], reverse=True):
        tk.Label(tab_kalender, text=f"📅 {log}", bg="#1A1A1A", fg="white").pack(anchor='w', padx=20)

    # Tab Statistik
    tab_stat = tk.Frame(notebook, bg="#1A1A1A")
    notebook.add(tab_stat, text="Statistik Mingguan")
    now = datetime.date.today()
    minggu = [t for t in user['log'] if datetime.date.fromisoformat(t) >= now - datetime.timedelta(days=6)]
    tk.Label(tab_stat, text=f"📊 Latihan 7 Hari: {len(minggu)} hari", bg="#1A1A1A", fg="#FFD700").pack(pady=12)

    # Tombol Keluar
    ttk.Button(root, text="Keluar Aplikasi", command=root.quit).pack(pady=15)

# Setup awal aplikasi
root = tk.Tk()
root.title("BAKTI - Bina Akal, Kuat Tubuh, Integritas")
root.geometry("480x800")
root.configure(bg="#101820")
user_data = load_users()
show_login()
root.mainloop()
