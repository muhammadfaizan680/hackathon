import pyodbc
import pandas as pd
from config import SQL_CONN_STR

def load_to_sql():
    df = pd.read_csv("../banggood_clean.csv")

    conn = pyodbc.connect(SQL_CONN_STR)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO banggood_products
            (category, name, price, rating, reviews, value_score, popularity, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        row.category, row.name, row.price, row.rating,
        row.reviews, row.value_score, row.popularity, row.url)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM banggood_products")
    print("Rows Inserted:", cursor.fetchone()[0])

if _name_ == "_main_":
    load_to_sql()