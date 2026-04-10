from sqlalchemy import create_engine, Column, Integer,Boolean, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///Saúde.db", echo=False)
Session = sessionmaker(bind=engine)

class Farmacia(Base):
    __tablename__ = "farmacia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    funcionario = Column(String(100), nullable=False)
    cliente = Column(String(100), nullable=False)
    horario = Column(Boolean, nullable=False)

    medicamento = relationship("Medicamento", back_populates="farmacia")

    def __init__(self,nome):
        self.nome=nome

    def __repr__(self):
        return f"Farmacia: id={self.id} - Nome={self.nome}"
    
class Medicamento(Base):
    __tablename__ = "medicamento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    validade = Column(Boolean, nullable=False)
    preco = Column(Float, nullable=False)

    Farmacia_id = Column(Integer, ForeignKey("farmacia.id"))

    farmacia = relationship("Farmacia", back_populates= "medicamento")
    def __init__ (self,nome , validade , preco , farmacia):
        self.nome=nome
        self.validade=validade
        self.preco=preco
        self.farmacia=farmacia

    def __repr__(self):
        return f"medicamentoS: id={self.id} - nome={self.nome} - validade={self.validade} - preco={self.preco}"

Base.metadata.create_all(engine)
                   



