from pydantic import BaseModel
from typing import List

'''
Im using pydantic for serialization and validation purposes
'''


class ReviewCreateModel(BaseModel):
    title: str
    review: str
    product_id: int


class ReviewModel(BaseModel):
    title: str
    review: str

    class Config:
        orm_mode = True
        from_attributes = True


class ProductGetModel(BaseModel):
    title: str
    asin: str
    reviews: List[ReviewModel]

    class Config:
        from_attributes = True
