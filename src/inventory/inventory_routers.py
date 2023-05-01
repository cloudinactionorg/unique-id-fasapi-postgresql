from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.inventory.dependencies import get_db
from src.inventory import crud, schemas

router = APIRouter()

@router.get("/inventory_items", response_model=list[schemas.InventoryItem])
async def get_inventory_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_inventory_items(db, skip=skip, limit=limit)
    return items

@router.post("/add_inventory_item", response_model=schemas.InventoryItem)
async def create_inventory_item(
    item: schemas.InventoryItem, db: Session = Depends(get_db)
):
    return crud.create_inventory_item(db=db, item=item)