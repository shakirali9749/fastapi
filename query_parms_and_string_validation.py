from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_item(
	q: Annotated[ str, Query(min_length=4)] 
	):
	results = {"items":[{"item_id": "Foo"},{"item_id": "Bar"}]}
	if q:
		results.update({'q': q})
	# breakpoint()
	return results