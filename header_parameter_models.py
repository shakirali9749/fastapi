from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
	# model_config = {"extra": "forbid"}
	
	host: str 
	save_data: bool
	if_modified_since: str | None = None
	traceparent: str | None = None
	x_tags: list[str] = []


@app.get("/items/")
async def read_items(
	headers: Annotated[CommonHeaders, Header()]
):
	return headers