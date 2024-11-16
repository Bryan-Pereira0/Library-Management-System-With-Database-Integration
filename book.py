#class for book operations
class Book:
    #adds book
    def add_book(self, db):
        title = input("Enter book title: ")
        author_name = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")

        #check if the author exists
        check_author_query = "SELECT id FROM authors WHERE name = %s"
        author = db.fetch_one(check_author_query, (author_name,))
        if not author:
            print("Author not found. Adding new author.")
            biography = input("Enter author biography: ")
            add_author_query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            db.execute_query(add_author_query, (author_name, biography))
            author = db.fetch_one(check_author_query, (author_name,))

        author_id = author[0]

        query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (title, author_id, isbn, publication_date))
        print("Book added successfully.")
    #borrows book
    def borrow_book(self, db):
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID: "))
        borrow_date = input("Enter borrow date (YYYY-MM-DD): ")

        #check if the book exists
        check_book_query = "SELECT * FROM books WHERE id = %s"
        book = db.fetch_one(check_book_query, (book_id,))
        if not book:
            print("Book with the given ID does not exist.")
            return

        #check if the book is available
        check_query = "SELECT * FROM borrowed_books WHERE book_id = %s AND return_date IS NULL"
        result = db.fetch_one(check_query, (book_id,))
        if result:
            print("This book is currently borrowed and not available.")
            return

        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        db.execute_query(query, (user_id, book_id, borrow_date))
        update_query = "UPDATE books SET availability = 0 WHERE id = %s"
        db.execute_query(update_query, (book_id,))
        print("Book borrowed successfully.")
    #returns borrowed book
    def return_book(self, db):
        book_id = int(input("Enter book ID: "))
        return_date = input("Enter return date (YYYY-MM-DD): ")
        query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL"
        db.execute_query(query, (return_date, book_id))
        update_query = "UPDATE books SET availability = 1 WHERE id = %s"
        db.execute_query(update_query, (book_id,))
        print("Book returned successfully.")
    #searches for a specific book
    def search_book(self, db):
        title = input("Enter book title to search: ")
        query = "SELECT * FROM books WHERE title LIKE %s"
        results = db.fetch_all(query, ('%' + title + '%',))
        for row in results:
            print(row)
    #displays all books
    def display_all_books(self, db):
        query = "SELECT * FROM books"
        results = db.fetch_all(query)
        for row in results:
            print(row)