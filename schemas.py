from pydantic import BaseModel


class RepoBase(BaseModel):
    user_name: str = None
    name: str = None
    description: str = None
    url: str = None
    language: str = None
    tags: str = []


class RepoCreate(RepoBase):
    pass


class Repo(RepoBase):
    id: str = None

    class Config:
        orm_mode = True