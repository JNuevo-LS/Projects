import tkinter as tk
import os
# Color being used: #77866A

#Main window
window = tk.Tk()
window.configure(background='#77866A', highlightbackground='#77866A', highlightcolor='#77866A', highlightthickness=3)
window.overrideredirect(True)
window.geometry('200x300+200+200')

#Title bar

titlebar = tk.Frame(window, relief='raised', bd=2)
titlebar.config(bg='#77866A', bd=0)
titlebar.pack(expand=0, fill=tk.X)

#Listbox

L = tk.Listbox(window, bg='#77866A', highlightbackground='#77866A', bd=0)

#On open, read and add to listbox

if os.path.exists('listbox.txt') == True:
    previous_list_data = open(r'listbox_data.txt', 'r')
    previous_lines = previous_list_data.readlines()
    for line in previous_lines:
        if line == '':
            previous_lines.pop(line)
        else:
            L.insert(tk.END, line)
else: 
    listbox_data = open(r'listbox_data.txt', 'w')
    listbox_data.close()


#Entry

entry_item = tk.StringVar()
add_item_entry = tk.Entry(window)
add_item_entry.config(bg='#77866A', highlightbackground='#77866A', highlightcolor='#77866A', highlightthickness=1)

#Greetings
greeting = tk.Label(text='Hello, user!', bg='#77866A')
greeting.pack(side=tk.TOP)

#To-do-list commands

def list_addition():
    entry_item = add_item_entry.get()
    L.insert(tk.END, entry_item + '\n')

def bound_addition(text):
    text = add_item_entry.get()
    L.insert(tk.END, text)

def remove_from_list():
    L.delete(tk.END)

def move_window(event):
    window.geometry('+{0}+{1}'.format(event.x_root, event.y_root)) 

#Save content
# Still working on the ability to save the to-do-list items
def save_list_data(): 
    listbox_data = open(r'listbox_data.txt', 'w')
    for item in L.get(0, tk.END):
        item = item.rstrip('\n')
        listbox_data.write(str(item) + '\n')
    listbox_data.close()

#Add and remove item buttons, plus bind

add_item_button = tk.Button(window, text= 'Add', command = list_addition)
add_item_button.config(bg='#77866A', highlightbackground='#77866A', highlightcolor='#77866A', highlightthickness=1)
remove_item_button = tk.Button(window, text= 'Remove last item', command = remove_from_list)
remove_item_button.config(bg='#77866A', highlightbackground='#77866A', highlightcolor='#77866A', highlightthickness=1)
add_item_button.pack()
window.bind('<Return>', bound_addition)
titlebar.bind('<B1-Motion>', move_window)

#Close button (X)

def on_close():
    save_list_data()
    window.destroy()

close_button = tk.Button(titlebar, text='X', command= on_close)
close_button.config(bg='#77866A', bd=0)
close_button.pack(side=tk.RIGHT)



window.protocol('WM_DELETE_WINDOW', on_close)


add_item_entry.pack()
L.pack()
remove_item_button.pack()
window.mainloop()

