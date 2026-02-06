import tkinter as tk
root = tk.Tk()
label1 = tk.Label(root, text="Label 1")
label1.place(x=10, y=10)

button1 = tk.Button(root, text="Tombol 1")
button1.place(x=50, y=50, width=100, height=30)
root.mainloop()