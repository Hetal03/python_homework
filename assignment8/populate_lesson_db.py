# python_homework/assignment8/populate_lesson_db.py
import os
import sqlite3

def main():
    db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "db", "lesson.db"))
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS line_items (
            line_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    """)

    # Insert sample products
    products = [
        ("Laptop", 1200.0),
        ("Smartphone", 800.0),
        ("Headphones", 150.0),
        ("Keyboard", 75.0)
    ]
    cursor.executemany("INSERT INTO products (product_name, price) VALUES (?, ?)", products)

    # Insert sample line_items
    line_items = [
        (1, 2),  # 2 Laptops
        (2, 5),  # 5 Smartphones
        (3, 10), # 10 Headphones
        (4, 3),  # 3 Keyboards
        (1, 1),  # 1 Laptop
        (2, 2)   # 2 Smartphones
    ]
    cursor.executemany("INSERT INTO line_items (product_id, quantity) VALUES (?, ?)", line_items)

    conn.commit()
    print("lesson.db populated with sample data.")
    conn.close()

if __name__ == "__main__":
    main()
