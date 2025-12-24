from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.v1.endpoints.curso import curso_route

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        field = ".".join(map(str, error["loc"][1:]))
        errors.append({"field": field, "message": exc.errors()[0]["msg"]})

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={"message": "Erro de validação", "errors": errors},
    )


app.include_router(curso_route, tags=["cursos"])
