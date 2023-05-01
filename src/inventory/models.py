from sqlalchemy import Column, String, Integer

from src.database import Base
from src.config import settings

class InventoryItem(Base):
    __tablename__ = settings.POSTGRESQL_INVENTORY_TABLE
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = Column(String, index=True)
    person = Column(String, index=True)
    department = Column(String, index=True)
    description = Column(String, index=True)