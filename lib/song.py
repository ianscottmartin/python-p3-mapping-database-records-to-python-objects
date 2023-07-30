import sqlite3
from config import CURSOR


class Song:
    all = []  # List to store all song instances

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

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))

        # Fetch the last inserted row id
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

    @classmethod
    def new_from_db(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]
        return song

    @classmethod
    def all(cls):
        sql = """
            SELECT *
            FROM songs
        """
        all_songs = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all_songs]
        return cls.all
