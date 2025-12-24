# from fastapi import APIRouter, Response, status
# from fastapi.exceptions import HTTPException

# from models import Curso, CursoResponse

# router = APIRouter()
# cursos = {
#     1: {"titulo": "Brasil do mundo", "aulas": 12, "horas": 14},
#     2: {"titulo": "Brasil do mundo w", "aulas": 123, "horas": 144},
# }


# @router.get("/cursos")
# async def get_cursos(a: str | None = None):
#     return cursos


# @router.get("/cursos/{id}", status_code=status.HTTP_200_OK)
# async def get_curso(id: int) -> dict:
#     curso = cursos.get(id)
#     if not curso:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
#         )
#     # 3 formas de fazer a mesma coisas
#     # novo = curso.copy()
#     # novo["id"] = 1
#     # return novo

#     # novo = {}  # cria novo dicionário
#     # for k, v in curso.items():
#     #     novo[k] = v  # copia cada par chave:valor
#     # novo["id"] = __import__
#     # return novo
#     return {**curso, "id": id}


# def gerar_id() -> int:
#     if cursos:
#         return max(cursos) + 1
#     return 1


# @router.post(
#     "/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED
# )
# async def create_curso(curso: Curso):
#     id = gerar_id()
#     cursos[id] = curso.model_dump()
#     return CursoResponse(id=id, **curso.model_dump())


# @router.put("/cursos/{id}")
# async def update_curso(id: int, curso: Curso):
#     if id not in cursos:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Curso com {id} não foi encontrado",
#         )
#     cursos[id] = curso.model_dump()
#     return CursoResponse(id=id, **curso.model_dump())


# @router.delete("/cursos/{id}")
# async def delete_curso(id: int):
#     if id not in cursos:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Curso com id {id} não foi encontrado",
#         )
#     del cursos[id]
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
