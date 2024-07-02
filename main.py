import uvicorn
from fastapi import FastAPI
from database import Base, engine, SessionLocal
from routers import user as UserRouter


Base.metadata.create_all(bind=engine) # Create the database tables
app = FastAPI()
app.include_router(UserRouter.router, prefix="/user", tags=["user"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=3, reload=True)
