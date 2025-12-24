from typing import List, Sequence

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from models.curso_model import CursoModel
from schema.curso_schema import CursoSchema

curso_route = APIRouter(prefix="/cursos")


@curso_route.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()
    return novo_curso


@curso_route.get("/", response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    query = select(CursoModel)
    result = await db.execute(query)
    cursos: Sequence[CursoModel] = result.scalars().all()
    return cursos
