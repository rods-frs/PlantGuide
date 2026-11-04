"""Database functions for creating and querying the plant SQLite database."""

import sqlite3
from database.seed import plant_base_data
from database.seed import plant_water_data
from database.seed import plant_sun_data
from database.seed import plant_recipe_data
from pathlib import Path

# Global variable to store the database path across function calls
global_db_path = None

def start_db(db_path):
    """Create the database tables and seed them with initial plant data. """
    global global_db_path
    global_db_path = db_path
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # rows act like dicts: row["name"]
    cursor = conn.cursor()

    # Table for basic plant info (name, type, size, etc.)
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

    # Table for watering schedule and method per plant
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

    # Table for sunlight requirements per plant
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

    # Table for recipes associated with each plant
    cursor.execute("""
    
        CREATE TABLE IF NOT EXISTS plant_recipe_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_name TEXT NOT NULL UNIQUE,
            recipe_name TEXT NOT NULL UNIQUE,
            main_ingredient TEXT NOT NULL UNIQUE,
            prep_time INT NOT NULL,
            step_1 TEXT NOT NULL,
            step_2 TEXT NOT NULL,
            step_3 TEXT NOT NULL
        )
    """)

    # Load seed data from the seed module
    plants_base_data = plant_base_data()
    plants_water_data = plant_water_data()
    plants_sun_data = plant_sun_data()
    plants_recipe_data = plant_recipe_data()

    # Insert seed data (IGNORE skips rows that already exist)
    cursor.executemany(
        "INSERT OR IGNORE INTO plant_data (name, search_name, type, water_per_day, size) VALUES (:name, :search_name,:type, :water_per_day, :size)", plants_base_data
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_water_data (search_name, water_every_days, water_every_days_winter, water_method, water_amount) VALUES (:search_name, :water_every_days, :water_every_days_winter, :water_method, :water_amount)", plants_water_data
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_sun_data (search_name, light_level, best_sun_time, direct_sun_hours, sun_notes) VALUES (:search_name, :light_level, :best_sun_time, :direct_sun_hours, :sun_notes)", plants_sun_data
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO plant_recipe_data (search_name, recipe_name, main_ingredient, prep_time, step_1, step_2, step_3) VALUES (:search_name, :recipe_name, :main_ingredient, :prep_time_mins, :step_1, :step_2, :step_3)", plants_recipe_data
    )

    conn.commit()  # without this, the inserts are lost on exit
    conn.close()

def card_query():
    """Fetch all plants' basic info for the plant list cards."""
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
    """Fetch full detail info for one plant by its search_name."""
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
    """Fetch watering schedule and method for one plant."""
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
    """Fetch sunlight requirements for one plant."""
    conn = sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM plant_sun_data WHERE search_name='{search_name}'")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"search_name":row["search_name"], "light_level":row["light_level"], "best_sun_time":row["best_sun_time"], "direct_sun_hours":row["direct_sun_hours"],"sun_notes":row["sun_notes"]})
    conn.close()
    return query_return

def recipe_query(search_name):
    """Fetch the recipe associated with one plant."""
    conn= sqlite3.connect(global_db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM plant_recipe_data WHERE search_name='{search_name}'")
    query_return = []
    for row in cursor.fetchall():
        query_return.append({"search_name":row["search_name"], "recipe_name":row["recipe_name"], "main_ingredient":row["main_ingredient"], "prep_time":row["prep_time"], "step_1":row["step_1"], "step_2":row["step_2"], "step_3":row["step_3"]})
    conn.close()
    return query_return


