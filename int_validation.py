from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
	*, item_id: int = Path(title="The ID of the item to get",ge=1, le=100), 
	q:str,
	size: Annotated[float,Query(gt=0,lt=10.5)]
):
	results = {'item_id': item_id}
	print(f'>>>>>>>>>>>>>>>>>>>>>> : {q}')
	if q:
		results.update({'q':q})

	if size:
		results.update({"size": size})
	return results