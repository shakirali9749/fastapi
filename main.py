from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
	alexnet = 'alexnet'
	resnet = 'resnet'
	lenet = 'lenets'

# create FastApi instance
app = FastAPI()

@app.get('/')
async def root():
	return {"message": "hello, world" }


# path parameter
@app.get('/items/{item_id}')
async def read_item(item_id: int):
	return {'item_id': item_id}


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {'model_name': model_name, 'message': 'Deep Learning FWT'}

	if model_name.value == 'lenet':
		return {'model_name': model_name, 'message': 'leCNN all images'}

	return {'model_name': model_name, 'message': 'Have some resiuadels'}


# file path
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
	return {'file_path': file_path}