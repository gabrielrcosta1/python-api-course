from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.configs import settings


class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    aulas: Mapped[int] = mapped_column(Integer, nullable=False)
    horas: Mapped[int] = mapped_column(Integer, nullable=False)
