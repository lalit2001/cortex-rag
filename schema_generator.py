
import psycopg2
import json


def get_db_metadata(connection):
    cursor = connection.cursor()

    # Query to get table names
    cursor.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """)
    tables = cursor.fetchall()

    db_info = {}

    for table in tables:
        table_name = table[0]
        # print(table_name)
        # this line to filter tables
        if "settlement" in table_name.lower():


            # Query to get column information
            cursor.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table_name}';
            """)
            columns = cursor.fetchall()

            # Query to get foreign key relationships
            cursor.execute(f"""
            SELECT
                kcu.column_name,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name
            FROM 
                information_schema.table_constraints AS tc 
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                  AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                  ON ccu.constraint_name = tc.constraint_name
                  AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='{table_name}';
            """)
            relationships = cursor.fetchall()

            # Construct table info
            table_info = {
                "columns": [{"name": col[0], "type": col[1]} for col in columns],
                "relationships": [{"column": rel[0], "foreign_table": rel[1], "foreign_column": rel[2]} for rel in
                                  relationships]
            }

            db_info[table_name] = table_info

    return db_info


# Database connection settings
db_config = {
    "host": "localhost",
    "database": "unification-db",
    "user": "postgres",
    "password": "admin"
}

# Connect to the database
connection = psycopg2.connect(**db_config)

# Get database metadata
db_metadata = get_db_metadata(connection)

# Convert metadata to JSON string
db_metadata_json = json.dumps(db_metadata, indent=4)

# Print the JSON string
print(db_metadata_json)

# Close the connection
connection.close()
