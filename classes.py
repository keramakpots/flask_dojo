import sqlite3

class Post:
    x = 0


    def __init__(self):
        Post.x += 1


    def safe_to_db(self):
        conn = sqlite3.connect('db')
        cursor = conn.cursor()

        cursor.execute("UPDATE post SET counter = '{}';".format(Post.x))

        conn.commit()
        conn.close()