from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def db_connection():
    conn = sqlite3.connect('movies.db')
    return conn

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Pydantic models
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

@app.get("/movies", response_model=List[Movie])
def get_movies():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "title": row[1], "genre": row[2], "year": row[3], "director_id": row[4], "rating": row[5]} for row in movies]

@app.post("/movies", response_model=Movie)
def create_movie(movie: MovieIn):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, genre, year, director_id, rating) VALUES (?, ?, ?, ?, ?)", (movie.title, movie.genre, movie.year, movie.director_id, movie.rating))
    conn.commit()
    movie_id = cursor.lastrowid
    conn.close()
    return {"id": movie_id, **movie.dict()}

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: MovieIn):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET title = ?, genre = ?, year = ?, director_id = ?, rating = ? WHERE id = ?", (movie.title, movie.genre, movie.year, movie.director_id, movie.rating, movie_id))
    conn.commit()
    conn.close()
    return {"id": movie_id, **movie.dict()}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()
    return {"message": "Movie deleted"}

@app.get("/directors", response_model=List[Director])
def get_directors():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM directors")
    directors = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "birth_year": row[2]} for row in directors]

@app.post("/directors", response_model=Director)
def create_director(director: DirectorIn):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO directors (name, birth_year) VALUES (?, ?)", (director.name, director.birth_year))
    conn.commit()
    director_id = cursor.lastrowid
    conn.close()
    return {"id": director_id, **director.dict()}

@app.put("/directors/{director_id}", response_model=Director)
def update_director(director_id: int, director: DirectorIn):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE directors SET name = ?, birth_year = ? WHERE id = ?", (director.name, director.birth_year, director_id))
    conn.commit()
    conn.close()
    return {"id": director_id, **director.dict()}

@app.delete("/directors/{director_id}")
def delete_director(director_id: int):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM directors WHERE id = ?", (director_id,))
    conn.commit()
    conn.close()
    return {"message": "Director deleted"}