from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED
from sqlalchemy.orm import Session

import models
import crud
import api
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.put("/repository/{user_name}", response_model=schemas.Repo, status_code=200)
def read_or_create_repos(response: Response, user_name: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_repo = crud.get_repo(db, skip=skip, limit=limit, user_name=user_name)
    if db_repo == []:
        results = api.run_query(user_name)  # Execute the query
        for result in results["data"]["user"]["starredRepositories"]["edges"]:
            try:
                language = result["node"]["primaryLanguage"]["name"]
            except TypeError:
                language = ''
            crud.create_repo(db, id=result["node"]["id"], user_name=user_name, name=result["node"]["name"],
                             description=result["node"]["description"], url=result["node"]["url"],
                             language= language)
        response.status_code = HTTP_201_CREATED
        return crud.create_repo
    else:
        return db_repo

@app.put("/repository/{user_name}/{id}/{tag}", response_model=schemas.Repo)
def create_tag(user_name: str, tag: str, id: str, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag=tag, user_name=user_name, id=id)
    for item in db_tag:
        if item.tags.find(tag) != -1:
            raise HTTPException(status_code=400, detail="This tag already registered")
    return crud.create_tag(db=db, tag=tag, id=id, user_name=user_name)

@app.delete("/repository/{user_name}/{id}/{tag}", response_model=schemas.Repo)
def delete_tag(user_name: str, tag: str, id: str, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag=tag, user_name=user_name, id=id)
    for item in db_tag:
        if item.tags.find(tag) == -1:
            raise HTTPException(status_code=400, detail="This tag doesn't exist ")
    return crud.remove_tag(db, tag=tag, user_name=user_name, id=id)

