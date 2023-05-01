from sqlalchemy.orm import Session
from src.inventory import models, schemas

def generateInventoryID(id, department):
    
    from hashids import  Hashids
    hashids = Hashids(min_length=8)

    if department == 'string':
        prefix = 'cia'
    else:
        prefix = department
    hash = hashids.encode(id)
    inventory_id = f"{prefix}-{hash}"
    return inventory_id

def get_inventory_items(db: Session, skip: int = 0, limit: int = 100):  
    return db.query(models.InventoryItem).offset(skip).limit(limit).all()

def create_inventory_item(db: Session, item: schemas.InventoryItem):
    db_item = models.InventoryItem(**item.dict())
    db.add(db_item)
    db.commit()

    # Generate new inventory_id
    db_item.inventory_id = generateInventoryID(db_item.id, db_item.department)
    db.commit()
    db.refresh(db_item)
    return db_item