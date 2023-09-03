import mysql.connector
from prettytable import PrettyTable

host = "localhost"
user = "root"
password = "1234"

def create_connection(database_name):
    return mysql.connector.connect(host=host, user=user, password=password, database=database_name)

def create_table(conn):
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS place (
      place_name VARCHAR(255) NOT NULL,
      place_type VARCHAR(255) NOT NULL,
      reviews TEXT,
      rating FLOAT,
      price_range VARCHAR(255),
      opening_hours VARCHAR(255),
      website VARCHAR(255),
      contact_number VARCHAR(255)
    );
    """)
    conn.commit()
    print("Table 'place' created successfully.")

def add_place(conn, place_name, place_type, reviews, rating, price_range, opening_hours, website, contact_number):
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO place (place_name, place_type, reviews, rating, price_range, opening_hours, website, contact_number)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """, (place_name, place_type, reviews, rating, price_range, opening_hours, website, contact_number))
    conn.commit()
    print("Place added successfully.")

def search_place(conn, place_name):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM place WHERE place_name = %s;", (place_name,))
    place_details = cursor.fetchone()

    if place_details:
        print("Place Details:")
        table = PrettyTable(["Place Name", "Place Type", "Reviews", "Rating", "Price Range", "Opening Hours", "Website", "Contact Number"])
        table.add_row(place_details)
        print(table)
    else:
        print(f"Place '{place_name}' not found.")

def search_by_contact_number(conn, contact_number):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM place WHERE contact_number = %s;", (contact_number,))
    places = cursor.fetchall()

    if places:
        print(f"Places with contact number '{contact_number}':")
        table = PrettyTable(["Place Name"])
        for place in places:
            table.add_row([place[0]])
        print(table)
    else:
        print(f"No places found with contact number '{contact_number}'.")

def delete_place(conn, place_name):
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM place WHERE place_name = %s;", (place_name,))
    conn.commit()
    print(f"Place '{place_name}' deleted successfully.")

def search_by_price_range(conn, min_price, max_price):
    if min_price > max_price:
        raise ValueError("Minimum price must be less than or equal to maximum price")
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM place WHERE rating BETWEEN %s AND %s;", (min_price, max_price))
    places = cursor.fetchall()

    if places:
        print(f"Places in price range {min_price} to {max_price}:")
        table = PrettyTable(["Place Name"])
        for place in places:
            table.add_row([place[0]])
        print(table)
    else:
        print(f"No places found in the price range {min_price} to {max_price}.")

def sort_by_opening_hours(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM place ORDER BY opening_hours;")
    sorted_places = cursor.fetchall()

    if sorted_places:
        print("Places sorted by opening hours:")
        table = PrettyTable(["Place Name", "Opening Hours"])
        for place in sorted_places:
            table.add_row([place[0], place[5]])
        print(table)
    else:
        print("No places found in the database.")

while True:
    print("\nMenu:")
    print("1. Create Table")
    print("2. Add a Place")
    print("3. Search for a Place")
    print("4. Search by Contact Number")
    print("5. Delete a Place")
    print("6. Search by Price Range")
    print("8. Sort by Opening Hours")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        create_table(conn)
        conn.close()

    elif choice == "2":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        place_name = input("Enter the name of the place: ")
        place_type = input("Enter the type of the place: ")
        reviews = input("Enter the reviews of the place: ")
        rating = float(input("Enter the rating of the place: "))
        price_range = input("Enter the price range of the place: ")
        opening_hours = input("Enter the opening hours of the place: ")
        website = input("Enter the website of the place: ")
        contact_number = input("Enter the contact number of the place: ")
        add_place(conn, place_name, place_type, reviews, rating, price_range, opening_hours, website, contact_number)
        conn.close()

    elif choice == "3":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        place_name = input("Enter the name of the place to search for: ")
        search_place(conn, place_name)
        conn.close()

    elif choice == "4":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        contact_number = input("Enter the contact number to search for: ")
        search_by_contact_number(conn, contact_number)
        conn.close()

    elif choice == "5":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        place_name = input("Enter the name of the place to delete: ")
        delete_place(conn, place_name)
        conn.close()

    elif choice == "6":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        search_by_price_range(conn, min_price, max_price)
        conn.close()

    elif choice == "8":
        database_name = input("Enter the database name: ")
        conn = create_connection(database_name)
        sort_by_opening_hours(conn)
        conn.close()

    elif choice == "9":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
