import sqlite3
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    director_id: int
    rating: float

class MovieIn(BaseModel):
    title: str
    genre: str
    year: int
    director_id: int
    rating: float

class Director(BaseModel):
    id: int
    name: str
    birth_year: int

class DirectorIn(BaseModel):
    name: str
    birth_year: int

def create_tables():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        year INTEGER NOT NULL,
        director_id INTEGER NOT NULL,
        rating REAL NOT NULL,
        FOREIGN KEY (director_id) REFERENCES directors (id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS directors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def delete_tables():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS movies")
    cursor.execute("DROP TABLE IF EXISTS directors")
    conn.commit()
    conn.close()

create_tables()