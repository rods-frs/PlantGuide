import sqlite3
from database.seed import plant_base_data
from database.seed import plant_water_data
from database.seed import plant_sun_data
from pathlib import Path

def start_db(db_path):
    global global_db_path
    global_db_path = db_path
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # rows act like dicts: row["name"]
    cursor = conn.cursor()

    # UNIQUE on name means the database itself refuses duplicate plants.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_data (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            search_name TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            water_per_day TEXT NOT NULL,
            size TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_water_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_name TEXT NOT NULL UNIQUE,
            water_every_days INTEGER NOT NULL,
            water_every_days_winter INTEGER,
            water_method TEXT NOT NULL,
            water_amount TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_sun_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_name TEXT NOT NULL UNIQUE,
            light_level INTEGER NOT NULL,
            best_sun_time TEXT NOT NULL,
            direct_sun_hours INTEGER NOT NULL,
            sun_notes TEXT
        )
    """)

    plants_base_data = plant_base_data()
    plants_water_data = plant_water_data()
    plants_sun_data = plant_sun_data()

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_data (name, search_name, type, water_per_day, size) VALUES (:name, :search_name,:type, :water_per_day, :size)", plants_base_data
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_water_data (search_name, water_every_days, water_every_days_winter, water_method, water_amount) VALUES (:search_name, :water_every_days, :water_every_days_winter, :water_method, :water_amount)", plants_water_data
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_sun_data (search_name, light_level, best_sun_time, direct_sun_hours, sun_notes) VALUES (:search_name, :light_level, :best_sun_time, :direct_sun_hours, :sun_notes)", plants_sun_data
    )

    conn.commit()  # without this, the inserts are lost on exit
    conn.close()

def card_query():
    conn = sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row  # rows act like dicts: row["name"]
    cursor = conn.cursor()
    cursor.execute("SELECT name, search_name, type FROM plant_data")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"name":row["name"], "search_name":row["search_name"], "type":row["type"]})
    conn.close()
    return query_return

def detail_query(plant_name):
    conn = sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM plant_data WHERE search_name='{plant_name}'")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"name":row["name"], "search_name":row["search_name"], "type":row["type"], "water":row["water_per_day"], "size":row["size"]})
    conn.close()
    return query_return

def water_query(search_name):
    conn = sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM plant_water_data WHERE search_name='{search_name}'")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"search_name":row["search_name"], "water_every_days":row["water_every_days"], "water_every_days_winter":row["water_every_days_winter"], "water_method":row["water_method"], "water_amount":row["water_amount"]})
    conn.close()
    return query_return

def sun_query(search_name):
    conn = sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM plant_sun_data WHERE search_name='{search_name}'")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"search_name":row["search_name"], "light_level":row["light_level"], "best_sun_time":row["best_sun_time"], "direct_sun_hours":row["direct_sun_hours"],"sun_notes":row["sun_notes"]})
    conn.close()
    return query_return



