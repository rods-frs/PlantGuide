import sqlite3
from database.seed import return_plants_data

def start_db():
    conn = sqlite3.connect("plants.db")
    conn.row_factory = sqlite3.Row  # rows act like dicts: row["name"]
    cursor = conn.cursor()

    # UNIQUE on name means the database itself refuses duplicate plants.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plants (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            water_per_day TEXT NOT NULL,
            size TEXT NOT NULL
        )
    """)

    plants_original_data = return_plants_data

    cursor.executemany(
        "INSERT OR IGNORE INTO plants (name, type, water_per_day, size) VALUES (?, ?, ?, ?)", plants_original_data
    )

    conn.commit()  # without this, the inserts are lost on exit
    conn.close()

def card_query():
    cursor.execute("SELECT name, type FROM plants")
    query_return = [{}]
    for row in cursor.fetchall():
        query_return.append({row["name"], row["type"]})
    return query_return

# Convert all rows to the list of dicts your cards will use.
#cursor.execute("SELECT * FROM plants ORDER BY name")
#plant_dicts = [dict(row) for row in cursor.fetchall()]
#print(plant_dicts)

