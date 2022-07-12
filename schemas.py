from pydantic import BaseModel


class CursoBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int


class CursoRequest(CursoBase):
    ...


class CursoResponse(CursoBase):
    id: int

    class Config:
        orm_mode = True
