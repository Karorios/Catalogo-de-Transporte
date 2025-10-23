from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./transportes.db"

engine = create_engine(DATABASE_URL, echo=True)

# Crear las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Obtener sesión de base de datos
def get_session():
    with Session(engine) as session:
        yield session
