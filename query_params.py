from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
	{'item_name': 'foo'},
	{'item_name': 'Bar'},
	{'item_name': 'Baz'},
]


# @app.get('/items/')
# async def read_item(skip: int = 0, limit: int = 10):
# 	return fake_items_db[skip: skip + limit]


# query parms
@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None, short: bool = False):
	item = {'itme_id': item_id}
	if q:
		item.update({'q': q})
	if not short:
		item.update(
			{'Description': 'This is an amazing item that has long description'}
		)
	return item 


# many path parms and Default query parms
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_itme(
	user_id: int, item_id: str, q: str | None = None, short: bool = False
):
	item = {'itme_id': item_id, 'owner_id': user_id}
	if q:
		item.update(
			{'q': q}
		)
	if not short:
		item.update(
			{'Descreption': 'This is an amazing item that has long descreption'}
		)
	return item


# required query parms
@app.get('/users/{user_id}')
async def read_user_items(user_id: str, needy: str, skip: int = 0, limit: int | None = None):
	item = {'user_id': user_id, 'needy': needy, 'skip': skip, 'limit': limit}
	return item 



	


		


