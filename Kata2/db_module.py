import sqlite3

def create_connection(db_name: str) -> sqlite3.Connection:
    """Create and return a connection to a SQLite database.

    Args:
        db_name: Name of the SQLite database file.

    Returns:
        sqlite3.Connection object.
    """
    return sqlite3.connect(db_name)


def create_tables(conn: sqlite3.Connection) -> None:
    """Create airports and flights tables if they do not exist.

    Args:
        conn: An open sqlite3.Connection.
    """
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS airports (
            id INTEGER PRIMARY KEY,
            code TEXT NOT NULL,
            name TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY,
            flight_number TEXT NOT NULL,
            origin_airport_id INTEGER,
            FOREIGN KEY (origin_airport_id) REFERENCES airports(id)
        );
    """)

    conn.commit()


def seed_data(conn: sqlite3.Connection) -> None:
    """Populate the database with sample data.

    Args:
        conn: An open sqlite3.Connection.
    """
    cursor = conn.cursor()

    airports = [
        ("DFW", "Dallas/Fort Worth"),
        ("DEN", "Denver International"),
        ("LAX", "Los Angeles International"),
        ("JFK", "John F. Kennedy International"),
        ("ATL", "Hartsfield-Jackson Atlanta"),
        ("ORD", "Chicago O'Hare"),
        ("SEA", "Seattle-Tacoma International"),
        ("PHX", "Phoenix Sky Harbor"),
        ("LAS", "Harry Reid International"),
        ("MIA", "Miami International"),
    ]

    flights = [
        ("AA101", 1), ("UA202", 2), ("DL303", 3), ("SW404", 4), ("AA505", 5),
        ("UA606", 6), ("DL707", 7), ("SW808", 8), ("AA909", 9), ("UA010", 10),
        ("DL111", 1), ("SW222", 2), ("AA333", 3), ("UA444", 4), ("DL555", 5),
        ("SW666", 6), ("AA777", 7), ("UA888", 8), ("DL999", 9), ("SW123", 10),
    ]

    cursor.executemany(
        "INSERT INTO airports (code, name) VALUES (?, ?)",
        airports
    )

    cursor.executemany(
        "INSERT INTO flights (flight_number, origin_airport_id) VALUES (?, ?)",
        flights
    )

    conn.commit()