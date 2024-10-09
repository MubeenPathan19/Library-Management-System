from fastapi import FastAPI
from app.routes import auth, books, members
from app.database import engine
from app.models import Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Register the routers
app.include_router(auth.router, prefix="/auth")
app.include_router(books.router, prefix="/books")
app.include_router(members.router, prefix="/members")

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System"}
