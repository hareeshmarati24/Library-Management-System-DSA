class Book:
    def __init__(self, book_id, name, author):
        self.id = book_id
        self.name = name
        self.author = author
        self.is_issued = False
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        new_book = Book(book_id, name, author)

        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book

        print("Book added successfully!\n")

    def view_books(self):
        if self.head is None:
            print("No books available.\n")
            return

        print("\nLibrary Books:")
        temp = self.head
        while temp:
            status = "Issued" if temp.is_issued else "Available"
            print(f"ID: {temp.id}, Name: {temp.name}, Author: {temp.author}, Status: {status}")
            temp = temp.next
        print()

    def issue_book(self):
        if self.head is None:
            print("Library is empty.\n")
            return

        book_id = int(input("Enter Book ID to borrow: "))
        temp = self.head
        while temp:
            if temp.id == book_id:
                if not temp.is_issued:
                    temp.is_issued = True
                    print("Book borrowed successfully!\n")
                else:
                    print("Book already borrowed.\n")
                return
            temp = temp.next

        print("Book not found.\n")

    def return_book(self):
        if self.head is None:
            print("Library is empty.\n")
            return

        book_id = int(input("Enter Book ID to return: "))
        temp = self.head
        while temp:
            if temp.id == book_id:
                if temp.is_issued:
                    temp.is_issued = False
                    print("Book returned successfully!\n")
                else:
                    print("Book was not borrowed.\n")
                return
            temp = temp.next

        print("Book not found.\n")

    def delete_book(self):
        if self.head is None:
            print("Library is empty.\n")
            return

        book_id = int(input("Enter Book ID to delete: "))

        if self.head.id == book_id:
            self.head = self.head.next
            print("Book deleted successfully!\n")
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.id == book_id:
                prev.next = curr.next
                print("Book deleted successfully!\n")
                return
            prev = curr
            curr = curr.next

        print("Book not found.\n")


def main():
    library = Library()

    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.delete_book()
        elif choice == "6":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
