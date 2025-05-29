import psycopg2

hostname = 'localhost'
dbname = 'postgres'
username = 'postgres'
pwd = 'Artorias421a'
port_id = 5432

connection = None
cur = None

try:
    connection = psycopg2.connect(
        host=hostname,
        database=dbname,
        user=username,
        password=pwd,
        port=port_id
    )

    cur = connection.cursor()

    cur.execute('DROP TABLE IF EXISTS weapons')

    # Create table with corrected types
    create_table = '''
    CREATE TABLE IF NOT EXISTS weapons (
        type VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        dps NUMERIC(5, 2),
        crit NUMERIC(5, 2))'''
    
    cur.execute(create_table)

    # Properly use placeholders
    insert_query = 'INSERT INTO weapons (type, name, dps, crit) VALUES (%s, %s, %s, %s) ON CONFLICT (type) DO NOTHING'
    values = ('crossbow', 'test_bow', 420.00, 69.00)
    cur.execute(insert_query, values)

    # Fetch and print
    cur.execute('SELECT * FROM weapons')
    for row in cur.fetchall():
        print(row)

    connection.commit()
    connection.close()

except Exception as error:
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if connection is not None:
        connection.close()