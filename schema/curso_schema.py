from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: int | None = None
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
