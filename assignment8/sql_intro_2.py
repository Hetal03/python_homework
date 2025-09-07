# python_homework/assignment8/sql_intro_2.py
import os
import sqlite3
import pandas as pd

def main():
    # Path to lesson.db (relative to this script)
    db_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "db", "lesson.db"))
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    print(f"Connected to database: {db_path}\n")
    
    try:
        # Step 1: Read data from JOIN of line_items and products
        query = """
        SELECT 
            line_items.line_item_id,
            line_items.quantity,
            products.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id;
        """
        
        df = pd.read_sql_query(query, conn)
        print("First 5 rows of the DataFrame:")
        print(df.head())
        
        # Step 2: Add 'total' column (quantity * price)
        df['total'] = df['quantity'] * df['price']
        print("\nDataFrame with 'total' column:")
        print(df.head())
        
        # Step 3: Group by product_id
        summary_df = df.groupby('product_id').agg({
            'line_item_id': 'count',  # count of line items
            'total': 'sum',           # total sales per product
            'product_name': 'first'   # keep product name
        }).reset_index()
        print("\nGrouped summary DataFrame:")
        print(summary_df.head())
        
        # Step 4: Sort by product_name
        summary_df = summary_df.sort_values('product_name')
        print("\nSorted summary DataFrame:")
        print(summary_df.head())
        
        # Step 5: Write to CSV in assignment8 folder
        csv_path = os.path.join(os.path.dirname(__file__), "order_summary.csv")
        summary_df.to_csv(csv_path, index=False)
        print(f"\nOrder summary written to: {csv_path}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
