#!/usr/bin/env python3
"""
Database initialization and management for In-N-Out locations.
"""

import sqlite3
import json
import os


def create_database(db_path='innout.db'):
    """
    Create the SQLite database and locations table.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create locations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            UNIQUE(latitude, longitude)
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database created/verified: {db_path}")


def import_locations(json_file='innout_locations.json', db_path='innout.db'):
    """
    Import locations from JSON file into the database.
    """
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found")
        return False
    
    # Read JSON data
    with open(json_file, 'r') as f:
        locations = json.load(f)
    
    print(f"Importing {len(locations)} locations...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    imported = 0
    skipped = 0
    
    for location in locations:
        try:
            cursor.execute('''
                INSERT INTO locations (latitude, longitude, city, state)
                VALUES (?, ?, ?, ?)
            ''', (
                location['latitude'],
                location['longitude'],
                location['city'],
                location['state']
            ))
            imported += 1
        except sqlite3.IntegrityError:
            # Duplicate location
            skipped += 1
    
    conn.commit()
    conn.close()
    
    print(f"Import complete: {imported} added, {skipped} skipped (duplicates)")
    return True


def get_all_locations(db_path='innout.db'):
    """
    Retrieve all locations from the database.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM locations ORDER BY state, city')
    rows = cursor.fetchall()
    
    locations = [dict(row) for row in rows]
    conn.close()
    
    return locations


def get_location_count(db_path='innout.db'):
    """
    Get the total count of locations in the database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM locations')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count


def main():
    """Main function for database operations."""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'init':
        # Initialize database only
        create_database()
    elif len(sys.argv) > 1 and sys.argv[1] == 'import':
        # Create database and import data
        create_database()
        import_locations()
        count = get_location_count()
        print(f"Total locations in database: {count}")
    else:
        print("Usage:")
        print("  python database.py init     - Create database")
        print("  python database.py import   - Create database and import from JSON")


if __name__ == "__main__":
    main()
