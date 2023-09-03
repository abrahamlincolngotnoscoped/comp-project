import mysql.connector
from prettytable import PrettyTable  # Import PrettyTable

# Function to connect to the MySQL database and create database and tables if they don't exist
def connect_to_database():
    # Connect to the MySQL server without specifying a database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
    )

    # Create the database if it doesn't exist
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library")

    conn.close()

    # Connect to the 'library' database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="library"
    )

    # Create tables if they don't exist
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DenormalizedLibrary (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            isbn VARCHAR(255),
            title VARCHAR(255),
            author_name VARCHAR(255),
            publisher_name VARCHAR(255),
            publication_date DATE,
            edition VARCHAR(255),
            genre_name VARCHAR(255),
            return_date DATE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS IssuedBooks (
            issue_id INT AUTO_INCREMENT PRIMARY KEY,
            book_id INT,
            member_name VARCHAR(255),
            due_date DATE,
            FOREIGN KEY (book_id) REFERENCES DenormalizedLibrary(book_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Membership (
            member_id INT AUTO_INCREMENT PRIMARY KEY,
            member_name VARCHAR(255)
        )
    ''')

    return conn

# Function to add a new book to the library
def add_book():
    conn = connect_to_database()
    cursor = conn.cursor()

    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author_name = input("Enter author name: ")
    publisher_name = input("Enter publisher name: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    edition = input("Enter edition: ")
    genre_name = input("Enter genre name: ")

    cursor.execute('''
        INSERT INTO DenormalizedLibrary (isbn, title, author_name, publisher_name, publication_date, edition, genre_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (isbn, title, author_name, publisher_name, publication_date, edition, genre_name))

    conn.commit()
    conn.close()
    print("Book added successfully!")

# Function to search for books by title
def search_books_by_title():
    conn = connect_to_database()
    cursor = conn.cursor()

    title = input("Enter the title to search for: ")
    cursor.execute('''
        SELECT * FROM DenormalizedLibrary WHERE title LIKE %s
    ''', ('%' + title + '%',))

    books = cursor.fetchall()

    if books:
        print("Search results:")
        table = PrettyTable(["Book ID", "ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Genre"])
        for book in books:
            table.add_row(book[0:8])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No books found with the given title.")

    conn.close()

# Function to check due books
def check_due_books():
    conn = connect_to_database()
    cursor = conn.cursor()

    today = input("Enter the current date (YYYY-MM-DD): ")
    cursor.execute('''
        SELECT title, member_name, due_date FROM DenormalizedLibrary
        WHERE due_date < %s AND return_date IS NULL
    ''', (today,))

    due_books = cursor.fetchall()

    if due_books:
        print("Due books:")
        table = PrettyTable(["Title", "Borrower", "Due Date"])
        for book in due_books:
            table.add_row(book[0:3])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No books are currently due.")

    conn.close()

# Function to mark a book as returned
def mark_book_returned():
    conn = connect_to_database()
    cursor = conn.cursor()

    book_id = input("Enter the ID of the book being returned: ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")

    cursor.execute('''
        UPDATE DenormalizedLibrary
        SET return_date = %s
        WHERE book_id = %s
    ''', (return_date, book_id))

    conn.commit()
    conn.close()
    print("Book marked as returned.")

# Function to sort books by genre
def sort_books_by_genre():
    conn = connect_to_database()
    cursor = conn.cursor()

    genre = input("Enter the genre to sort by: ")
    cursor.execute('''
        SELECT * FROM DenormalizedLibrary WHERE genre_name = %s
    ''', (genre,))

    books = cursor.fetchall()

    if books:
        print(f"Books in the {genre} genre:")
        table = PrettyTable(["Book ID", "ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Genre"])
        for book in books:
            table.add_row(book[0:8])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print(f"No books found in the {genre} genre.")

    conn.close()

# Function to search for books by publisher name
def search_books_by_publisher():
    conn = connect_to_database()
    cursor = conn.cursor()

    publisher_name = input("Enter the publisher name to search for: ")
    cursor.execute('''
        SELECT * FROM DenormalizedLibrary WHERE publisher_name LIKE %s
    ''', ('%' + publisher_name + '%',))

    books = cursor.fetchall()

    if books:
        print("Books from the publisher:")
        table = PrettyTable(["Book ID", "ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Genre"])
        for book in books:
            table.add_row(book[0:8])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No books found from the specified publisher.")

    conn.close()

# Function to search for books by publication date
def search_books_by_date():
    conn = connect_to_database()
    cursor = conn.cursor()

    publication_date = input("Enter the publication date (YYYY-MM-DD) to search for: ")
    cursor.execute('''
        SELECT * FROM DenormalizedLibrary WHERE publication_date = %s
    ''', (publication_date,))

    books = cursor.fetchall()

    if books:
        print("Books published on the specified date:")
        table = PrettyTable(["Book ID", "ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Genre"])
        for book in books:
            table.add_row(book[0:8])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No books found with the specified publication date.")

    conn.close()

# Function to search for books by author name
def search_books_by_author():
    conn = connect_to_database()
    cursor = conn.cursor()

    author_name = input("Enter the author name to search for: ")
    cursor.execute('''
        SELECT * FROM DenormalizedLibrary WHERE author_name LIKE %s
    ''', ('%' + author_name + '%',))

    books = cursor.fetchall()

    if books:
        print("Books by the author:")
        table = PrettyTable(["Book ID", "ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Genre"])
        for book in books:
            table.add_row(book[0:8])  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No books found by the specified author.")

    conn.close()

# Function to edit book details
def edit_book_details():
    conn = connect_to_database()
    cursor = conn.cursor()

    book_id = input("Enter the ID of the book you want to edit: ")
    new_title = input("Enter the new title (or press Enter to keep it unchanged): ")
    new_publication_date = input("Enter the new publication date (YYYY-MM-DD) (or press Enter to keep it unchanged): ")
    new_publisher_name = input("Enter the new publisher name (or press Enter to keep it unchanged): ")
    new_author_name = input("Enter the new author name (or press Enter to keep it unchanged): ")
    new_genre_name = input("Enter the new genre name (or press Enter to keep it unchanged): ")

    update_query = '''
        UPDATE DenormalizedLibrary
        SET
            title = COALESCE(%s, title),
            publication_date = COALESCE(%s, publication_date),
            publisher_name = COALESCE(%s, publisher_name),
            author_name = COALESCE(%s, author_name),
            genre_name = COALESCE(%s, genre_name)
        WHERE book_id = %s
    '''

    cursor.execute(update_query, (new_title, new_publication_date, new_publisher_name, new_author_name, new_genre_name, book_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Book details updated successfully.")
    else:
        print("No matching book found for the specified ID.")

    conn.close()

# Function to issue a book to a person
def issue_book():
    conn = connect_to_database()
    cursor = conn.cursor()

    book_id = input("Enter the ID of the book you want to issue: ")
    member_name = input("Enter the name of the person issuing the book: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    insert_query = '''
        INSERT INTO IssuedBooks (book_id, member_name, due_date)
        VALUES (%s, %s, %s)
    '''

    cursor.execute(insert_query, (book_id, member_name, due_date))
    conn.commit()

    if cursor.rowcount > 0:
        print("Book issued successfully.")
    else:
        print("Failed to issue the book. Please check the book ID.")

    conn.close()

# Function to add a new library member
def add_member():
    conn = connect_to_database()
    cursor = conn.cursor()

    member_name = input("Enter the name of the library member: ")

    cursor.execute('''
        INSERT INTO Membership (member_name)
        VALUES (%s)
    ''', (member_name,))

    conn.commit()
    conn.close()
    print("Library member added successfully!")

# Function to list all library members
def list_members():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Membership')

    members = cursor.fetchall()

    if members:
        print("List of Library Members:")
        table = PrettyTable(["Member ID", "Member Name"])
        for member in members:
            table.add_row(member)  # Add the relevant columns to the table

        print(table)  # Print the table
    else:
        print("No library members found.")

    conn.close()

# Function to remove a library member
def remove_member():
    conn = connect_to_database()
    cursor = conn.cursor()

    member_id = input("Enter the ID of the library member you want to remove: ")

    # First, check if the member exists
    cursor.execute('SELECT * FROM Membership WHERE member_id = %s', (member_id,))
    member = cursor.fetchone()

    if member:
        # Remove the member
        cursor.execute('DELETE FROM Membership WHERE member_id = %s', (member_id,))
        conn.commit()
        print("Library member removed successfully.")
    else:
        print("No matching library member found.")

    conn.close()

# Updated menu with additional options
def display_menu():
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Search for books by title")
    print("3. Check due books")
    print("4. Mark a book as returned")
    print("5. Sort books by genre")
    print("6. Search for books by publisher name")
    print("7. Search for books by publication date")
    print("8. Search for books by author name")
    print("9. Edit book details")
    print("10. Issue a book to a person")
    print("11. Add a new library member")
    print("12. List all library members")
    print("13. Remove a library member")
    print("14. To create database and tables if it doesnt exist")
    print("15. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        search_books_by_title()
    elif choice == '3':
        check_due_books()
    elif choice == '4':
        mark_book_returned()
    elif choice == '5':
        sort_books_by_genre()
    elif choice == '6':
        search_books_by_publisher()
    elif choice == '7':
        search_books_by_date()
    elif choice == '8':
        search_books_by_author()
    elif choice == '9':
        edit_book_details()
    elif choice == '10':
        issue_book()
    elif choice == '11':
        add_member()
    elif choice == '12':
        list_members()
    elif choice == '13':
        remove_member()  # Call the remove_member function
    elif choice == '14':
        connect_to_database()
    elif choice == '15':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

