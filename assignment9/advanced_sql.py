# advanced_sql.py
import sqlite3
import os

def main():
    # Path to database
    db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "db", "lesson.db"))
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    try:
        # -----------------------------
        # Task 1: Total price of first 5 orders
        # -----------------------------
        query1 = """
        SELECT o.order_id, SUM(li.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """
        cursor.execute(query1)
        results1 = cursor.fetchall()
        print("Task 1: Order totals for first 5 orders:")
        for row in results1:
            print(row)

        # -----------------------------
        # Task 2: Average order price per customer
        # -----------------------------
        query2 = """
        SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM orders c
        LEFT JOIN (
            SELECT o.order_id, o.customer_name AS customer_name_b, SUM(li.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS order_totals
        ON c.customer_name = order_totals.customer_name_b
        GROUP BY c.customer_name;
        """
        cursor.execute(query2)
        results2 = cursor.fetchall()
        print("\nTask 2: Average order price per customer:")
        for row in results2:
            print(row)

        # -----------------------------
        # Task 3: Insert new order for Perez and Sons
        # -----------------------------
        print("\nTask 3: Insert new order and line items for Perez and Sons...")

        # Get employee_id (using Miranda Harris)
        cursor.execute("SELECT employee_id FROM employees WHERE first_name='Miranda' AND last_name='Harris';")
        employee_id = cursor.fetchone()[0]

        # Get product_ids of 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert new order
        cursor.execute(
            "INSERT INTO orders (customer_name, order_date, employee_id) VALUES (?, DATE('now'), ?) RETURNING order_id;",
            ('Perez and Sons', employee_id)
        )
        order_id = cursor.fetchone()[0]

        # Insert line items
        for pid in product_ids:
            cursor.execute(
                "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
                (order_id, pid, 10)
            )

        conn.commit()

        # Print line items for the new order
        cursor.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?;
        """, (order_id,))
        new_line_items = cursor.fetchall()
        print(f"\nInserted line items for order_id {order_id}:")
        for row in new_line_items:
            print(row)

        # -----------------------------
        # Task 4: Employees with more than 1 order
        # -----------------------------
        print("\nTask 4: Employees with more than 1 order:")
        query4 = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 1;
        """
        cursor.execute(query4)
        results4 = cursor.fetchall()
        for row in results4:
            print(row)

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        conn.close()
        print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
