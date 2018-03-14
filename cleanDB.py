#!venv/bin/python
from dbmanager import DBManager

manager = DBManager()

print("Cleaning DB...")
try:
    manager.cleanDB()
    print("DB Cleaned!")
except Exception as e:
    print("ERRROR!")
    print(e)
