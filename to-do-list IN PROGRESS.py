import tkinter as tk

window = tk.Tk()




L = tk.Listbox(window)
entry_item = tk.StringVar()
greeting = tk.Label(text='Hello, User!')
greeting.pack()
add_item_entry = tk.Entry(window, text = entry_item)

def list_addition(entry_item):
    L.insert(0, entry_item)

add_item_button = tk.Button(text= 'Add', command = list_addition)
add_item_button.pack()
add_item_button.bind('<Return>', entry_item = add_item_entry)
add_item_entry.pack()   
L.pack()
window.mainloop()
