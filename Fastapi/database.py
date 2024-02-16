from fastapi import FastAPI
from sqlalchemy import create_engine, Column,Integer, String,Float, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()

expenses = Table(
    "expenses",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("amount", Float),
    Column("category", String)
)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommint=False,autoflush=False, bind=engine)

app = FastAPI()

