from typing import Union, Literal, Dict
from pydantic import BaseModel, Field

class Material(BaseModel):
    id: str
    name: str
    unit: Union[Literal["kg", "L", "g"] , str] = "kg"
    in_stock: Union[int, float] = 0


class Recipe(BaseModel):
    product_id: str
    ingredients: Dict[str, Union[int, float]] = Field(default_factory=dict)


class Product(BaseModel):
    id: str
    name: str
    abv: Union[float, int]
    brew_time: Union[float, int]
    unit: Literal["days"] = "days"
    packaging: Literal["Casks", "Bottles"]


class WorkOrder(BaseModel):
    id: str
    product_id: str
    quantity: Union[int, float]
    creation_date: str
    delivery_date: str
    status: Literal["open", "in_progress", "completed", "cancelled", "quality_review"]
    priority: Literal["low", "medium", "high"]

