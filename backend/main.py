from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import seed
from routers import auth, rules
from scheduler import start_scheduler

# Create tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Smart E-Commerce Automation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(rules.router, prefix="/api", tags=["Automation Rules"])

@app.on_event("startup")
def on_startup():
    seed.seed_db()
    start_scheduler()

@app.get("/")
def read_root():
    return {"message": "Server is running"}
