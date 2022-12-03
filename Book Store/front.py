from tkinter import *
from back import *

def delete_listbox():
    lb.delete(0, END)

def fill_listbox(books):
    for book in books:
        lb.insert(END, book)

window = Tk()
window.title("Book Store")
window.geometry("400x300")
window.resizable(width=False, height=False)

# =================================Labels===================================

l1 = Label(window, text="Title :")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year :")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author :")
l3.grid(row=0, column=2)

l4 = Label(window, text="ISBN :")
l4.grid(row=1, column=2)

# =================================Entries and variables and Box and Scrollbar===================================

title = StringVar()
title_entry = Entry(window, textvariable=title)
title_entry.grid(row=0, column=1)

year = StringVar()
year_entry = Entry(window, textvariable=year)
year_entry.grid(row=1, column=1)

author = StringVar()
author_entry = Entry(window, textvariable=author)
author_entry.grid(row=0, column=3)

isbn = StringVar()
isbn_entry = Entry(window, textvariable=isbn)
isbn_entry.grid(row=1, column=3)

lb = Listbox(window, width=35, height=10)
lb.grid(row=2, column=0, rowspan=8, columnspan=2)

sc = Scrollbar(window)
sc.grid(row=2, column=1, rowspan=8, columnspan=3)

lb.configure(yscrollcommand=sc.set)
sc.configure(command=lb.yview)

def selected_item(event):
    global selected
    index = lb.curselection()[0]
    selected = lb.get(index)
    title_entry.delete(0,END)
    title_entry.insert(END, selected[1])
    year_entry.delete(0, END)
    year_entry.insert(END, selected[2])
    author_entry.delete(0, END)
    author_entry.insert(END, selected[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected[4])


lb.bind("<<ListboxSelect>>", selected_item)
# =================================Buttons===================================
def view_all_command():
    delete_listbox()
    fill_listbox(View_All())

btn1 = Button(window, text="View All", width=15, command=view_all_command)
btn1.grid(row=2, column=3)

def search_command():
    delete_listbox()
    fill_listbox(Search(title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get()))

btn2 = Button(window, text="Search", width=15, command=search_command)
btn2.grid(row=3, column=3)

def add_command():
    Add(title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get())

btn3 = Button(window, text="Add", width=15, command=add_command)
btn3.grid(row=4, column=3)

def update_command():
    Update(selected[0], title_entry.get(), year_entry.get(), author_entry.get(), isbn_entry.get())

btn4 = Button(window, text="Update", width=15, command=update_command)
btn4.grid(row=5, column=3)

def delete_command():
    Delete(selected[0])

btn5 = Button(window, text="Delete", width=15, command=delete_command)
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close", width=15, command=window.destroy)
btn6.grid(row=7, column=3)

view_all_command()
window.mainloop()
