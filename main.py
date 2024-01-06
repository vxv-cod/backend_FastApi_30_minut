import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import user as UserRouter

def create_database():
    '''
    При запуске через консоль или напрямую, создает базу данных
    с описанными таблицами из моделей
    '''
    Base.metadata.create_all(bind=engine)

# create_database()
        
app = FastAPI(
    title="Название документации",
    description="Какое-то описание"
)

app.include_router(UserRouter.router, prefix="/user")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, workers=3)