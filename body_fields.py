"""
you can use validation on body parms , as like as Query params and path parms you will use Body params as well
"""

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()



class Item(BaseModel):
    name: str
    description: str | None =  Field(
        default=None, title="The description of the item",max_length=300
        )
    price: float = Field(
        gt=0, description="the price must be grater than zero"
        )
    tex: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results