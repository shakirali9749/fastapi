from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	
	name: str
	description: str | None = None
	price: float
	tex: float | None = None


class User(BaseModel):

	username: str
	full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
# 	item_id: Annotated[int, Path(title="The ID of the item to get",ge=0,le=1000)],
# 	q: str | None = None,
# 	item: Item | None = None
# ):
# 	results = {"item_id": item_id}
# 	if q:
# 		results.update(q=q)
# 	if item:
# 		results.update(item=item)
# 	return results


@app.put("/items/{item_id}")
async def update_item(
	# *,
	item_id: int,
	item: Annotated[Item, Body(embed=True)]
	# user: User,
	# importance: Annotated[int, Body(gt=0)],
	# q: str | None = None
):
	results = {
		"item_id": item_id,
		"item": item,
		# "user": user,
		# "importance": importance
	}
	# if q:
	# 	results.update(q=q)

	return results



# this is request body for remember pourpose only
{
	"item": {
	"name": "Shakir Ali",
	"description": "this is optional and also for testing pourpose",
	"price": 22.7,
	"tex": 3.9
	}, "user":{

    "username":"shakir Ali",
    "fullname": "shakiralisourcekode"
    },
    "importance": 22,

}