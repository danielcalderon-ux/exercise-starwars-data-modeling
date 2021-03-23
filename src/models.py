import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    contraseña = Column(String(20)) 
    name = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    estatura = Column(String(250))
    fecha_nacimiento = Column(String(250))
    genero = Column(String(250))

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    poblacion = Column(Integer)
    diametro = Column(Integer)
    gravedad = Column(String(250))


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    personajes_name = Column(Integer, ForeignKey('personajes.name'))
    planetas_name = Column(Integer, ForeignKey('planetas.name'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')