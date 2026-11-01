import sqlite3
from pathlib import Path
DB=Path(__file__).with_name("app.db")
MENU=[("Espresso","Strong and concentrated"),("Cappuccino","Espresso with steamed milk"),("Latte","Smooth and milky"),("Mocha","Coffee with chocolate")]
def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    with connect() as c:
        c.execute("CREATE TABLE IF NOT EXISTS coffees(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE,description TEXT,votes INTEGER NOT NULL DEFAULT 0)")
        for name,desc in MENU: c.execute("INSERT OR IGNORE INTO coffees(name,description) VALUES(?,?)",(name,desc))
if __name__=="__main__": init_db(); print("Coffee database initialized.")
