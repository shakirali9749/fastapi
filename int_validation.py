from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
	*, item_id: int = Path(title="The ID of the item to get",ge=0, le=100), 
	q:str
):
	results = {'item_id': item_id}
	print(f'>>>>>>>>>>>>>>>>>>>>>> : {q}')
	if q:
		results.update({'q':q})
	return results