# --- database.py ---
import sqlite3
from TECH_NOTEBOOK_APP_SQLITE.config import DB_PATH

def create_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # return rows as dict-like objects
    return conn


def initialize_database():
    """Create all required tables if they do not exist."""
    conn = create_connection()
    cursor = conn.cursor()

    # ------------------------------
    # WORK ORDERS TABLE
    # ------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wo_number TEXT,
            customer_first TEXT,
            customer_last TEXT,
            customer_tag TEXT,
            machine_id INTEGER,
            engine_id INTEGER,
            machine_type TEXT,
            machine_make TEXT,
            machine_model TEXT,
            machine_model_number TEXT,
            machine_serial_number TEXT,
            machine_year TEXT,
            engine_make TEXT,
            engine_model TEXT,
            engine_model_number TEXT,
            engine_serial_number TEXT,
            status TEXT,
            created_on TEXT,
            updated_on TEXT
        )
    """)

    # ------------------------------
    # MACHINES TABLE
    # ------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_number TEXT,
            type TEXT,
            make TEXT,
            model TEXT,
            model_number TEXT,
            serial_number TEXT,
            year TEXT
        )
    """)

    # ------------------------------
    # ENGINES TABLE
    # ------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id INTEGER,
            make TEXT,
            model TEXT,
            model_number TEXT,
            serial_number TEXT,
            FOREIGN KEY(machine_id) REFERENCES machines(id)
        )
    """)

    # ------------------------------
    # PARTS TABLE
    # ------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            part_id INTEGER PRIMARY KEY AUTOINCREMENT,
            wo_id INTEGER,
            quantity INTEGER,
            description TEXT,
            part_number TEXT,
            location TEXT,
            our_cost REAL,
            retail_cost REAL,
            supplier TEXT,
            status TEXT,
            po_number TEXT,
            ordered_on TEXT,
            received_on TEXT,
            pulled_on TEXT,
            FOREIGN KEY(wo_id) REFERENCES work_orders(id)
        )
    """)

    # ------------------------------
    # NOTES TABLE
    # ------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wo_id INTEGER,
            section TEXT,
            note_text TEXT,
            FOREIGN KEY(wo_id) REFERENCES work_orders(id)
        )
    """)

    conn.commit()
    conn.close()
    print("[DB] initialize_database() completed")
