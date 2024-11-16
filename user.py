#class for user operations
class User:
    #adds user
    def add_user(self, db):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        db.execute_query(query, (name, library_id))
        print("User added successfully.")
    #displays all users 
    def display_all_users(self, db):
        query = "SELECT * FROM users"
        results = db.fetch_all(query)
        for row in results:
            print(row)
    #searches for a specific user
    def search_user(self, db):
        name = input("Enter user name to search: ")
        query = "SELECT * FROM users WHERE name LIKE %s"
        results = db.fetch_all(query, ('%' + name + '%',))
        for row in results:
            print(row)