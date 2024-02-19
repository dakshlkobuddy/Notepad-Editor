import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

def save_file():
    file_path = asksaveasfilename(defaultextension='.txt')
    with open(file_path, 'w') as file:
        text = text_area.get('1.0', tk.END)
        file.write(text)

def open_file():
    file_path = askopenfilename(defaultextension='.txt')
    with open(file_path, 'r') as file:
        text = file.read()
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, text)

root = tk.Tk()
root.title("Notepad")

text_area = tk.Text(root, height=30, width=80)
text_area.pack()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()


