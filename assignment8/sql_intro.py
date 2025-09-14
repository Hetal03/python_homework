# python_homework/assignment8/sql_intro.py
import os
import sqlite3
import sys

def create_tables(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
            UNIQUE(subscriber_id, magazine_id)
        );
        """)
        conn.commit()
        print("Tables created (or already existed).")
    except sqlite3.Error as e:
        print(f"SQLite error while creating tables: {e}")
        conn.rollback()
        raise

# ---------------------------
# Insert functions (Task 3)
# ---------------------------
def add_publisher(conn, name):
    try:
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Publisher added: {name}")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(conn, name, publisher_id):
    try:
        conn.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
        print(f"Magazine added: {name}")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists or invalid publisher_id.")

def add_subscriber(conn, name, address):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if cursor.fetchone():
        print(f"Subscriber '{name}, {address}' already exists.")
        return
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    print(f"Subscriber added: {name}, {address}")

def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        conn.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
        conn.commit()
        print(f"Subscription added: subscriber {subscriber_id} -> magazine {magazine_id} (exp: {expiration_date})")
    except sqlite3.IntegrityError:
        print(f"Subscription already exists or invalid subscriber/magazine ID.")

# ---------------------------
# Query functions (Task 4)
# ---------------------------
def show_all_subscribers(conn):
    print("\n--- All Subscribers ---")
    cursor = conn.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

def show_all_magazines_sorted(conn):
    print("\n--- All Magazines (sorted by name) ---")
    cursor = conn.execute("SELECT * FROM magazines ORDER BY name ASC")
    for row in cursor.fetchall():
        print(row)

def show_magazines_by_publisher(conn, publisher_name):
    print(f"\n--- Magazines for publisher: {publisher_name} ---")
    cursor = conn.execute("""
        SELECT m.magazine_id, m.name
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = ?
        ORDER BY m.name
    """, (publisher_name,))
    for row in cursor.fetchall():
        print(row)

# ---------------------------
# Main function
# ---------------------------
def main():
    db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "db", "magazines.db"))
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        print(f"Connected to database: {db_path}")

        create_tables(conn)

        # Populate tables with sample data (Task 3)
        add_publisher(conn, "Pearson")
        add_publisher(conn, "Springer")
        add_publisher(conn, "Oxford Press")

        add_magazine(conn, "Tech Monthly", 1)
        add_magazine(conn, "Science Weekly", 2)
        add_magazine(conn, "Literature Today", 3)

        add_subscriber(conn, "Alice Smith", "123 Main St")
        add_subscriber(conn, "Bob Johnson", "456 Oak Ave")
        add_subscriber(conn, "Charlie Lee", "789 Pine Rd")

        add_subscription(conn, 1, 1, "2025-12-31")
        add_subscription(conn, 1, 2, "2025-06-30")
        add_subscription(conn, 2, 3, "2025-11-15")

        # ---------------------------
        # Run queries (Task 4)
        # ---------------------------
        show_all_subscribers(conn)
        show_all_magazines_sorted(conn)
        show_magazines_by_publisher(conn, "Pearson")

    except sqlite3.Error as e:
        print(f"SQLite connection error: {e}")
        sys.exit(1)
    finally:
        if conn:
            try:
                conn.close()
                print("Connection closed.")
            except sqlite3.Error as e:
                print(f"Error closing connection: {e}")

if __name__ == "__main__":
    main()
