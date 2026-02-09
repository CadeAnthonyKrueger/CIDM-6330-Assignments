import sqlite3
import db_module

def print_dataset(conn: sqlite3.Connection, dataset: list[any], dataset_name: str):
    print(f'-------------------------------- {dataset_name} --------------------------------')
    for entry in dataset:
        print(entry)
    print(f'---------------------------------{len(dataset_name)*'-'}---------------------------------\n\n\n\n')

def main():
    conn = db_module.create_connection("air_travel.db")

    # Create Tables and seed data
    db_module.create_tables(conn)
    db_module.seed_data(conn)

    # Print all airports
    print_dataset(conn, db_module.get_airports(conn), 'Airports')

    # Insert airports and print the updated table
    db_module.insert_airport(conn, 'AMA', 'Rick Husband International Airport')
    db_module.insert_airport(conn, 'ANC', 'Ted Stevens Anchorage International Airport')
    db_module.insert_airport(conn, 'BFL', 'Meadows Field')
    print_dataset(conn, db_module.get_airports(conn), 'Airports')

    # Delete airport and print the updated table
    db_module.delete_airport(conn, 9)
    print_dataset(conn, db_module.get_airports(conn), 'Airports')

    # Update airport names and print the updated table
    db_module.update_airport_name(conn, 11, 'Rick Husband International')
    db_module.update_airport_name(conn, 12, 'Ted Stevens Anchorage International')
    print_dataset(conn, db_module.get_airports(conn), 'Airports')

    # Print flights and airports table
    print_dataset(conn, db_module.get_flights_with_airports(conn), 'Flights & Airports')

    # Print Explain Query Plan table with NO index
    print_dataset(conn, db_module.explain_query_plan(conn), 'Explain Query Plan')

    # Print Explain Query Plan table WITH index
    db_module.create_index(conn)
    print_dataset(conn, db_module.explain_query_plan(conn), 'Explain Query Plan')

    # Close connection to the db
    conn.close()

if __name__ == "__main__":
    main()
