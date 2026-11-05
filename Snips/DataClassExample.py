from dataclasses import dataclass
from datetime import date

@dataclass
class DataClassWorkOrder:
    id: str
    product_id: str
    quantity: int
    creation_date: str
    delivery_date: str
    status: str
    priority: str

    @classmethod
    def from_dict(cls, data: dict) -> "DataClassWorkOrder":
        return cls(
            id=data["ID"],
            product_id=data["Product_ID"],
            quantity=data["Quantity"],
            creation_date=data["Creation_Date"],
            delivery_date=data["Delivery_Date"],
            status=data["Status"],
            priority=data["Priority"]
        )

    def to_dict(self) -> dict:
        return {
            "ID": self.id,
            "Product_ID": self.product_id,
            "Quantity": self.quantity,
            "Creation_Date": self.creation_date,
            "Delivery_Date": self.delivery_date,
            "Status": self.status,
            "Priority": self.priority
        }