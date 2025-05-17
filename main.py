import tkinter as tk
from tkinter import messagebox
import random
import string

# ----------- توليد كلمة المرور -----------
def generer_mot_de_passe():
    try:
        total = int(entry_total.get())
        lettres = int(entry_lettres.get())
        chiffres = int(entry_chiffres.get())
        symbols = int(entry_symbols.get())

        if lettres + chiffres + symbols != total:
            messagebox.showerror("Erreur", "La somme des éléments ne correspond pas au nombre total.")
            return

        l = random.choices(string.ascii_letters, k=lettres)
        c = random.choices(string.digits, k=chiffres)
        s = random.choices(string.punctuation, k=symbols)

        code = l + c + s
        random.shuffle(code)
        password = "".join(code)

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des nombres.")

# ----------- إعداد النافذة -----------
root = tk.Tk()
root.title("Générateur de mot de passe")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# ----------- العنوان -----------
tk.Label(root, text="🔐 Générateur de mot de passe", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# ----------- إدخالات المستخدم -----------
def champ(label_text):
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=5)
    tk.Label(frame, text=label_text, font=("Arial", 12), bg="#f0f0f0").pack(side="left")
    entry = tk.Entry(frame, width=10, font=("Arial", 12))
    entry.pack(side="left", padx=10)
    return entry

entry_total = champ("Nombre total d'expressions:")
entry_lettres = champ("Nombre de lettres:")
entry_chiffres = champ("Nombre de chiffres:")
entry_symbols = champ("Nombre de symboles:")

# ----------- زر توليد الباسورد -----------
tk.Button(root, text="Générer", font=("Arial", 12), command=generer_mot_de_passe, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

# ----------- عرض النتيجة -----------
result_var = tk.StringVar()
tk.Label(root, text="Mot de passe généré:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=30, justify="center").pack(pady=5)

# ----------- زر خروج -----------
tk.Button(root, text="Quitter", font=("Arial", 11), command=root.quit, bg="#f44336", fg="white", padx=10, pady=5).pack(pady=15)

# ----------- إطلاق البرنامج -----------
root.mainloop()
