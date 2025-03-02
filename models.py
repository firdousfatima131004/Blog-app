from sqlalchemy import Column , Integer , String,ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'Blog'
    id = Column(Integer, primary_key=True)
    img = Column(String, nullable=False)
    blog_name= Column(String,nullable=False)
    blog_desc = Column(String,nullable=False)
    url = Column(String, nullable=False)
    categoty = Column(String ,nullable=False)
    