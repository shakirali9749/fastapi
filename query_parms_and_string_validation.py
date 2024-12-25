from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(
# 	q: Annotated[str | None, Query(title='quer string',min_length=3)] = None):
#     result = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
#     if q:
#     	result.update({"q": q})
# 	return result

# alias is just like nick name of q query from the queqest
@app.get("/items/")
async def read_items(
	q: Annotated[str | None, Query(alias="item-query")] = None):
    result = {"items": [{"item_id": "foo"}, {"item_id": "Bar"}]}
    if q:
    	result.update({"q": q})

    return result



@app.get("/hidden_query/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}



