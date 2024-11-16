#class for all author operations

class Author:
    #adds author
    def add_author(self, db):
        name = input("Enter author name: ")
        biography = input("Enter biography: ")
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        db.execute_query(query, (name, biography))
        print("Author added successfully.")
    #displays all authors
    def display_all_authors(self, db):
        query = "SELECT * FROM authors"
        results = db.fetch_all(query)
        for row in results:
            print(row)
    #searches for a specific author
    def search_author(self, db):
        name = input("Enter author name to search: ")
        query = "SELECT * FROM authors WHERE name LIKE %s"
        results = db.fetch_all(query, ('%' + name + '%',))
        for row in results:
            print(row)