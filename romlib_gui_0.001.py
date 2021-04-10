from tkinter import *
from Book import Book


# Lists to work with ============================

just_a_list = []
list_of_books = []

# Adds a book data to the first list and then separates it in four variables to add to the second list

book_list = open("books.txt", "r")
for book in book_list.readlines():
    just_a_list.append(book.split(";"))
for entry in just_a_list:
    new_book = Book(entry[0], entry[1], entry[2], entry[3])
    list_of_books.append(new_book)


root = Tk()

# Top of the window ============================

f1 = LabelFrame(root, text="List of books")
f1.pack()

l1 = Label(f1, text="Title", width=30,
           borderwidth=1, relief="solid")
l1.pack(side=LEFT)

l2 = Label(f1, text="Author", width=30,
           borderwidth=1, relief="solid")
l2.pack(side=LEFT)

l3 = Label(f1, text="Pages", width=30,
           borderwidth=1, relief="solid")
l3.pack(side=LEFT)

l4 = Label(f1, text="Fin", width=10,
           borderwidth=1, relief="solid")
l4.pack(side=LEFT)

# Main book list window ============================

f2 = Frame(master=root).pack()

# List of books ============================

for book in list_of_books:
    fbook = Frame(master=f2)
    fbook.pack()
    books_title = Label(fbook, text=book.check_title(), width=30)
    books_title.pack(side=LEFT)

    books_author = Label(fbook, text=book.check_author(), width=30)
    books_author.pack(side=LEFT)

    books_pages = Label(fbook, text=book.check_length(), width=30)
    books_pages.pack(side=LEFT)
    book_bool = " "
    if not book.check_status():
        book_bool = "No"
    else:
        book_bool = "Yes"
    books_status = Label(fbook, text=book_bool, width=10)
    books_status.pack(side=LEFT)


# Entry fields ============================

f3 = LabelFrame(root, text="New book", width=120)
f3.pack()

lb1 = Label(f3, text="Title: ")
lb1.pack(side=LEFT)
e1 = Entry(f3)
e1.pack(side=LEFT, padx="5", pady="5")

lb2 = Label(f3, text="Author: ")
lb2.pack(side=LEFT, padx="5", pady="5")
e2 = Entry(f3)
e2.pack(side=LEFT, padx="5", pady="5")

lb3 = Label(f3, text="Number of pages: ")
lb3.pack(side=LEFT, padx="5", pady="5")
e3 = Entry(f3)
e3.pack(side=LEFT, padx="5", pady="5")

finished = IntVar()
finished.set(0)

e4 = Checkbutton(f3, text="Fin", variable=finished, onvalue=1, offvalue=0)
e4.pack(side=LEFT, padx="5", pady="5")

# Buttons ============================

f4 = Frame(root, width=120)
f4.pack()

but_save = Button(f4, text="Save", width=5)
but_save.pack(side=RIGHT, pady="5", padx="5")

root.mainloop()
