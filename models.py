from sqlalchemy import  Column, String

from database import Base

class Repository(Base):
    __tablename__ = "repositories"
    id = Column(String, primary_key=True, index=True)
    user_name = Column(String, index=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    language = Column(String)
    tags = Column(String)
