from fastapi import FastAPI

from src.inventory import inventory_routers

app = FastAPI()

# Include different routes
app.include_router(inventory_routers.router)


@app.get("/")
def root():
    return {"message": "We are online"}

