import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import math

def hitung():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operasi = combo.get()

        if operasi == "Tambah (+)":
            hasil = a + b
        elif operasi == "Kurang (-)":
            hasil = a - b
        elif operasi == "Kali (×)":
            hasil = a * b
        elif operasi == "Bagi (÷)":
            hasil = a / b
        elif operasi == "Modulus (%)":
            hasil = a % b
        elif operasi == "Pangkat (^)":
            hasil = a ** b
        elif operasi == "Akar (√a)":
            hasil = math.sqrt(a)
        elif operasi == "Log (log a)":
            hasil = math.log10(a)
        elif operasi == "Sin (sin a)":
            hasil = math.sin(math.radians(a))
        elif operasi == "Cos (cos a)":
            hasil = math.cos(math.radians(a))
        elif operasi == "Tan (tan a)":
            hasil = math.tan(math.radians(a))
        else:
            hasil = "Operasi tidak dikenal"

        hasil_var.set(f"Hasil: {hasil:.6f}")
    except Exception:
        hasil_var.set("Error")

root = tk.Tk()
root.title("Kalkulator Ilmiah")
root.attributes('-fullscreen', True)
root.configure(bg="#e754b5")

frame = tk.Frame(root, bg="white", padx=40, pady=40)
frame.pack(expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 16, "bold"), foreground="white", background="#ff69b4", padding=10)
style.map("TButton", background=[('active', '#ff85c1')])
style.configure("TCombobox", font=("Arial", 14))
style.configure("TEntry", font=("Arial", 14))

# Judul
judul = tk.Label(frame, text="📊 Kalkulator Ilmiah", font=("Arial", 28, "bold"), bg="white", fg="#e754b5")
judul.pack(pady=(0, 20))

# Input A
label1 = tk.Label(frame, text="Masukkan angka pertama (a):", font=("Arial", 14), bg="white")
label1.pack(anchor="w")
entry1 = ttk.Entry(frame, justify="center")
entry1.pack(fill="x", pady=5)
entry1.insert(0, "0")

# Input B
label2 = tk.Label(frame, text="Masukkan angka kedua (b):", font=("Arial", 14), bg="white")
label2.pack(anchor="w")
entry2 = ttk.Entry(frame, justify="center")
entry2.pack(fill="x", pady=5)
entry2.insert(0, "0")

# Operasi
label3 = tk.Label(frame, text="Pilih Operasi:", font=("Arial", 14), bg="white")
label3.pack(anchor="w", pady=(10, 0))
combo = ttk.Combobox(frame, state="readonly", font=("Arial", 14))
combo['values'] = [
    "Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)",
    "Modulus (%)", "Pangkat (^)", "Akar (√a)",
    "Log (log a)", "Sin (sin a)", "Cos (cos a)", "Tan (tan a)"
]
combo.current(0)
combo.pack(fill="x", pady=5)

# Tombol Hitung
tombol = ttk.Button(frame, text="Hitung", command=hitung)
tombol.pack(fill="x", pady=(10, 5))

# Hasil
hasil_var = StringVar()
hasil_var.set("Hasil: 0")
hasil_label = tk.Label(frame, textvariable=hasil_var, font=("Arial", 18, "bold"), bg="white", fg="#ff69b4")
hasil_label.pack(pady=(10, 10))

# Tombol keluar
exit_btn = ttk.Button(frame, text="Keluar", command=root.destroy)
exit_btn.pack(fill="x")

root.mainloop()
