from config import config

print("Starting test_config.py...")

try:
    db_config = config()
    print("Config loaded successfully:", db_config)
except Exception as e:
    print("Error:", e)