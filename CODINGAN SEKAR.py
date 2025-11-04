import tkinter as tk
from tkinter import ttk, messagebox

def hitung_luas():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        luas = 0.5 * alas * tinggi
        hasil_var.set(f"Luas segitiga adalah {luas:.2f} cm²")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

# Window utama
root = tk.Tk()
root.title("Kalkulator Luas Segitiga")
root.geometry("400x280")
root.configure(bg="#2a2e38")

# Gaya modern
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2a2e38", foreground="white", font=("Segoe UI", 10))
style.configure("TEntry", padding=6)
style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
style.map("TButton",
    background=[("active", "#e65100"), ("!disabled", "#ff9800")],
    foreground=[("!disabled", "white")]
)

# Frame utama
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Input alas
ttk.Label(frame, text="Alas (cm):").grid(column=0, row=0, columnspan=2, sticky="w", pady=5)
entry_alas = ttk.Entry(frame, width=35)
entry_alas.grid(column=0, row=1, columnspan=2, pady=5)

# Input tinggi
ttk.Label(frame, text="Tinggi (cm):").grid(column=0, row=2, columnspan=2, sticky="w", pady=5)
entry_tinggi = ttk.Entry(frame, width=35)
entry_tinggi.grid(column=0, row=3, columnspan=2, pady=5)

# Tombol Hitung & Keluar sejajar
ttk.Button(frame, text="Hitung Luas", command=hitung_luas).grid(column=0, row=4, pady=15, sticky="ew", padx=(0, 10))
ttk.Button(frame, text="Keluar", command=root.quit).grid(column=1, row=4, pady=15, sticky="ew")

# Hasil
hasil_var = tk.StringVar()
ttk.Label(frame, textvariable=hasil_var, font=("Segoe UI", 10, "italic"), foreground="cyan").grid(column=0, row=5, columnspan=2, pady=10)

# Kolom rata
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Jalankan
root.mainloop()
