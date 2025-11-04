import tkinter as tk
from tkinter import ttk, messagebox
import math

def hitung():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Kesalahan", "Nilai a tidak boleh 0 (bukan persamaan kuadrat).")
            return

        D = b**2 - 4*a*c  # diskriminan

        # Hitung Sumbu X
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            hasil_x = f"Dua akar real:\nx₁ = {x1:.3f}, x₂ = {x2:.3f}"
        elif D == 0:
            x = -b / (2 * a)
            hasil_x = f"Akar kembar:\nx = {x:.3f}"
        else:
            hasil_x = "Tidak memiliki akar real (akar imajiner)"

        # Sumbu Y
        hasil_y = f"y = {c:.3f}"

        hasil_var.set(f"Sumbu X:\n{hasil_x}\n\nSumbu Y:\n{hasil_y}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan semua nilai (a, b, c) dengan benar.")

# Window utama
root = tk.Tk()
root.title("Kalkulator Sumbu X & Y")
root.geometry("440x400")
root.configure(bg="#e3f2fd")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#e3f2fd", foreground="#2c3e50", font=("Segoe UI", 10))
style.configure("TEntry", padding=5, relief="flat")
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.map("TButton",
          background=[("active", "#0056b3"), ("!disabled", "#007bff")],
          foreground=[("!disabled", "white")])

# Frame utama
frame = ttk.Frame(root, padding=25, style="TFrame")
frame.pack(expand=True)

# Judul
judul = ttk.Label(frame, text="🎯 Hitung Sumbu X dan Y", font=("Segoe UI", 15, "bold"), anchor="center")
judul.grid(column=0, row=0, columnspan=2, pady=(0, 12))

ttk.Label(frame, text="Persamaan: y = ax² + bx + c", font=("Segoe UI", 10, "italic")).grid(column=0, row=1, columnspan=2, pady=(0, 20))

# Input a, b, c
label_opts = {'sticky': 'w', 'pady': 4}
entry_opts = {'width': 32}

ttk.Label(frame, text="Nilai a:").grid(column=0, row=2, **label_opts)
entry_a = ttk.Entry(frame, **entry_opts)
entry_a.grid(column=1, row=2, pady=4)

ttk.Label(frame, text="Nilai b:").grid(column=0, row=3, **label_opts)
entry_b = ttk.Entry(frame, **entry_opts)
entry_b.grid(column=1, row=3, pady=4)

ttk.Label(frame, text="Nilai c:").grid(column=0, row=4, **label_opts)
entry_c = ttk.Entry(frame, **entry_opts)
entry_c.grid(column=1, row=4, pady=4)

# Tombol Hitung & Keluar
ttk.Button(frame, text="Hitung", command=hitung).grid(column=0, row=5, pady=18, sticky="ew", padx=(0, 10))
ttk.Button(frame, text="Keluar", command=root.quit).grid(column=1, row=5, pady=18, sticky="ew")

# Hasil
hasil_var = tk.StringVar()
ttk.Label(
    frame, textvariable=hasil_var,
    background="#e3f2fd", font=("Segoe UI", 10, "italic"),
    wraplength=360, justify="left", relief="solid", padding=10
).grid(column=0, row=6, columnspan=2, pady=10)

# Kolom rata
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
