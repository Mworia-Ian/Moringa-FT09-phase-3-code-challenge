import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        
        # Create a new entry in the 'magazines' table
        conn = sqlite3.connect('magazine.db')
        c = conn.cursor()
        c.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (self._id, self._name, self._category))
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        # Retrieve the name from the magazizine.db
        conn = sqlite3.connect('magazine.db')
        c = conn.cursor()
        c.execute("SELECT name FROM magazines WHERE id = ?", (self._id,))
        self._name = c.fetchone()[0]
        conn.close()
        return self._name

    @name.setter
    def name(self, new_name):
        if 2 <= len(new_name) <= 16:
            self._name = new_name
            
            # Update the name in the magazine.db
            conn = sqlite3.connect('magazine.db')
            c = conn.cursor()
            c.execute("UPDATE magazines SET name = ? WHERE id = ?", (self._name, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Name must be between 2 and 16 characters, inclusive.")

    @property
    def category(self):
        # Retrieve the category from the magazine.db
        conn = sqlite3.connect('magazine.db')
        c = conn.cursor()
        c.execute("SELECT category FROM magazines WHERE id = ?", (self._id,))
        self._category = c.fetchone()[0]
        conn.close()
        return self._category

    @category.setter
    def category(self, new_category):
        if len(new_category) > 0:
            self._category = new_category
            
            # Update the category in the magazine.db
            conn = sqlite3.connect('magazine.db')
            c = conn.cursor()
            c.execute("UPDATE magazines SET category = ? WHERE id = ?", (self._category, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Category must be longer than 0 characters.")