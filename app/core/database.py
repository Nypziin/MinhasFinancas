from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

DB_SERVER = os.getenv("DB_SERVER", "SQLEXPRESS")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_DATABASE = os.getenv("DB_DATABASE", "finance")

# Efetuo a conexão no banco de dados master apenas para ter uma conexão com o SQL Server
MASTER_DATABASE_URL = f"mssql+pyodbc://@{DB_SERVER}/master?driver={DB_DRIVER}&trusted_connection=yes"
master_engine = create_engine(MASTER_DATABASE_URL, isolation_level="AUTOCOMMIT")

# Crio o banco de dados finance se não houver
with master_engine.connect() as conn:
    conn.execute(text("IF DB_ID('finance') IS NULL CREATE DATABASE finance;"))

# Efetuo de fato a conexão com o banco de dados finance
DATABASE_URL = f"mssql+pyodbc://@{DB_SERVER}/{DB_DATABASE}?driver={DB_DRIVER}&trusted_connection=yes"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()