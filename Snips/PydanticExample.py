from datetime import date
from Pydantic import BaseModel

class WorkOrder(BaseModel):
    ID: str
    Product_ID: str
    Quantity: int
    Creation_Date: date
    Delivery_Date: date
    Status: str
    Priority: str

# from_dict equivilent
wo = WorkOrder.model_validate(data)

# to_dict equivilent
wo_dict = wo.model_dump(by_alias=True)