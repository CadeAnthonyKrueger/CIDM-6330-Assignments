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
            code TEXT NOT NULL UNIQUE,
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
    """Populate the database with sample data if empty.

    Args:
        conn: An open sqlite3.Connection.
    """
    cursor = conn.cursor()

    # Check if airports already have data
    cursor.execute("SELECT COUNT(*) FROM airports")
    count = cursor.fetchone()[0]

    if count > 0:
        # Data already seeded, do nothing
        return

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


def insert_airport(conn: sqlite3.Connection, code: str, name: str) -> None:
    """Insert or update an airport record by code.

    Args:
        conn: An open sqlite3.Connection.
        code: Airport code.
        name: Airport name.
    """
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO airports (code, name)
        VALUES (?, ?)
        ON CONFLICT(code) DO UPDATE SET
            name = excluded.name
    """, (code, name))

    conn.commit()


def get_airports(conn: sqlite3.Connection):
    """Retrieve all airports.

    Args:
        conn: An open sqlite3.Connection.

    Returns:
        List of airport rows.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM airports")
    return cursor.fetchall()


def update_airport_name(conn: sqlite3.Connection, airport_id: int, new_name: str) -> None:
    """Update the name of an airport.

    Args:
        conn: An open sqlite3.Connection.
        airport_id: ID of the airport to update.
        new_name: New airport name.
    """
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE airports SET name = ? WHERE id = ?",
        (new_name, airport_id)
    )
    conn.commit()


def delete_airport(conn: sqlite3.Connection, airport_id: int) -> None:
    """Delete an airport record.

    Args:
        conn: An open sqlite3.Connection.
        airport_id: ID of the airport to delete.
    """
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM airports WHERE id = ?",
        (airport_id,)
    )
    conn.commit()

def get_flights_with_airports(conn: sqlite3.Connection):
    """Return flights joined with airport information.

    Args:
        conn: An open sqlite3.Connection.

    Returns:
        Joined flight and airport rows.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT flights.flight_number, airports.code, airports.name
        FROM flights
        JOIN airports ON flights.origin_airport_id = airports.id
    """)
    return cursor.fetchall()

def create_index(conn: sqlite3.Connection) -> None:
    """Create an index on flights.origin_airport_id to improve query performance.

    Args:
        conn: An open sqlite3.Connection.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_origin_airport
        ON flights(origin_airport_id)
    """)
    conn.commit()


def explain_query_plan(conn: sqlite3.Connection):
    """Return the query plan for selecting flights by airport.

    Args:
        conn: An open sqlite3.Connection.

    Returns:
        Query plan rows.
    """
    cursor = conn.cursor()
    cursor.execute("""
        EXPLAIN QUERY PLAN
        SELECT * FROM flights WHERE origin_airport_id = ?
    """, (1,))
    return cursor.fetchall()
