import sqlite3

class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part TEXT, customer TEXT, retailer TEXT, price REAL)''')
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM parts")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cursor.execute("INSERT INTO parts (part, customer, retailer, price) VALUES (?, ?, ?, ?)", (part, customer, retailer, price))
        self.connection.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM parts WHERE id=?", (id,))
        self.connection.commit()

    def update(self, id, part, customer, retailer, price):
        self.cursor.execute("UPDATE parts SET part=?, customer=?, retailer=?, price=? WHERE id=?", (part, customer, retailer, price, id))
        self.connection.commit() 
        
    def __del__(self):
        self.connection.close()
        
#db = Database('store.db')
#db.insert("Widget", "John Doe", "Retailer A", 19.99)
#db.insert("Gadget", "Jane Smith", "Retailer B", 29.99)
#db.insert("Thingamajig", "Bob Johnson", "Retailer C", 9.99)
#db.insert("Doohickey", "Alice Brown", "Retailer D", 14.99)
#db.insert("Contraption", "Charlie Davis", "Retailer E", 24.99)
#db.insert("Gizmo", "Eve Wilson", "Retailer F", 39.99)
#db.insert("Apparatus", "Frank Miller", "Retailer G", 49.99)
                               