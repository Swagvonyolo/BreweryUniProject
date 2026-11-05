from datetime import date

class WorkOrder:
    def __init__(
        self, 
        id: str, 
        product_id: str, 
        quantity: int, 
        creation_date: str, 
        delivery_date: str, 
        status: str, 
        priority: str
    ):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.creation_date = creation_date
        self.delivery_date = delivery_date
        self.status = status
        self.priority = priority

    @classmethod
    def from_dict(cls, data: dict) -> "WorkOrder":
        return cls(
            id=data["ID"],
            product_id=data["Product_ID"],
            quantity=data["Quantity"],
            creation_date=["Creation_Date"],
            delivery_date=["Delivery_Date"],
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