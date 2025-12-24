from pydantic import BaseModel


class Curso(BaseModel):
    titulo: str
    aulas: int
    horas: int


class CursoResponse(BaseModel):
    id: int
    titulo: str
    aulas: int
    horas: int
