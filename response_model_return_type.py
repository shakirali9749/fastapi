from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

from typing import Any
from pydantic import BaseModel, EmailStr

app = FastAPI()



class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
	"/items/{item_id}",
	response_model=Item,
	response_model_include=["name", "description"],
	# response_model_exclude={"name", "description"},
	# response_model_exclude_unset=True,
)
async def read_item(item_id: str):
	return items[item_id]

@app.get(
	"/items/{item_id}/public/",
	response_model=Item,
	response_model_exclude=["tax"],
)
async def read_item_public_data(item_id:str):
	return items[item_id]

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
	return user

# @app.get('/portal/')
# async def get_portal(teleport: bool = False) -> Response:
# 	if teleport:
# 		return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# 	return JSONResponse(content={"message": "here is your simple message"})
# 	


# @app.get("/portal/")
# async def get_teleport() -> RedirectResponse:
# 	return RedirectResponse(url="https://monkeytype.com/")


# @app.get("/portal", response_model=None)
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}