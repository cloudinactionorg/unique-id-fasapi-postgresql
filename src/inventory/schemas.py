from pydantic import BaseModel
from pydantic.types import Optional

class InventoryItem(BaseModel):
    id : Optional[int]
    inventory_id : Optional[str]
    person : str
    department : str
    description : str

    class Config:
        orm_mode = True