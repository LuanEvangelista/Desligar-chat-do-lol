import tkinter as tk
import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

root = tk.Tk()
root.geometry("300x100")

button_1 = tk.Button(root, text="Ligar", command=lambda: run_command("Ligar Chat Atualizado.bat"))
button_1.pack(pady=10)

button_2 = tk.Button(root, text="Desligar", command=lambda: run_command("Desligar Chat Atualizado.bat"))
button_2.pack(pady=10)

root.mainloop()
