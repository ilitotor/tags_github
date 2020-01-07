from sqlalchemy.orm import Session
from fastapi import HTTPException

import models


def get_repo(db: Session, user_name, skip: int = 0, limit: int = 100):
    return db.query(models.Repository).filter(models.Repository.user_name == user_name).offset(skip).limit(limit).all()


def create_repo(db: Session, id, user_name, name='', url='', description='', language='', tags=''):
    db_create_repo = models.Repository(id=id, user_name=user_name, name=name,
                                       description=description, url=url, language=language, tags=tags)
    db.add(db_create_repo)
    db.commit()
    db.refresh(db_create_repo)
    return db_create_repo


def get_tag(db: Session, user_name, tag, id):
    db_query = db.query(models.Repository).filter(models.Repository.user_name == user_name) \
        .filter(models.Repository.id == id).all()
    return db_query


def create_tag(db: Session, id, tag, user_name):
    try:
        db_tag = db.query(models.Repository).filter(models.Repository.id == id) \
            .filter(models.Repository.user_name == user_name).all()
        for items in db_tag:
            if items.tags != '':
                items.tags += ',' + tag
            else:
                items.tags = tag
            db.commit()
        return items
    except:
        raise HTTPException(status_code=400, detail="This repository does not exist")


def remove_tag(db: Session, id, tag, user_name):
    try:
        search = "%{}%".format(tag)
        db_tag_delete = db.query(models.Repository).filter(models.Repository.id == id) \
            .filter(models.Repository.user_name == user_name)
        for items in db_tag_delete:
            if items.tags != '':
                tags_split = items.tags.split(',')
                for tag_compare in tags_split:
                    if tag_compare == tag:
                        tags_split.remove(tag)
                tags_split = str(tags_split)
                tags_split_clean = tags_split.replace("'", "")
                items.tags = tags_split_clean[1:-1]
                db.commit()
        return items
    except:
        raise HTTPException(status_code=400, detail="This tag does not exist")
