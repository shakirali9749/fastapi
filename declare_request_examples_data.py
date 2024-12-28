from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import ClassVar, Annotated

app = FastAPI()

class Item(BaseModel):
	name: str # = Field(examples=["foo"])
	description: str | None = None #Field(default=None, examples=["A vary nice Item"])
	price: float # = Field(examples=[3.4])
	tex: float | None = None #Field(default=None, examples=[1.3])

	# model_cnfig: ClassVar[dict] = {
	# 	"json_schema_extra": {
	# 		"examples": [
	# 			{
	# 				"name": "foo",
	# 				"description": "A very Nice Item",
	# 				"price": 22.4,
	# 				"tex": 1.9,
	# 			}
	# 		]
	# 	}

	# }

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results