from fastapi import FastAPI
from backend.routes.scan import router as scan_router
from backend.routes.inventory import router as inventory_router

app = FastAPI()

app.include_router(scan_router)
app.include_router(inventory_router)

@app.get("/")
def root():
    return {"message": "busscollab API is running"}