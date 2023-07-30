#!/usr/bin/env python3
class Song:
    all = []  # Class variable to store all song instances

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        cls.all = [cls(*row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM songs
            WHERE name = ?
            LIMIT 1
        """

        song = CURSOR.execute(sql, (name,)).fetchone()

        return cls.new_from_db(song)

from song import Song, CONN, CURSOR

def reset_database():
    Song.drop_table()
    Song.create_table()
    Song.create("Hello", "25")
    Song.create("99 Problems", "The Black Album")


if __name__ == '__main__':
    reset_database()
    import ipdb; ipdb.set_trace()
