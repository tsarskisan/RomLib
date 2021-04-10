from Book import Book

# Lists to work with

just_a_list = []
list_of_books = []

# Adds a book data to the first list and then separates it in four variables to add to the second list

book_list = open("books.txt", "r")
print("Currently added books: ")
for book in book_list.readlines():
    just_a_list.append(book.split(";"))
for entry in just_a_list:
    new_book = Book(entry[0], entry[1], entry[2], entry[3])
    list_of_books.append(new_book)


# Prints out values for each books, separated by ; sign

for b1 in list_of_books:
    book_status = ""
    if bool(b1.check_status()) == True:
        book_status = " You've read it already."
    else:
        book_status = " You have yet to read it."

    print("A book by " + b1.check_author() + " titled \"" + b1.check_title() + "\" containing " +
          b1.check_length() + " pages." + book_status)
# Takes input from user to assign to values: title, author, number of pages and y/n if user has read the book

enter_title = input("Enter book's name: ")
enter_author = input("Enter author's name: ")
for varus in list_of_books:
    if varus.check_title() == enter_title and varus.check_author() == enter_author:
        print("This book title already exist with this author!")
enter_length = input("How many pages does it have?(if not sure, enter 0) ")
enter_status = input("Have you read it yet?(Y/N) ")
if enter_status == str("Y"):
    status = True
else:
    status = False
book_list.close()

# Notification about added book


def add_book(e1, e2, e3):
    print("Book " + e1 + " written by " + e2 + " containing " + e3 + " pages was added!")

# Creates new book with parameters from user input, passes it to add book function and  writes it to the file


new_book = str(enter_title + ";" + enter_author + ";" + str(enter_length) + ";" + str(status) + ";")
add_book(enter_title, enter_author, enter_length)
book_list = open("books.txt", "a")
book_list.write("\n" + new_book)
book_list.close()
