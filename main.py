from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "C:/Users/ASUS Vivobook/PycharmProjects/pythonProject/mydat abase.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)