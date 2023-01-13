from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database import Base, engine, Session
from schemas import AddMovieSchema
from models import Movie
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return "ok"

@app.get("/movies")
def list_movies():
    db = Session()
    result = db.query(Movie).all()
    return jsonable_encoder(result)

@app.post("/movies")
def create_movies(movie: AddMovieSchema):
    db = Session()
    insert = Movie(**movie.dict())
    db.add(insert)
    db.commit()
    return {"message": "Movie Inserted successfully"}

@app.put(f"/movies/{id}/")
def update_movie(id: int, movie_update: AddMovieSchema):
    db = Session()
    result = db.query(Movie).filter(Movie.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    for k,v in movie_update.dict().items():
        setattr(result, k, v)
    db.commit()
    return {"message": f"Movie pk: '{id}' update successfully"}

@app.get(f"/movies/{id}/")
def get_movie(id: int):
    db = Session()
    result = db.query(Movie).filter(Movie.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return jsonable_encoder(result)