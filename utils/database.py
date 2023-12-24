import sqlite3


class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "users_tg_id TEXT,"
                     "users_group TEXT);")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as E:
            print("CE:", E)

    def add_user(self, users_tg_id, users_group):
        self.cursor.execute(f"INSERT INTO users(users_tg_id, users_group) VALUES (?,?)",
                            (users_tg_id, users_group))
        self.connection.commit()

    def select_user(self, user_tg_id):
        users = self.cursor.execute(f"SELECT * FROM users WHERE users_tg_id = ?", (user_tg_id,))
        return users.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connection.close()