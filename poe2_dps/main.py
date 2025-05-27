from database import db
from calculator.PoE2_DPS_Checker import run_calculator

def main():
    connection = db()
    if connection:
        print("Connected to DB")
        run_calculator()
        connection.close()
        print("DB connection closed")
    else:
        print("Failed to connect to DB")

if __name__ == "__main__":
    main()
