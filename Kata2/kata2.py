import sqlite3
import db_module


def main():
    conn = db_module.create_connection("air_travel.db")

    db_module.create_tables(conn)
    db_module.seed_data(conn)

    conn.close()


if __name__ == "__main__":
    main()
