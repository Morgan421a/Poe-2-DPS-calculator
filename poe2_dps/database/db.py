import psycopg2
from psycopg2 import sql
from database.config import config
from calculator.PoE2_DPS_Checker import run_calculator

def db():
    connection = None
    try:
        params = config()
        print('connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)
        
        crsr = connection.cursor()
        print('postgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
        
        return connection  # <-- Return connection so caller can use it

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def create_table_if_not_exists(weapon, conn):
    cursor = conn.cursor()
    table_name = weapon.type.replace(" ", "_")

    base_columns = """
        name VARCHAR(255) NOT NULL,
        total_dps NUMERIC(6, 2) NOT NULL,
        crit_chance NUMERIC(4, 2) NOT NULL,
        attacks_per_second NUMERIC(4, 2) NOT NULL,
        quality NUMERIC(5,2),
        item_level NUMERIC(4) NOT NULL,
        required_level NUMERIC(4) NOT NULL,
        rarity VARCHAR(255) NOT NULL
    """

    if weapon.type.lower() == "crossbow":
        base_columns += ", relaod_time Numeric(4,2) NOT NULL"

    create_query = sql.SQL("CREATE TABLE IF NOT EXISTS {table} ({fields})").format(
        table=sql.identifier(table_name),
        fields=sql.SQL(base_columns)
    )

    cursor.execute(create_query)
    conn.commit()
    cursor.close()

def insert_weapon_list(weapon):
    conn = psycopg2.connect(
       **config()
    )
    
    table_name = weapon.type.replace(" ", "_")
    create_table_if_not_exists(weapon, conn)
    cursor = conn.cursor()

    if weapon.type.lower() == "crossbow":
        # Insert including reload_time
        insert_query = sql.SQL("""
            INSERT INTO {table} (name, total_dps, crit_chance, attacks_per_second, reload_time,
                                 quality, item_level, required_level, rarity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """).format(table=sql.Identifier(table_name))

        cursor.execute(insert_query, (
            weapon.name,
            weapon.dps,
            weapon.critical_chance,
            weapon.attacks_per_second,
            weapon.reload_time,
            weapon.quality,
            weapon.item_level,
            weapon.required_level,
            weapon.rarity
        ))
    else:
        # Standard insert
        insert_query = sql.SQL("""
            INSERT INTO {table} (name, total_dps, crit_chance, attacks_per_second,
                                 quality, item_level, required_level, rarity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """).format(table=sql.Identifier(table_name))

        cursor.execute(insert_query, (
            weapon.name,
            weapon.dps,
            weapon.critical_chance,
            weapon.attacks_per_second,
            weapon.quality,
            weapon.item_level,
            weapon.required_level,
            weapon.rarity
        ))

    conn.commit()
    cursor.close()
    conn.close()

base_columns = """
    name VARCHAR(255) NOT NULL,
    total_dps NUMERIC(6, 2) NOT NULL,
    crit_chance NUMERIC(4, 2) NOT NULL,
    attacks_per_second NUMERIC(4, 2) NOT NULL,
    quality NUMERIC(5,2),
    item_level NUMERIC(4) NOT NULL,
    required_level NUMERIC(4) NOT NULL,
    rarity VARCHAR(255) NOT NULL
"""



if __name__ == "__main__":
    conn = db()
    if conn is not None:
        weapon_dict = run_calculator()

        for weapon in weapon_dict.values():
            create_table_if_not_exists(weapon, conn)
            insert_weapon_list(weapon)


