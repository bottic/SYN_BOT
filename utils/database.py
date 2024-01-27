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
                     "users_group TEXT,"
                     "subscribe BOOLEAN,"
                     "users_chat_id);")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as E:
            print("CE:", E)

    def add_user(self, users_tg_id, users_group, users_chat_id):
        self.cursor.execute(f"INSERT INTO users(users_tg_id, users_group, subscribe, users_chat_id) VALUES "
                            f"(?,?,?,?)",
                            (users_tg_id, users_group, False, users_chat_id))
        self.connection.commit()

    def change_user(self, users_group, users_tg_id):
        self.cursor.execute(f"UPDATE users SET users_group=? WHERE users_tg_id=?", (users_group, users_tg_id))
        self.connection.commit()

    def select_user(self, user_tg_id):
        users = self.cursor.execute(f"SELECT * FROM users WHERE users_tg_id = ?", (user_tg_id,))
        return users.fetchone()

    def change_subscribe(self, user_tg_id, sub):
        self.cursor.execute(f"UPDATE users SET subscribe=? WHERE users_tg_id=?", (sub, user_tg_id))
        self.connection.commit()

    def select_all_subscribe_user(self):
        data = self.cursor.execute("SELECT users_chat_id FROM users WHERE subscribe=1")
        return data.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()