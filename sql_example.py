import sqlite3

conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row  # rows act like dicts: row["name"]
cursor = conn.cursor()

# UNIQUE on name means the database itself refuses duplicate plants.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS plants (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL
    )
""")

plants = [
    ("Basil", "Herb"),
    ("Tomato", "Vegetable"),
    ("Lavender", "Flower"),
    ("Aloe Vera", "Succulent"),
]

# INSERT OR IGNORE skips any row that would violate the UNIQUE
# constraint, instead of raising an error. Safe to run repeatedly.
cursor.executemany(
    "INSERT OR IGNORE INTO plants (name, type) VALUES (?, ?)", plants
)
conn.commit()  # without this, the inserts are lost on exit

# Example query: only herbs. ("Herb",) needs the trailing comma
# because the parameters must be a tuple.
cursor.execute("SELECT * FROM plants WHERE name = ?", ("Lavender",))
for row in cursor.fetchall():
    print(row["id"], row["name"], row["type"])

# Convert all rows to the list of dicts your cards will use.
cursor.execute("SELECT * FROM plants ORDER BY name")
plant_dicts = [dict(row) for row in cursor.fetchall()]
print(plant_dicts)

conn.close()