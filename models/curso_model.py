from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.configs import settings


class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    titulo: Mapped[str] = mapped_column(String(100))
    aulas: Mapped[int]
    horas: Mapped[int]
