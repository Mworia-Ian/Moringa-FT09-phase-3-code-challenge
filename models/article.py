from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    # Add other properties as needed

class Magazine(Base):
    __tablename__ = 'magazines'
    id = Column(Integer, primary_key=True)
    # Add other properties as needed

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    magazine_id = Column(Integer, ForeignKey('magazines.id'), nullable=False)

    author = relationship('Author')
    magazine = relationship('Magazine')

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        # Create a new entry in the database
        session.add(self)
        session.commit()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after initialization.")
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value

    def __repr__(self):
        return f'<Article {self.title}>'