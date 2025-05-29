from database.db import *
from calculator.PoE2_DPS_Checker import run_calculator


def main():
    connection = db()
    if connection:
        weapon_dict = run_calculator()
        
        for weapon in weapon_dict.values():
            create_table_if_not_exists(weapon, connection)
            insert_weapon_list(weapon, connection)

    else:
        print("Failed to connect to DB")

print(f"In main.py {__name__}")
if __name__ == "__main__":
    main()
