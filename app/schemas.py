from pydantic import BaseModel, Field

class ChurnFeatures (BaseModel):
    customer_id: int = Field(..., ge = 0)
    credit_score: int = Field(..., ge=0, le=1000)
    country: str
    gender: str
    age: int = Field(..., ge=0, le=120)
    tenure: int = Field(..., ge=0, le=120)
    balance: float = Field(..., ge=0)
    products_number: int = Field(..., ge=0, le=10)
    credit_card: int = Field(..., ge=0, le=1)
    active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)

    