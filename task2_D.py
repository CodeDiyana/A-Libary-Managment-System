class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.__borrowed_books = []

    def borrow_book(self, book):
        if not book.is_available:
            print("Book not available")
            return
        self.__borrowed_books.append(book)
        book.is_available = False
        book.borrowed_by = self.name
        print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.is_available = True
            book.borrowed_by = None
            print(f"{self.name} returned '{book.title}'")


class StudentMember(Member):
    def __init__(self, member_id, name, student_id):
        super().__init__(member_id, name)
        self.student_id = student_id
        self._borrow_limit = 3


class TeacherMember(Member):
    def __init__(self, member_id, name, employee_id):
        super().__init__(member_id, name)
        self.employee_id = employee_id
        self._borrow_limit = 10


class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)

    def add_member(self, member):
        self.__members.append(member)

    def display_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.__books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"  [{book.book_id}] {book.title} by {book.author} - {status}")

    def display_members(self):
        print(f"\nMembers of {self.name}:")
        for member in self.__members:
            member_type = type(member).__name__
            print(f"  [{member.member_id}] {member.name} - {member_type}")

    def display_borrowed_books(self):
        print(f"\nBorrowed Books:")
        borrowed = [book for book in self.__books if not book.is_available]
        if borrowed:
            for book in borrowed:
                print(f"  [{book.book_id}] {book.title} - Borrowed by: {book.borrowed_by}")
        else:
            print("  No books currently borrowed")


if __name__ == "__main__":
    library = Library("City Library")

    book1 = Book("B001", "Python Programming", "John Smith")
    book2 = Book("B002", "Data Structures", "Jane Doe")

    student = StudentMember("M001", "Emma", "S123")
    teacher = TeacherMember("M002", "Dr. Sarah", "T001")

    library.add_book(book1)
    library.add_book(book2)
    library.display_books()
    library.add_member(student)
    library.add_member(teacher)
    library.display_members()

    student.borrow_book(book1)
    teacher.borrow_book(book2)

    library.display_borrowed_books()

    student.return_book(book1)
    library.display_borrowed_books()
