from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers.auth_router import router as auth_router
from app.routers.products_router import router as products_router
from app.routers.ai_router import router as ai_router

# Create all tables (for development)
# In production, you will use Alembic migration instead of this
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ecommerce + AI API",
    version="1.0.0"
)

# Allow frontend (Next.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
# app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(auth_router, prefix="/auth")
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(ai_router)

@app.get("/")
def home():
    return {"message": "FastAPI Backend Running Successfully with DB!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)