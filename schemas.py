from pydantic import BaseModel

class AddMovieSchema(BaseModel):
    title: str
    year: int
    overview: str

    class Config:
        orm_mode = True

class MovieSchema(BaseModel):
    id: int
    title: str
    year: int
    overview: str

    class Config:
        orm_mode = True