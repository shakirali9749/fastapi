from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class Image(BaseModel):
	url: HttpUrl
	name: str

class Item(BaseModel):
	name: str
	description: str | None = None
	price: float
	tex: float | None = None
	# simple list of tags have any type of lst
	# tags: list = []
	# Now specific strings, in list there is allow duplications but in set not
	# tags: list[str] = []
	# set of string as a tags for uniqueness
	tags: set[str] = set()
	images: list[Image] | None  = None

class Offer(BaseModel):
	name: str
	description: str | None = None
	price: float
	items: list[Item]


# @app.put("/items/{item_id}")
# async def update_item(
# 	item_id: int, item: Item
# ):
# 	result = {"item_id": item_id, "itme": item}
# 	return result


@app.post("/offers/")
async def create_offer(offer: Offer):
	return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
	return images


