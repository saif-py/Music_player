import tkinter as tk

root = tk.Tk()
pic = tk.PhotoImage(file=r"button.png")
b1 = tk.Button(root, image=pic)
b1.grid(row=1, column=0)

root.mainloop()
