from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Usuario(Base):
     __tablename__ = ''
     id = Column(Integer, primary_key=True)
     email = Column(String, nullable=False)
     nome = Column(String, nullable=False)
     

class Agenda(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     descricao = Column(String, nullable=False)
     titulo = Column(String, nullable=False)
     id_usuario = Column(String, nullable=False)
     prazo_final = Column(String, nullable=False)

engine = create_engine("sqlite:///meubanco.db", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.close()