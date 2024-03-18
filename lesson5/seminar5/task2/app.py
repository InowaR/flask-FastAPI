import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = [
    Movie(id=1, title='film1', description="description1", genre="Action"),
    Movie(id=2, title="film2", description="description2", genre="Comedy"),
    Movie(id=3, title="film3", description="description3", genre="Action"),
    Movie(id=4, title="film4", description="description4", genre="Action"),
    Movie(id=5, title="film5", description="description5", genre="Action"),
    Movie(id=6, title="film6", description="description6", genre="Drama"),
]


@app.get("/")
async def main():
    return movies


@app.get("/movies/")
async def get_movies_by_genre(genre: str):
    return [movie for movie in movies if movie.genre.lower() == genre.lower()]


@app.post("/movies/")
async def set_movie(movie: Movie):
    movies.append(movie)
    return {"message": "Movie added"}


@app.put("/movies")
async def rename_movie(movie: Movie):
    for i, element in enumerate(movies):
        if element == movie:
            movies[i] = movie
            return {"message": "Movie renamed"}


@app.delete("/movies")
async def delete_movie(movie: Movie):
    for i, element in enumerate(movies):
        if element == movie:
            del movies[i]
            return {"message": "Movie deleted"}
